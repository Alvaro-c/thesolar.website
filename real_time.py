import datetime
import time
import serial
import argparse


def main():
    parser = argparse.ArgumentParser(description='Gives lectures in real time.')
    parser.add_argument("--s", help="Seconds between results")
    args = parser.parse_args()

    lapse = 1 if not args.s else lapse = args.s

    first_time = int(time.time())

    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        time_now = int(time.time())
        if time_now > first_time + lapse and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            first_time = time_now


if __name__ == '__main__':
    main()
