import optparse

class vsphere(object):

    def __init__(self):
        print "Test1"

    def asdf(self):
        print "Test2"

def main():
    print "Main"
    parser = optparse.OptionParser()
    parser.add_option('--list', action='store_true', dest='list', default=False, help='Output inventory groups and hosts')
    print



if __name__ == '__main__':
    main()