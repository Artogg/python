from netmiko import ConnectHandler
from datetime import datetime
import threads

def timestamp():
    date = datetime.now()
    date = f'{date.day}-{date.month}-{date.year}'
    return date
    
def precise_timestamp():
    date = datetime.now()
    date = f'{date.hour}:{date.minute}:{date.second} {date.day}-{date.month}-{date.year}'
    return date
    

def set_conf(router, user, passwd, enable, config_file):
    try:
        device = { 'device_type': 'cisco_ios', 'host': router, 'username': user, 'password': passwd, 'secret': enable, 'verbose': True }
        connection = ConnectHandler(**device)
        connection.enable()
        output = connection.send_config_from_file(config_file)
        date = timestamp()
        with open(f'{router}-{date}.txt', 'w') as f:
            f.write(output)
        connection.disconnect()
    except Exceptions as Err:
        print(f'Erreur: {Err}')

def get_conf(router, user, passwd, enable):
    try:
        device = { 'device_type': 'cisco_ios', 'host': router, 'username': user, 'password': passwd, 'secret': enable, 'verbose': True }
        connection = ConnectHandler(**device)
        connection.enable()
        output = connection.send_command('show run')
        output = '\n'.join(output.splitlines()[3:])
        date = timestamp()
        with open(f'{router}-{date}-backup.txt', 'w') as f:
            f.write(output)
        connection.disconnect()
    except Exceptions as Err:
        print(f'Erreur: {Err}')

def get_conf_all(router_file, user, passwd, enable):
    try:
        with open(router, 'r') as f:
            routers = f.read().splitlines()
        for router in routers:
            get_conf(router, user, passwd, enable)
    except Exceptions as Err:
        print(f'Erreur: {Err}')
        
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



