import sys
import os
from jinja2 import Environment, FileSystemLoader
import json

sys.path.append(os.getenv("ENV_PATH"))

from lib import ScriptRunner

script_runner = ScriptRunner(os.path.join(os.getenv("DEV_PATH"), "bash_scripts"))

def get_port() -> str:
      start_port = 9050

      for port in range(start_port, start_port + 1000 - 1):
        if script_runner.run(f"run_using_port.sh {port}"):
            continue
        return port 