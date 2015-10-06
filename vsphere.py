import argparse

class vsphere(object):

    def __init__(self):
        print "Test1"

    def asdf(self):
        print "Test2 "

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers')

    args = parser.parse_args()
    print(args.accumulate(args.integers))




if __name__ == '__main__':
    main()