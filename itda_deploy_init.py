import sys
import os
import argparse

import lib
import utils

script_runner = lib.ScriptRunner(os.path.join("/home/ubuntu/itda_deploy_instnace", "bash_scripts"))

def run():
    if not script_runner.run(f'aws_setup_init.sh'):
        return

    if not utils.generate_nginx_conf():
        return
    
    if not script_runner.run(f'aws_setup_nginx_conf.sh'):
        return
    


if __name__ == "__main__":
    run()


    


