import sys
import os
import argparse

import lib

script_runner = lib.ScriptRunner(os.path.join("/home", "itda_deploy_instnace", "bash_scripts"))

def aws_setup_init():
    print("aws_setup_init")

    if not script_runner.run(f'aws_setup_init.sh'):
        return False

def run():
    if aws_setup_init():
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="My CLI tool")
    args = parser.parse_args()

    run(args.assignment, args.tag, args.port)


    


