import serial
from django.db import models
import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219


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


def get_battery_voltage():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        print(ser)
    except Exception as e:
        print('Exception: ')
        print(e)
        return None

    ser.reset_input_buffer()

    while ser.in_waiting == 0:
        pass

    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print('line')
        print(line)
        result_list = line.split(";")
        battery_voltage = result_list[5]
        return battery_voltage


def get_result_from_rpi():
    battery_voltage = get_battery_voltage()
    i2c_bus = board.I2C()  # uses board.SCL and board.SDA
    # i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

    ina219 = INA219(i2c_bus)
    # optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
    ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
    ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
    # optional : change voltage range to 16V
    ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

    bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    current = ina219.current  # current in mA
    power = ina219.power  # power in watts

    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage

    result = Result.objects.create(
        bus_voltage_V='{0:.2f}'.format(bus_voltage),
        shunt_voltage_mV='{0:.2f}'.format(shunt_voltage),
        load_voltage_V='{0:.2f}'.format(bus_voltage+shunt_voltage),
        current_mA='{0:.2f}'.format(current / 1000),
        power_mW='{0:.2f}'.format(power/1000),
        battery_voltage='{0:.2f}'.format(float(battery_voltage)),
    )
    print(result)
    return result

