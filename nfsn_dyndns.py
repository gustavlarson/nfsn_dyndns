#!/usr/bin/env python3
"""NFSN DYNDNS

Updates DNS records on NearlyFreeSpeech.net when a change of public ip is
detected.

Configure login name and api key in /etc/nfsn_dundns.conf,
see nfsn_dyndns.conf.example

Requires ipgetter and python-nfsn
https://github.com/phoemur/ipgetter
https://github.com/ktdreyer/python-nfsn


"""
import json
import os
import tempfile

import ipgetter
from nfsn import Nfsn

CONFIG_FILE = '/etc/nfsn_dyndns.conf'

IP_FILE = '{directory}/nfsn_dyndns.ip'.format(directory=tempfile.gettempdir())
PUBLIC_IP = ipgetter.myip()

with open(CONFIG_FILE) as config_raw:
    CONFIG = json.load(config_raw)

NFSN = Nfsn(login_file=CONFIG_FILE)


def main():
    """Main function. Check if update is required and perform update"""
    if update_needed():
        print('DNS record update is needed')
        domain = CONFIG['domain']
        records = NFSN.dns(domain).listRRs()
        for record in records:
            if record['type'] == 'A' and record['data'] != PUBLIC_IP:
                print('Removing {name}.{domain} with data: {data}'.format(
                    domain=domain,
                    name=record['name'],
                    data=record['data']
                    ))
                NFSN.dns(domain).removeRR(
                    name=record['name'],
                    type=record['type'],
                    data=record['data']
                    )
                print('Adding {name}.{domain} with data: {data}'.format(
                    domain=domain,
                    name=record['name'],
                    data=PUBLIC_IP
                    ))
                NFSN.dns(domain).addRR(
                    name=record['name'],
                    type=record['type'],
                    data=PUBLIC_IP
                    )


def update_needed():
    """Check if an update of the DNS resource records are needed"""
    print('Current public IP: {ip}'.format(ip=PUBLIC_IP))

    if os.path.isfile(IP_FILE):
        file_handle = open(IP_FILE, 'r')
        if file_handle.read() == PUBLIC_IP:
            print('{file} matches public ip'.format(file=IP_FILE))
            file_handle.close()
            return False
        else:
            print('{file} does not match public ip'.format(file=IP_FILE))
            file_handle.close()
            os.remove(IP_FILE)
            return True
    else:
        if all_records_up_to_date():
            print('All records matches public ip, writing {file}'.format(
                file=IP_FILE
                ))
            file_handle = open(IP_FILE, 'w')
            file_handle.write(PUBLIC_IP)
            file_handle.close()
            return False
        else:
            print('All records does not match public ip')
            return True


def all_records_up_to_date():
    """Check if all DNS resource records are matching the public ip"""
    domain = CONFIG['domain']
    records = NFSN.dns(domain).listRRs()
    for record in records:
        if record['type'] == 'A':
            if record['data'] != PUBLIC_IP:
                return False
    return True

if __name__ == '__main__':
    main()
