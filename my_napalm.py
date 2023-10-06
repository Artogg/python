from napalm import get_network_driver
import json

def timestamp_date():
  date = datetime.now()
  date = f'{date.day}{date.month}{date.year}'
  return date

def open_ssh_cisco(router, user, passwd, enable):
  driver = get_network_driver('ios')
  optional_args = {'secret': enable}
  ios = driver(router, user, passwd, optional_args=optional_args)
  ios.open()

def close_ssh(ios):
  ios.close()

def get_arp_export(json_file,ios)
  output = ios.get_arp_table()
  for item in output:
    with open(json_file, 'w') as f:
      json.dump(output, f, sort_keys = True, indent= 4)

def get_arp(ios):
  output = ios.get_arp_table()
  for item in output:
    json.dumps(output, sort_keys= True, indent= 4)

def backup_cisco(ios):
  output = ios.get_config(retrieve='startup')
  hostname = ios.get_facts()['hostname']
  date = timestamp_date()
  dump = json.dump(output, sort_keys= True, indent= 4)
  with open(f'{hostname}_backup_{date}.json', 'w') as f:
    f.write(dump)
  

def get_facts(ios):
  output = ios.get_facts()
  print(json.dumps(output, sort_keys= True, indent= 4))

def get_int(ios):
    output = ios.get_interfaces()
    print(json.dumps(output, sort_keys= True, indent= 4))

def get_int_counters(ios):
    output = ios.get_interfaces_counters()
    print(json.dumps(output, sort_keys= True, indent= 4))  
  
 def get_int_ip(ios):
    output = ios.get_interfaces_ip()
    print(json.dumps(output, sort_keys= True, indent= 4))

 def get_bgp_neighbors(ios):
    output = ios.get_bgp_neighbors()
    print(json.dumps(output, sort_keys= True, indent= 4))

 def get_users(ios):
    output = ios.get_users()
    print(json.dumps(output, sort_keys= True, indent= 4))

def get_mac_table(ios):
  output = ios.get_mac_address_table()
  print(json.dumps(output, sort_keys= True, indent= 4))

 def send_ping(ip,ios):
    output = ios.ping(ip)
    print(json.dumps(output, sort_keys= True, indent= 4)) 

def send_extended_ping(ip_src, ip_dest, count,ios):
  output = ios.ping(destination= ip_dest, count= count, source= ip_src)
  print(json.dumps(output, sort_keys= True, indent= 4)) 

def send_cmds(config_file,ios):
  ios.load_merge_candidate(config_file)
  ios.commit_config()

def rollback(ios):
  ios.rollback()
  
