import sys
import os
import argparse

import lib
import utils

script_runner = lib.ScriptRunner(os.path.join("/home/ubuntu/itda-deploy-instance", "bash_scripts"))

def run():
    if not script_runner.run(f'aws_install.sh'):
        return

    utils.generate_nginx_conf()
    
    if not script_runner.run(f'aws_setup_nginx_conf.sh'):
        return

if __name__ == "__main__":
    run()


    


