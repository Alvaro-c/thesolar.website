import datetime
import time


def write_time():
    with open('time_stamps.txt', 'a') as f:
        time_stamp = datetime.datetime.now().strftime('%d.%m.%Y - %H:%M')
        f.write(f"{time_stamp}\n")
        f.close()


def main():
    sleep_time = 60 * 60
    while True:
        write_time()
        time.sleep(sleep_time)


if __name__ == '__main__':

    main()
