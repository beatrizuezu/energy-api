from ninja import NinjaAPI

from src.devices.api.schemas import MeasurementDeviceRequest,  MeasurementDeviceResponse
from src.devices.models import MeasurementDevice

api = NinjaAPI(title='Devices', version='1.0.0')


@api.post('measurement-devices', response=MeasurementDeviceResponse)
def create_measurement_device(request, data: MeasurementDeviceRequest):
    return MeasurementDevice.objects.create(**data)

@api.get('measurement-devices', response=list[MeasurementDeviceResponse])
def list_measurement_devices(request):
    return MeasurementDevice.objects.all()

@api.get('measurement-devices/{id}', response=MeasurementDeviceResponse)
def retrieve_measurement_device(request, id: str):
    return MeasurementDevice.objects.get(id=id)
