"""

TODO add license statement

"""


import sys
import os
import shelve
import settings

# Global varibles
global USER_FILE
global USERS
global CLOCKED
global LOG_FILE
USER_FILE = "/home/batess22/.librepunch/data_files/user.dat"
LOG_FILE = "/home/batess22/.librepunch/data_files/USER.log"
USERS = {}
CLOCKED = {}

def statusOverview():
	for i in CLOCKED:
		print(CLOCKED[i])

def checkpin(pin):
	global USERS
	if pin in USERS.keys():
		return True
	else:
		return False
	
def init():
	global USER_FILE
	global USERS
	if len(sys.argv) >= 2:
		if sys.argv[1] == "-s":
			print("TODO add license agreement.") # TODO add license agreement.
			USERS = shelve.open(USER_FILE)
			while True:
				os.system("clear")
				statusOverview()
				pin = input(settings.user_prompt)
				if pin == "exit":
					USERS.close()
					os.system("sh")
					USERS = shelve.open(USER_FILE)
				else:
					valid = checkpin(pin)
					if valid:
						if pin in CLOCKED.keys():
							del(CLOCKED[pin])
							f = open(LOG_FILE, "a")
							f.write("[" + pin + " : " + USERS[pin] + "]: signed out.\n")
							f.close()
						else:
							CLOCKED[pin] = USERS[pin]
							f = open(LOG_FILE, "a")
							f.write("[" + pin + " : " + USERS[pin] + "]: signed in.\n")
							f.close()
					else:
						input("Invalid pin...\nPlease contact Mr. Cochran for assistance.")
		elif sys.argv[1] == "-n":
			perm = input("Doing this will clear all users from the system.\nAre you sure (y/n)? ")
			if perm == "y":
				users = shelve.open(USER_FILE)
				for i in list(users.keys()):
					del(users[i])
				users.sync()
				print("new user file created.")
			else:
				print("exiting...")
		elif sys.argv[1] == "-l":
			users = shelve.open(USER_FILE)
			for i in list(users.keys()):
				print(i + " : " + users[i])
			print("end of list.")
		elif sys.argv[1] == "-e":
			if len(sys.argv) == 4:
				users = shelve.open(USER_FILE)
				users[sys.argv[2]] = sys.argv[3]
				users.sync()
				print("added user \"" + sys.argv[3] + "\".")
			elif len(sys.argv) > 4:
				print("To many input for edit flag.")
			else:
				print("Missing inputs for edit flag.")
		elif sys.argv[1] == "-d":
			if len(sys.argv) == 3:
				users = shelve.open(USER_FILE)
				del(users[sys.argv[2]])
				users.sync()
				print("Removed user.")
		else:
			print("No such flag \"" + sys.argv[1] + "\".")

if __name__=="__main__":
	init()
