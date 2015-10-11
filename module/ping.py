__author__ = 'ex'

import os
import click
import argparse

@click.command()
@click.option('-t', '--target', default=None, help='')

class arguments:
    def get_Arguments(self):
        print "asdf"
        getArguments = argparse.ArgumentParser(description='Process some integers.')
        getArguments.add_argument('-target',
                                 default="Empty",
                                 metavar='Example',
                                 nargs='+',
                                 help='Help')

        arguments = getArguments.parse_args()

        return arguments


class execute:

    def __init__(self, Name="there"):
        print "qwerty"


    def ping(target):
        response = os.system("ping -c 3 " + target + " >/dev/null 2>&1" )

        if response == 0:
            print '\033[92m' + target + " is Up!" + '\033[0m'
            return "Up"
        else:
            print '\033[91m' + target + " is Down!" + '\033[0m'
            return "Down"


def main():
    print "asdf"
    ping.ping()
if __name__ == '__main__':
    main()

