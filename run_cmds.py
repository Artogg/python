# To run commands asynchronously on a device and return to prompt the output
import asyncio


async def run(cmd):
  proc = await asyncio.create_subprocess_shell(cmd,
                                               stdout=asyncio.subprocess.PIPE,
                                               stderr=asyncio.subprocess.PIPE)
  stdout, stderr = await proc.communicate()
  print(f'{cmd} returned status code: {proc.returncode}')
  if stdout:
    print(f'STDOUT:\n{stdout.decode("UTF-8")}')

  if stderr:
    print(f'STDERR:\n{stderr.decode("UTF-8")}')


async def main(cmds):
  tasks = []
  for cmd in cmds:
    tasks.append(run(cmd))
  await asyncio.gather(*tasks)


cmds = ('ifconfig', 'ls', 'who')
asyncio.run(main(cmds))
