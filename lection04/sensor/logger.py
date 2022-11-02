from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{};temperature;{}\n'\
            .format(time, data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{};pressure;{}\n'\
            .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{};wind_speed;{}\n'\
            .format(time, data))