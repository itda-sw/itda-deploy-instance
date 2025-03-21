import os

import lib

script_runner = lib.ScriptRunner(os.path.join("/home/ubuntu/itda-deploy-instance", "bash_scripts"))

def get_port() -> str:
  start_port = 9050

  for port in range(start_port, start_port + 1000 - 1):
    if script_runner.run(f"using_port.sh {port}"):
        continue
    return port 
      
def get_nginx_port(subdomain) -> str:
    port = script_runner.run(f'nginx_port.sh {subdomain}', True)
    return port
    