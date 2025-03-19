import subprocess
import sys

class ScriptRunner:
	def __init__(self, script_path:str):
		self.script_path = script_path

	def run(self, command:str, result:bool = False) -> bool:
		cmd = f'{self.script_path}/{command}'
		if result:
			res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
			if res.returncode == 0:
				print(f"{cmd} command success", res.stdout.strip())
				return res.stdout.strip()
			else:
				print(f"{cmd} command fail", res.stderr)
				return res.returncode
		else:
			res = subprocess.run(cmd, capture_output=False, text=True, shell=True)
			if res.returncode == 0:
				print(f"{cmd} command success", res.stdout)
				return True
			else:
				print(f"{cmd} command fail", res.stderr)
				return False