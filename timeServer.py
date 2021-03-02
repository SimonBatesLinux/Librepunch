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
import sockets

class adminAccess:
        """ api for administrator """
        
        # todo
	pass
	
class userAccess:
        """ api for user client """
        
        #todo
	pass
	
class eventHandlerk:
	
	def __init__(self):
                """ start event handler """

		# start api handler
		cli = threading.Thread(target=self.run)
		cli.daemon = True
		cli.start()

		# start temporary  testing interface
		self.tempCLI()
		
	def run(self):
                """ api handler """

		global cmdStack
		while True:

                        # check for input
			if cmdStack != []:

                                # run all commands
				temp = cmdStack
				cmdStack = []
				for i in temp:
					self.proc(i)
		
	def tempCLI(self):
                """ temporary cli for testing """
                
		cmd = input("temp$ ")
		while True:
			cmdStack.append(cmd)
			cmd = input("temp$ ")
			
	def proc(self, cmd):
                """ proccess all commands """
		print("proccessed " + cmd)

def init():

        # global variables
	global userData
	userData = shelve.open("userData.dat")
	
	global cmdStack
	cmdStack = []

	# start main handler
	eventHandlerk()

if __name__ == "__main__":

        # check to ensure we're not imported
	init()
