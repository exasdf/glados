import module
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    args = parser.parse_args()
    print args.echo


    dog = module.Dog()
    dog.whoAmI()
    dog.eat()
    dog.bark()