__author__ = 'ex'

import paramiko

#SSH client
def ssh_exec( hostname, username, password, command, sudo):
	#if Sudo == True it does not require sudo
	#if Sudo == False it does not require sudo

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=hostname, username=username, password=password)

	transport = ssh.get_transport()

	session = transport.open_session()
	session.set_combine_stderr(True)
	session.get_pty()

	session.exec_command(command)

	stdin = session.makefile('wb', -1)
	stdout = session.makefile('rb', -1)

	#Add logic so it checks if root is needed
	if sudo is True:
		stdin.write(password +'\n')
		stdin.flush()
	elif sudo is False:
		stdin.flush()
	else:
		print "Invalid sudo input"


	stdin.flush()

	for line in stdout.read().splitlines():

		#and also prevents printing passwords on logging
		if line == password:
			continue

		#This prevents the log from returning unecessary white spaces
		elif line.isspace() == False:
			print '\033[94m' + "[" + username + "@" + hostname +"]: " + '\033[0m' + "\t" + line + " "

	return


#ssh interface
def run_Module( hostname, username, password, command ):

	for commandToExecute in command:

		sudo = commandToExecute.startswith("sudo")

		if sudo is True:
			ssh_exec( hostname, username, password, commandToExecute, sudo )

		elif sudo is False:
			ssh_exec( hostname, username, password, commandToExecute, sudo )

		else:
			print 'Unrecognized option'

	print '\033[92m' + u'\u2714'  + "  Done" + '\033[0m'

	return

#ssh interface
def run_Command( hostname, username, password, command ):

	sudo = command.startswith("sudo")

	if sudo is True:
		ssh_exec( hostname, username, password, command, sudo )

	elif sudo is False:
		ssh_exec( hostname, username, password, command, sudo )

	else:
		print 'Unrecognized option'

	print '\033[92m' + u'\u2714'  + "  Done" + '\033[0m'

	return




