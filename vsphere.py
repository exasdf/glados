import argparse



def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    #https://docs.python.org/3/library/argparse.html
    parser.add_argument('--integers', metavar='Example', nargs='+', help='an integer for the accumulator')

    args = parser.parse_args()
    print args.integers



if __name__ == '__main__':
    main()