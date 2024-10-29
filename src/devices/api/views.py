from django.db.models import ExpressionWrapper, F, FloatField, Sum
from django.db.models.functions import TruncMonth
from ninja import NinjaAPI, Query

from src.devices.api.schemas import (
    MeasurementDeviceRequest,
    MeasurementDeviceResponse,
    MeasurementResponse,
    MetricResponse,
)
from src.devices.models import Measurement, MeasurementDevice

api = NinjaAPI(title='Devices', version='1.0.0')


@api.post('measurement-devices', response=MeasurementDeviceResponse)
def create_measurement_device(request, data: MeasurementDeviceRequest):
    return MeasurementDevice.objects.create(**data)

@api.get('measurement-devices', response=list[MeasurementDeviceResponse])
def list_measurement_devices(request):
    return MeasurementDevice.objects.all()

@api.get('measurements/', response=list[MeasurementResponse])
def retrieve_measurement_device(request, measurement_device_id: int = Query(...)):
    return Measurement.objects.filter(device=measurement_device_id)

@api.get('metrics/', response=list[MetricResponse])
def retrieve_metrics(request, measurement_device_id: int = Query(...)):
    energy_kwh_expr = ExpressionWrapper(
        F("power_w") * F("duration") / (60 * 1000), output_field=FloatField()
    )
    return (
        Measurement.objects
        .filter(device_id=measurement_device_id)
        .annotate(month=TruncMonth("created_at")) # Group by month
        .annotate(energy_kwh=energy_kwh_expr)  # Calculate energy in kWh
        .values("month")
        .annotate(total_consumption=Sum("energy_kwh"))  # Sum up energy for each month
        .order_by("month")
    )
