from django.db import models


class Result(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    bus_voltage_V = models.FloatField()
    shunt_voltage_mV = models.FloatField()
    load_voltage_V = models.FloatField()
    current_mA = models.FloatField()
    power_mW = models.FloatField()

    def __str__(self):
        return f"{self.created_at};{self.bus_voltage_V};" \
               f"{self.shunt_voltage_mV};{self.load_voltage_V};" \
               f"{self.current_mA};{self.power_mW};"
