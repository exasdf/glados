import argparse
import engine
import lib
import os



def get_User_Arguments():

    getArguments = argparse.ArgumentParser(description='Process some integers.',)
    getArguments.add_argument('-on',
                             default="Empty",
                             metavar='Example',
                             help='Help')

    getArguments.add_argument('-do',
                             default="Empty",
                             metavar='Example',
                             help='Help')

    getArguments.add_argument('-run',
                             default="Empty",
                             metavar='Example',
                             nargs='+',
                             help='Help')

    getArguments.add_argument('-module',
                             '-m',
                             default="Empty",
                             metavar='Example',
                             nargs='+',
                             help='Help')

    arguments = getArguments.parse_args()

    return arguments

def execute(on, do, run, module):

    if do != "Empty":
        print do

    elif run != "Empty":
        print run

    elif module != "Empty":
        os.system('python module/' + module[0] + '.py' + " " + module[1])

    else:
        print '\033[91m' + u'\u2716'  + "  Invalid operation" + '\033[0m'
        exit()


def main():
    userInput = get_User_Arguments()
    execute(userInput.on, userInput.do, userInput.run, userInput.module)

if __name__ == '__main__':
    main()

