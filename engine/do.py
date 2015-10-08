__author__ = 'ex'


#Take the name of the module and returns
#the module's instructions
def call( action ):
	command = tuple(open("do/"+action, 'r'))
	return command

