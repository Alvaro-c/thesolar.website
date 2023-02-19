import serial
from django.db import models


class Result(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    bus_voltage_V = models.FloatField()
    shunt_voltage_mV = models.FloatField()
    load_voltage_V = models.FloatField()
    current_mA = models.FloatField()
    power_mW = models.FloatField()
    battery_voltage = models.FloatField()

    def __str__(self):
        return f"{self.created_at};{self.bus_voltage_V};" \
               f"{self.shunt_voltage_mV};{self.load_voltage_V};" \
               f"{self.current_mA};{self.power_mW};{self.battery_voltage};"


def get_result():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    except Exception as e:
        return None

    ser.reset_input_buffer()

    while ser.in_waiting == 0:
        pass

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        result_list = line.split(";")
        result = Result.objects.create(
            bus_voltage_V=result_list[0],
            shunt_voltage_mV=result_list[1],
            load_voltage_V=result_list[2],
            current_mA=result_list[3],
            power_mW=result_list[4],
            battery_voltage=result_list[5],
        )
        print(result)
        return result

import board
import busio
import adafruit_ina226

def get_result_ina_226():
    i2c = busio.I2C(board.SCL, board.SDA)
    ina226 = adafruit_ina226.INA226(i2c)

    print("Bus Voltage: {:.2f} V".format(ina226.bus_voltage))
    print("Current: {:.2f} mA".format(ina226.current))
    print("Power: {:.2f} mW".format(ina226.power))