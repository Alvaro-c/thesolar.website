import datetime
import time
import serial
import os


def write_to_file(path, line):
    with open(path, 'a+') as f:
        f.write(f"{line}\n")
        f.close()


def main():

    start_time = datetime.datetime.now().strftime('%d.%m.%Y')
    first_time = int(time.time())
    lapse = 60
    absolute_path = os.path.dirname(__file__)
    path = f"/home/pi/projects/thesolar.website/django/the_solar_website_media/results/results.txt"
    # path = f"{absolute_path}/django/the_solar_website/media/results/results.txt"

    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()

    line = 'DateTime;Bus voltage (V);Shunt Voltage (mV);Load Voltage (V);Current (mA);Power (mW)'
    write_to_file(path, line)
    print(line)

    while True:
        time_now = int(time.time())
        if time_now > first_time + lapse and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            ser.reset_input_buffer()
            line = f"{datetime.datetime.now().strftime('%d.%m.%Y - %H:%M')};{line}"
            write_to_file(path, line)
            print(line)
            first_time = time_now


if __name__ == '__main__':
    main()
