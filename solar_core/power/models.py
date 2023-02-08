import serial
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

    @staticmethod
    def get_result():
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
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
            )
            print(result)
            return result
