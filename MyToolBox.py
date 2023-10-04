import paramiko
import time
from datetime import datetime
from scp import SCPClient


def connect(server_ip, server_port, user, passwd):
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  print(f'Connecting to {server_ip}')
  ssh_client.connect(hostname=server_ip,
                     port=server_port,
                     username=user,
                     password=passwd,
                     look_for_keys=False,
                     allow_agent=False)
  return ssh_client


def get_shell(ssh_client):
  shell = ssh_client.invoke_shell()
  return shell


def send_cmd(shell, cmd, timeout=1):
  print(f'Sending command: {cmd}')
  shell.send(cmd + '\n')
  time.sleep(timeout)


def show(shell, n=10000):
  output = shell.recv(n)
  return output.decode()


def close(ssh_client):
  print('Closing connection.')
  ssh_client.close()


def backup_conf_single(server_ip, server_port, user, passwd, enable):
  client = connect(server_ip, server_port, user, passwd)
  shell = get_shell(client)
  send_cmd(shell, 'term length 0')
  send_cmd(shell, 'enable')
  send_cmd(shell, enable)
  send_cmd(shell, 'sh run')
  output = show(shell)
  output_list = output.splitlines()
  output_list = output_list[11:-1]
  output = '\n'.join(output_list)
  date = datetime.now()
  date = f'{date.day}-{date.month}-{date.year}'
  with open(f'{server_ip}-backup-{date}.txt') as f:
      f.write(output)

def backup_all(server_list, login_dict, server_port):
  pass

def scp_upload_file(server_ip, server_port, user, passwd, localfile, remotefile):
  client = connect(server_ip, server_port, user, passwd)
  shell = get_shell(client)
  scp = SCPClient(client.get_transport())
  scp.put(localfile, remotefile)
  scp.close()

def scp_upload_directory(server_ip, server_port, user, passwd, localdir, remotedir):
  client = connect(server_ip, server_port, user, passwd)
  shell = get_shell(client)
  scp = SCPClient(client.get_transport())
  scp.put(localdir, recursive=True, remote_path= remotedir)
  scp.close()

def scp_download_file(server_ip, server_port, user, passwd, remotefile, localfile):
  client = connect(server_ip, server_port, user, passwd)
  shell = get_shell(client)
  scp = SCPClient(client.get_transport())
  scp.get(remotefile, localfile)
  scp.close()

# def scp_download_dir(server_ip, server_port, user, passwd, remotedir, localdir):
#   client = connect(server_ip, server_port, user, passwd)
#   shell = get_shell(client)
#   scp = SCPClient(client.get_transport())
#   scp.get(remotedir, recursive=True, localdir)
#   scp.close()
