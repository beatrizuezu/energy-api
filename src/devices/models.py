from django.db import models


class MeasurementDevice(models.Model):
    """A model representing the measurement device itself."""
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    """Model to store energy measurements taken from the device."""
    device = models.ForeignKey(MeasurementDevice, on_delete=models.CASCADE)
    power_w = models.PositiveIntegerField(help_text='Power in Watts (W)')
    duration = models.PositiveIntegerField(help_text='Duration of measurement in minutes')
    created_at = models.DateTimeField()

    @property
    def energy_wh(self):
        """Calculate energy consumed in Watt-hours."""
        duration_hours = self.duration / 60  # Convert minutes to hours
        return self.power_w * duration_hours  # Energy in Wh

    @property
    def energy_kwh(self):
        """Calculate energy consumed in kilowatt-hours."""
        return self.energy_wh / 1000  # Convert Wh to kWh

    def __str__(self):
        return (
            'Measurement '
            f'id={self.id}, '
            f'device_id={self.device.id}, '
            f'device_name={self.device.name}, '
            f'power_w={self.power_w}, '
            f'duration={self.duration}',
    )

    @property
    def cost_in_sek(self):
        """Calculate the energy cost in SEK (assuming a fixed rate per kWh)."""
        rate_per_kwh = 2.00  # Assume SEK 2.00 per kWh
        energy_kwh = self.energy_wh / 1000  # Convert Wh to kWh
        return energy_kwh * rate_per_kwh  # Calculate cost
