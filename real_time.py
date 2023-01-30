import datetime
import time
import serial
import argparse


def main():
    parser = argparse.ArgumentParser(description='Gives lectures in real time.')
    parser.add_argument("--s", help="Seconds between results")
    args = parser.parse_args()

    lapse = 5
    if args.s:
        lapse = int(args.s)

    first_time = int(time.time())

    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        time_now = int(time.time())
        if time_now > first_time + (lapse - 1) and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            ser.reset_output_buffer()
            print(f"{datetime.datetime.now().strftime('%d.%m.%Y - %H:%M:%S')} - {line}")
            first_time = time_now


if __name__ == '__main__':
    main()
