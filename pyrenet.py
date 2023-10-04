from netmiko import ConnectHandler
from datetime import datetime

def timestamp():
    date = datetime.now()
    return date = f'{date.day}-{date.month}-{date.year}'
  
def set_conf(router_file, user, passwd, enable, config_file):
    try:
        with open(router_file, 'r') as f:
            routers = f.read().splitlines()
        router_list = list()
        for router in routers:
            device = { 'device_type': 'cisco_ios', 'host': router, 'username': user, 'password': passwd, 'secret': enable, 'verbose': True }
            router_list.append(device)
            connection = ConnectHandler(**device)
            connection.enable
            output = connection.send_config_from_file(config_file)
            date = timestamp()
            with open(f'{router}-{date}.txt', 'w') as f:
                f.write(output)
            connection.disconnect()
