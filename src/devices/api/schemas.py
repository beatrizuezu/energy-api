from datetime import datetime

from ninja import ModelSchema, Schema

from src.devices.models import Measurement, MeasurementDevice


class MeasurementDeviceRequest(Schema):
    name: str
    location: str

class MeasurementDeviceResponse(ModelSchema):
    class Meta:
        model = MeasurementDevice
        fields = ['id', 'name', 'location', 'created_at']


class MeasurementResponse(ModelSchema):
    class Meta:
        model = Measurement
        fields = ['device', 'power_w', 'duration', 'created_at']

