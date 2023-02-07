from django.core.management import BaseCommand
import serial

from web.the_solar_website.public_page.models import Result


class Command(BaseCommand):
    help = "Gets one reading result from Arduino"

    def handle(self, *args, **options):
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
