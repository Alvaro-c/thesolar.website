import serial
from django.db import models
import board
from adafruit_ina219 import ADCResolution, INA219


class Result(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    bus_voltage_V = models.FloatField()
    shunt_voltage_mV = models.FloatField()
    load_voltage_V = models.FloatField()
    current_mA = models.FloatField()
    power_mW = models.FloatField()
    solar_panel_current_mA = models.FloatField()

    def __str__(self):
        return f"{self.created_at};{self.bus_voltage_V};" \
               f"{self.shunt_voltage_mV};{self.load_voltage_V};" \
               f"{self.current_mA};{self.power_mW};{self.solar_panel_current_mA};"


def get_solar_panel_current():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    except Exception as e:
        return None

    ser.reset_input_buffer()

    while ser.in_waiting == 0:
        pass

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        try:
            line = float(line)
        except Exception as e:
            line = 0
            print(e)

        return line


def get_result():
    solar_panel_current = get_solar_panel_current()

    i2c_bus = board.I2C()  # uses board.SCL and board.SDA

    ina219 = INA219(i2c_bus)
    # Change configuration to use 32 samples averaging for both bus voltage and shunt voltage
    ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
    ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S

    bus_voltage = ina219.bus_voltage
    shunt_voltage = ina219.shunt_voltage
    current = ina219.current  # current in mA
    power = (ina219.power/1000)  # power in mW

    result = Result.objects.create(
        bus_voltage_V='{0:.2f}'.format(bus_voltage),
        shunt_voltage_mV='{0:.2f}'.format(shunt_voltage),
        load_voltage_V='{0:.2f}'.format(bus_voltage+shunt_voltage),
        current_mA='{0:.2f}'.format(current),
        power_mW='{0:.2f}'.format(power),
        solar_panel_current_mA='{0:.2f}'.format(solar_panel_current),
    )
    print(result)
    return result
