def inp_mod():
    mod = input('Введите режим работы (импорт или экспорт): ')
    return mod


def inp_import():
    sec_name = input('Введите фамилию для поиска: ')
    return sec_name

def view_import (result):
    print(*result, sep='\n') 

def inp_export():
    sec_name = input('Введите фамилию: ')
    name = input('Введите имя: ')
    surname = input('Введите отчество: ')
    phone = input('Введите телефона: ')
    comment = input('Ведите признак телефона (домашний, рабочий): ')
    return '\n',sec_name, name, surname, phone, comment


def view_import_no ():
    print(f'Данные не найдены')