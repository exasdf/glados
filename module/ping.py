__author__ = 'ex'

import os
import click

@click.command()
@click.option('-t', '--target', default=None, help='')


def hostname(target):
    print target


def ping(input):
    response = os.system("ping -c 3 " + input + " >/dev/null 2>&1" )

    if response == 0:
        print '\033[92m' + input + " is Up!" + '\033[0m'
        return "Up"
    else:
        print '\033[91m' + input + " is Down!" + '\033[0m'
        return "Down"
