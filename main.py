import argparse
import engine.importdir
engine.importdir.do("module", globals())


def user_Arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-on', default="Empty", metavar='Example', nargs='+', help='Help')
    parser.add_argument('-do', default="Empty", metavar='Example', nargs='+', help='Help')
    parser.add_argument('-run', default="Empty", metavar='Example', nargs='+', help='Help')
    parser.add_argument('-m', '-module', default="Empty", metavar='Example', nargs='+', help='Help')

    args = parser.parse_args()
    print args.run


def main():
    user_Arguments()




if __name__ == '__main__':
    main()