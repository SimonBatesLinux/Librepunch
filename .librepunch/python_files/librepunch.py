"""

	This file is part of librepunch.

    librepunch is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    librepunch is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with librepunch.  If not, see <https://www.gnu.org/licenses/>.

"""


import sys
import os
import shelve
import settings
import time

# Global varibles
global USER_FILE
global USERS
global CLOCKED
global LOG_FILE
USER_FILE = "/home/pi/.librepunch/data_files/user.dat"
LOG_FILE = "/home/pi/.librepunch/data_files/USER.log"
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
			os.system("clear")
			print(" librepunch  Copyright (C) 2021  Simon Bates\n    This program comes with ABSOLUTELY NO WARRANTY.\n    This is free software, and you are welcome to redistribute it under certain conditions.")
			USERS = shelve.open(USER_FILE)
			while True:
				statusOverview()
				pin = input(settings.user_prompt)
				if pin == "exit":
					USERS.close()
					os.system("sh")
					USERS = shelve.open(USER_FILE)
				else:
					valid = checkpin(pin)
					if valid:
						cur = time.localtime()
						curTime = str(cur.tm_mday) + "/" + str(cur.tm_mon) + "/" + str(cur.tm_year) + "   " + str(cur.tm_hour) + ":" + str(cur.tm_min) + ":" + str(cur.tm_sec)
						if pin in CLOCKED.keys():
							del(CLOCKED[pin])
							f = open(LOG_FILE, "a")
							f.write("[" + pin + " : " + USERS[pin] + "]: signed out at " + curTime + ".\n")
							f.close()
						else:
							CLOCKED[pin] = USERS[pin]
							f = open(LOG_FILE, "a")
							f.write("[" + pin + " : " + USERS[pin] + "]: signed in at " + curTime + ".\n")
							f.close()
					else:
						input(settings.invalid_pin)
				os.system("clear")
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
