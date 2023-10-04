from netmiko import ConnectHandler
from datetime import datetime

def timestamp():
    date = datetime.now()
    return date = f'{date.day}-{date.month}-{date.year}'
  
def set_conf(routers, user, passwd, enable, config_file):
    for router in routers:
      try:
          device = { 'device_type': 'cisco_ios', 'host':'router', 'username': user, 'password': passwd, 'secret': enable, 'verbose': True }
          connection = ConnectHandler(**device)
          connection.enable
          output = connection.send_config_from_file(config_file)
          date = timestamp()
          with open(f'{router}-{date}.txt', 'w') as f:
            f.write(output)
          connection.disconnect()
