# 1. Описати атрибут ip за допомогою дескрипторів.
#     атрибут може бути встановленим лише якщо значення - str,
#     відповідає шаблону "x.x.x.x" та кожен блок може бути конвертований в int
# 2. Створити ssh объект та викликати метод connect (імітація підключення)
# 3. Змінити доступ до методу execute. Якщо  self.connected == False має викликатися метод wait_for_connection (імітіція перепідключення),
#   якщо підключення встановлено має спрацювати метод execute.

import socket
import time


def valid_ip(address):
    if not isinstance(address, str):
        return False
    try:
        socket.inet_aton(address)
        return True
    except:
        return False


class IP_Descriptor:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if valid_ip(value):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError('It must be a string in IP format "x.x.x.x"')

    def __del__(self, instance):
        del instance.__dict__[self.__name]


class SSH:
    ip = IP_Descriptor('ip')

    def __init__(self, ip):
        self.ip = ip
        self.connected = False

    def connect(self):
        # Create connection to host
        self.connected = True

    def close_connection(self):
        # Close supported connection type
        self.connected = False

    def wait_for_connection(self, timeout, polling=0.1):
        while timeout > 0:
            if self.connected:
                return self.execute(timeout, polling)
            else:
                print('Still waiting for connection. {} seconds left.'.format(round(timeout, 2)))
                timeout -= polling
                time.sleep(polling)
        raise TimeoutError('Connection timeout')

    def execute(self, timeout, polling=0.1):
        if self.connected:
            print('Connected.')
        else:
            print('wait for connection..')
            self.wait_for_connection(timeout, polling)


a = SSH('10.10.10.1')
try:
    a.execute(5, 1)
except:
    print("Connection error appeared.\nNow trying to connect first")
    a.connect()
    a.execute(5, 1)
