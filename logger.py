from datetime import datetime as dt
from time import time

def import_name_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; поиск фамилии: {}\n'
                    .format(time, data))

def export_name_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; внесение фамилии: {}\n'
                    .format(time, data))