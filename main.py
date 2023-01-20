import datetime
import time
import serial


def main():
    start_time = datetime.datetime.now().strftime('%Y-%m-%d')
    first_time = int(time.time())
    lapse = 60
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    header = 'DateTime;Bus voltage (V);Shunt Voltage (mV);Load Voltage (V);Current (mA);Power (mW)'
    with open(f"{start_time}-power-info.txt", 'a+') as f:
        f.write(f"{header}\n")
        f.close()
    while True:
        time_now = int(time.time())
        if time_now > first_time + lapse and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            with open(f"{start_time}-power-info.txt", 'a+') as f:
                time_stamp = f"{datetime.datetime.now().strftime('%d.%m.%Y - %H:%M')};{line}"
                f.write(f"{time_stamp}\n")
                f.close()
                first_time = time_now


if __name__ == '__main__':
    main()
