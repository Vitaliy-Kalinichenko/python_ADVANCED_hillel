# Задача-1
# У вас есть список(list) IP адрессов. Вам необходимо создать
# класс который будет иметь методы:
# 1) Получить список IP адресов
# 2) Получить список IP адресов в развернутом виде
# (10.11.12.13 -> 13.12.11.10)
# 3) Получить список IP адресов без первых октетов
# (10.11.12.13 -> 11.12.13)
# 4) Получить список последних октетов IP адресов
# (10.11.12.13 -> 13)
ip_list = ['139.18.150.125', '139.18.150.128', '139.18.150.189', '139.18.150.127', '139.18.150.145', '139.18.150.236']


class IpAddress:
    def __init__(self, ip_list):
        self.__ip_list = ip_list

    def get_ip_list(self):
        return self.__ip_list

    def get_ip_list_expanded(self):
        return ['.'.join(ip.split('.')[::-1]) for ip in self.__ip_list]

    def get_ip_without_first_octets(self):
        return [ip[ip.find('.'):] for ip in self.__ip_list]  # ['.'.join(ip.split('.')[1:]) for ip in self.ip_list]

    def get_ip_last_octets(self):
        return [ip[ip.rfind('.'):][1:] for ip in self.__ip_list]


a = IpAddress(ip_list)
print(a.get_ip_list())
print(a.get_ip_list_expanded())
print(a.get_ip_without_first_octets())
print(a.get_ip_last_octets())


# Задача-2
# У вас несколько JSON файлов. В каждом из этих файлов есть
# произвольная структура данных. Вам необходимо написать
# класс который будет описывать работу с этими файлами, а
# именно:
# 1) Запись в файл
# 2) Чтение из файла
# 3) Объединение данных из файлов в новый файл
# 4) Получить путь относительный путь к файлу
# 5) Получить абсолютный путь к файлу
import json
from os import path

with open('example_json_1.json') as file:
    data_1 = json.load(file)

with open('example_json_2.json') as file:
    data_2 = json.load(file)


class FileJson:
    def __init__(self, path_to_file):
        self.__path_to_file = path_to_file

    def write_to_file(self, data):
        with open(self.__path_to_file, 'w') as file:
            json.dump(data, file, indent=4)

    def read_file(self):
        with open(self.__path_to_file) as file:
            return file.read()

    def merging_file(self, instance):
        if isinstance(instance, FileJson):
            with open('merging_file_' + path.basename(self.__path_to_file), 'w') as file:
                file.write(self.read_file() + instance.read_file())
        else:
            raise TypeError(f'{instance} не является экземпляром класса {FileJson.__name__}')

    def relative_path(self):
        return self.__path_to_file

    def absolute_path(self):
        return path.abspath(self.__path_to_file)


a = FileJson('example_json_1.json')
print(a.read_file())
a.write_to_file(data_1)
print(a.read_file())
b = FileJson('example_json_2.json')
a.merging_file(b)
print(a.relative_path())
print(a.absolute_path())


# Задача-3
#
# Создайте класс который будет хранить параметры для
# подключения к физическому юниту(например switch). В своем
# списке атрибутов он должен иметь минимальный набор
# (unit_name, mac_address, ip_address, login, password).
# Вы должны описать каждый из этих атрибутов в виде гетеров и
# сеттеров(@property). У вас должна быть возможность
# получения и назначения этих атрибутов в классе.

class ParamUnit:
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self.__unit_name = unit_name
        self.__mac_address = mac_address
        self.__ip_address = ip_address
        self.__login = login
        self.__password = password

    @property
    def unit_name(self):
        return self.__unit_name

    @unit_name.setter
    def unit_name(self, value):
        self.__unit_name = value

    @property
    def mac_address(self):
        return self.__mac_address

    @mac_address.setter
    def mac_address(self, value):
        self.__mac_address = value

    @property
    def ip_address(self):
        return self.__mac_address

    @ip_address.setter
    def ip_address(self, value):
        self.__ip_address = value

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

unit1 = ParamUnit('unit1', '48:df:37:33:fc:20', '10.11.12.13', 'login_unit1', 'qwerty')
print(unit1.unit_name)
unit1.unit_name = 'new_unit1'
print(unit1.unit_name)

print(unit1.password)
unit1.password = '12345'
print(unit1.password)
