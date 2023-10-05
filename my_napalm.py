from napalm import get_network_driver
import json

def open_ssh_cisco(router, user, passwd, enable):
  driver = get_network_driver('ios')
  optional_args = {'secret': enable}
  ios = driver(router, user, passwd, optional_args=optional_args)
  ios.open()

def close_ssh():
  ios.close()

def get_arp_export(json_file)
  output = ios.get_arp_table()
  for item in output:
    with open(json_file, 'w') as f:
      json.dump(output, f, sort_keys = True, indent= 4)

def get_arp():
  output = ios.get_arp_table()
  for item in output:
    json.dumps(output, sort_keys= True, indent= 4)

def backup_cisco():
  pass

def get_facts():
  output = ios.get_facts()
  print(json.dumps(output, sort_keys= True, indent= 4))

def get_int():
    output = ios.get_interfaces()
    print(json.dumps(output, sort_keys= True, indent= 4))

def get_int_counters():
    output = ios.get_interfaces_counters()
    print(json.dumps(output, sort_keys= True, indent= 4))  
  
 def get_int_ip():
    output = ios.get_interfaces_ip()
    print(json.dumps(output, sort_keys= True, indent= 4))

 def get_bgp_neighbors():
    output = ios.get_bgp_neighbors()
    print(json.dumps(output, sort_keys= True, indent= 4))

 def get_users():
    output = ios.get_users()
    print(json.dumps(output, sort_keys= True, indent= 4))

def get_mac_table():
  output = ios.get_mac_address_table()
  print(json.dumps(output, sort_keys= True, indent= 4))

 def send_ping(ip):
    output = ios.ping(ip)
    print(json.dumps(output, sort_keys= True, indent= 4)) 

def send_extended_ping(ip_src, ip_dest, count):
  output = ios.ping(destination= ip_dest, count= count, source= ip_src)
  print(json.dumps(output, sort_keys= True, indent= 4)) 
