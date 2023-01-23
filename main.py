import datetime
import serial
import os


def main():
    start_time = datetime.datetime.now().strftime('%Y-%m-%d')
    script_dir = os.path.dirname(__file__)
    rel_path = f"server/logs/{start_time}-power-info.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    lapse = 60
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=lapse)
    ser.reset_input_buffer()

    header = 'DateTime;Bus voltage (V);Shunt Voltage (mV);Load Voltage (V);Current (mA);Power (mW)'

    with open(abs_file_path, 'a+') as f:
        f.write(f"{header}\n")
        f.close()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            with open(f"server/logs/{start_time}-power-info.txt", 'a+') as f:
                time_stamp = f"{datetime.datetime.now().strftime('%d.%m.%Y - %H:%M')};{line}"
                f.write(f"{time_stamp}\n")
                f.close()


if __name__ == '__main__':
    main()
