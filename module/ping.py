__author__ = 'ex'

import os
import argparse


class arguments(object):
    def get_Input(self):
        getArguments = argparse.ArgumentParser(description='Process some integers.')
        getArguments.add_argument('-target',
                                  '-t',
                                 default="Empty",
                                 metavar='Example',
                                 help='Help')

        arguments = getArguments.parse_args()


        return arguments


class execute(object):


    def ping(self, server_Name):

        response = os.system("ping -c 3 " + server_Name + " >/dev/null 2>&1" )

        if response == 0:
            print '\033[92m' + server_Name + " is Up!" + '\033[0m'
            return "Up"
        else:
            print '\033[91m' + server_Name + " is Down!" + '\033[0m'
            return "Down"


def main():
    userinput = arguments().get_Input()
    print userinput




    #example = execute()
    #example.ping("localhost")


if __name__ == '__main__':
    main()

