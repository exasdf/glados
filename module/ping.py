import argparse
import os




def get_User_Arguments():

    getArguments = argparse.ArgumentParser(description='Process some integers.')
    getArguments.add_argument('-host',
                             '-H',
                             default="Empty",
                             metavar='Example',
                             help='Help')

    arguments = getArguments.parse_args()

    return arguments


def ping(server_Name):
    response = os.system("ping -c 3 " + server_Name + " >/dev/null 2>&1" )

    if response == 0:
        print '\033[92m' + server_Name + " is Up!" + '\033[0m'
        return "Up"
    else:
        print '\033[91m' + server_Name + " is Down!" + '\033[0m'
        return "Down"

def main():
    userInput = get_User_Arguments()
    ping(userInput.host)


if __name__ == '__main__':
    main()
