from solar_core.power.models import Result
from django.contrib import admin


@admin.register(Result)
class ConfirmedOrderRequestAdmin(admin.ModelAdmin):
    model = Result

    list_display = (
        "created_at",
        "bus_voltage_V",
        "shunt_voltage_mV",
        "load_voltage_V",
        "current_mA",
        "power_mW",
    )
