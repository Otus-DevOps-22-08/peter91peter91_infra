#!/bin/env python3

import argparse
import json
import subprocess


OUTPUT_FILE = './dynamic-inventory.json'


class YcInventory:
    def __init__(self):
        # Begin from empty inventory
        self.inventory = {
            "_meta":
            {
                "hostvars": {},
            }
        }
        self.args = None
        self.yc_instances = None

        self.parse_cli_args()
        self.fill_dynamic_inventory()

        if self.args.host:
            try:
               output = json_format_dict(
                    self.inventory['_meta']['hostvars'][self.args.host],
                    pretty=self.args.pretty,
                )
            except KeyError:
                output = f'Host "{self.args.host}" not found.'
        else:
            output = json_format_dict(
                self.inventory,
                pretty=self.args.pretty,
            )

        print(output)

        if self.args.save:
            with open(OUTPUT_FILE, 'w') as file:
                file.write(output)
                file.close()

    def parse_cli_args(self):
        parser = argparse.ArgumentParser(
            description='Make an Ansible Inventory file for YC'
        )
        parser.add_argument(
            '--list',
            action='store_true',
            default=True,
            help='List instances (default: True)',
        )
        parser.add_argument(
            '--host',
            action='store',
            help='Print instance hostvars',
        )
        parser.add_argument(
            '--pretty',
            action='store_true',
            default=False,
            help='Pretty output format (default: False)',
        )
        parser.add_argument(
            '--save',
            action='store_true',
            default=False,
            help='Save inventory to file (default: False)',
        )
        self.args = parser.parse_args()

    def get_yc_instances(self):
        self.yc_instances = json.loads(
            subprocess.getoutput('yc compute instance list --format json')
        )

    def fill_dynamic_inventory(self):
        self.get_yc_instances()
        for instance in self.yc_instances:
            # print(instance)
            # Trim "reddit-" in name
            group_name = instance['name'].replace('reddit-', '')
            host = f'{group_name}server'
            for iface in instance['network_interfaces']:
                primary_iface = iface['primary_v4_address']
                try:
                    ext_ip = primary_iface['one_to_one_nat']['address']
                    break
                except KeyError:
                    ext_ip = None
            if not ext_ip:
                # VM has no external IP, unable to connect
                continue

            self.inventory['_meta']['hostvars'].update({host: {'ansible_host': ext_ip}})
            # NB! In this case we have only one server in group
            self.inventory.update(
                {
                    group_name: {'hosts': [host]}
                }
            )

def json_format_dict(data, pretty=False):
    if pretty:
        return json.dumps(data, sort_keys=True, indent=2)
    else:
        return json.dumps(data)


if __name__ == '__main__':
    YcInventory()
