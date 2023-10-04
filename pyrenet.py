from netmiko import ConnectHandler
from datetime import datetime
import threading

# Get timestamp like dd-MM-yyyy
def timestamp():
    date = datetime.now()
    date = f'{date.day}-{date.month}-{date.year}'
    return date
# Get timestamp like hh:mm:ss dd-MM-yyyy
def precise_timestamp():
    date = datetime.now()
    date = f'{date.hour}:{date.minute}:{date.second} {date.day}-{date.month}-{date.year}'
    return date
    
# Send commands to a cisco router/switch from a config file
def set_conf(router, user, passwd, enable, config_file):
    try:
        device = { 'device_type': 'cisco_ios', 'host': router, 'username': user, 'password': passwd, 'secret': enable, 'verbose': True }
        connection = ConnectHandler(**device)
        connection.enable()
        hostname = connection.find_prompt()[0:-1]
        output = connection.send_config_from_file(config_file)
        date = timestamp()
        with open(f'{hostname}-{date}.txt', 'w') as f:
            f.write(output)
        connection.disconnect()
    except Exceptions as Err:
        print(f'Erreur: {Err}')

# Make a backup of a router/switch configuration file
def get_conf(router, user, passwd, enable):
    try:
        device = { 'device_type': 'cisco_ios', 'host': router, 'username': user, 'password': passwd, 'secret': enable, 'verbose': True }
        connection = ConnectHandler(**device)
        connection.enable()
        hostname = connection.find_prompt()[0:-1]
        output = connection.send_command('show run')
        output = '\n'.join(output.splitlines()[3:])
        date = timestamp()
        with open(f'{hostname}-{date}-backup.txt', 'w') as f:
            f.write(output)
        connection.disconnect()
    except Exceptions as Err:
        print(f'Erreur: {Err}')

# Make a backup of a group of routers/switchs listed in a file; use multi-threading
def get_conf_all(router_file, user, passwd, enable):
    try:
        with open(router_file, 'r') as f:
            routers = f.read().splitlines()
        threads = list()

        # Multi-threading
        for router in routers:
            th = threading.thread(target=get_conf, args=(router, user, passwd, enable))
            threads.append(th)

        for th in threads:
            th.start()

        for th in threads:
            th.join()
    except Exceptions as Err:
        print(f'Erreur:{Err}')

# Send commands from a config file to a list of routers/switchs
def set_conf_all(router_file, user, passwd, enable, config_file):
    try:
        with open(router_file, 'r') as f:
            routers = f.read().splitlines()
        threads = list()

        # Multi-threading
        for router in routers:
            th = threading.thread(target=set_conf, args=(router, user, passwd, enable, config_file))
            threads.append(th)

        for th in threads:
            th.start()

        for th in threads:
            th.join()
            
    except Exceptions as Err:
        print(f'Erreur:{Err}')



