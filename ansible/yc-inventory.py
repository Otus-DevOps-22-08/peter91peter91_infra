#!/bin/env python3
import argparse
import json
import subprocess
OUTPUT_FILE = './dynamic-inventory.json'

class YcInventory:
    def __init__(self):
        self.inventory = {
            "_meta":
            {
                "hostvars": {},
            }
        }
        self.yc_instances = None
        self.fill_dynamic_inventory()  # заполняем inventory

        output = json_format_dict(   #объявляем и заполняем переменную вывода
            self.inventory,
        )
        print(output)
        with open(OUTPUT_FILE, 'w') as file:   #пишем в файл наш вывод
            file.write(output)
            file.close()
###########################################################################################
    def get_yc_instances(self):   #получаем список инстансов от Yandex
        self.yc_instances = json.loads(
            subprocess.getoutput('yc compute instance list --format json')
        )

    def fill_dynamic_inventory(self): #заполняем inventory
        self.get_yc_instances()
        for instance in self.yc_instances:
            group_name = instance['name'].replace('reddit-', '')  #пишем имя инстанса, удаляем слова reddit-  в названиях
            host = f'{group_name}server'   #записываем имя хоста каждый раз проходя цикл
            for iface in instance['network_interfaces']:
                primary_iface = iface['primary_v4_address']
                try:
                    ext_ip = primary_iface['one_to_one_nat']['address']   #пытаемся найти внешний адрес если имеется
                    break
                except KeyError:
                    ext_ip = None
            if not ext_ip:
                continue
            self.inventory['_meta']['hostvars'].update({host: {'ansible_host': ext_ip}})  #дописываем адреса в вывод
            self.inventory.update(
                {
                    group_name: {'hosts': [host]}   #дописываем хосты  в вывод
                }
            )

def json_format_dict(data):
        return json.dumps(data)    #возвращает накопленные данные для Вывода output

if __name__ == '__main__':   #для возможности экспорта этого скрипта в другой скрипт
    YcInventory() #создание инстанса класса
