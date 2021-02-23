"""

	This file is part of Librepunch.

    Librepunch is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Librepunch is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Librepunch.  If not, see <https://www.gnu.org/licenses/>.
    
"""
import shelve
import threading

class adminAccess:
	pass
	
class userAccess:
	pass
	
class eventHandlerk:
	
	def __init__(self):
		
		cli = threading.Thread(target=self.run)
		cli.daemon = True
		cli.start()
		
		self.tempCLI()
		
	def run(self):
		global cmdStack
		while True:
			if cmdStack != []:
				temp = cmdStack
				cmdStack = []
				for i in temp:
					self.proc(i)
		
	def tempCLI(self):
		cmd = input("temp$ ")
		while True:
			cmdStack.append(cmd)
			cmd = input("temp$ ")
			
	def proc(self, cmd):
		print("proccessed " + cmd)

def init():
	global userData
	userData = shelve.open("userData.dat")
	
	global cmdStack
	cmdStack = []
	
	eventHandlerk()

if __name__ == "__main__":
	init()
