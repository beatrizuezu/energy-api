from ninja import NinjaAPI, Query

from src.devices.api.schemas import (
    MeasurementDeviceRequest,
    MeasurementDeviceResponse,
    MeasurementResponse,
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


