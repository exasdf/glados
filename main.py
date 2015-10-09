import argparse

def get_User_Arguments():

    getArguments = argparse.ArgumentParser(description='Process some integers.')
    getArguments.add_argument('-on',
                             default="Empty",
                             metavar='Example',
                             nargs='+',
                             help='Help')

    getArguments.add_argument('-do',
                             default="Empty",
                             metavar='Example',
                             nargs='+',
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

    #Parses module to do engine to return module instructions.
    if do != "Empty":
        COMMAND = do.call(do)  # @UndefinedVariable
        #Executes command over ssh
        engine.ssh.run_Module( on, "vagrant", "vagrant", COMMAND )  # @UndefinedVariable

    #Else run the command straight on hosts
    elif run != "Empty":
        #Executes command over ssh
        engine.ssh.run_Command( on, "vagrant", "vagrant", run )  # @UndefinedVariable

    elif module != "Empty":
        engine.ssh.run_Command( on, "vagrant", "vagrant", run )  # @UndefinedVariable

    else:
        print '\033[91m' + u'\u2716'  + "  Invalid operation" + '\033[0m'
        exit()


def main():
    userInput = get_User_Arguments()
    execute(userInput.on, userInput.do, userInput.run, userInput.module)

if __name__ == '__main__':
    main()

