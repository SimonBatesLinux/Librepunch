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
import os
import time
import settings

# universal functions

def clear():
    """ clear screen """
    os.system("clear")

def pause():
    """ pause to display information """
    time.sleep(3)

def numInput(text):
    """ get only number inputs """
    
    # get input
    cmd = input(text)
    
    if cmd != "":

        # check to see if we were given a number
        nums = "0123456789"
        good = True
        err = ""
        for i in cmd:
            if not (i in nums) and good:
                good = False
                err = i

        # return an error
        if not good:
            print("Invalid character \"" + err + "\".")
            pause()
            return "-error"
        else:
            return cmd
        
    else:
        
        # handle no input error
        print("no input given...")
        pause()
        return "-error"

# inerfaces

class serverOffloader:
    """ Handle the time server """
    
    def __init__(self):
        pass

    def sndPin(self, pin):
        """ check for valid pin """
        return True, "name"

class timeHandler:

    """ handler for time clocking. """

    def __init__(self):
        pass

    def handleData(self, pin):
    """ handle a time pin """

        # check pin
        global clocked
        goodPin, user = server.sndPin(pin)

        
        if goodPin:
            
            # check for user being already clocked in
            new = True
            i = 0
            while i < len(clocked):
                
                if clocked[i][0] == pin:

                    #clock our user
                    newClock = []
                    n = 0
                    while n < len(clocked):
                        if n != i:
                            newClock.append(clocked[n])
                        n += 1
                    clocked = newClock
                    new = False
                    break
                
                i += 1
                
            if new:

                # clock in user
                clocked.append([pin, user])
            
        

class interface:
    """ provide a user interface """

    def __init__(self):
        """ give inital alerts and start inferface """
        
        clear()
        print(settings.welcomeMessage)
        print("    Librepunch  Copyright (C) 2021  Simon Bates\n    This program comes with ABSOLUTELY NO WARRANTY; for details type read the LICENSE file.")
        self.handler()
        
    def handler(self):
        """ main interface for users """
        cmd = numInput(settings.user_prompt)
        while True:

            if cmd == "-error":

                # invalid input
                pass
            else:

                # valid user input
                handler.handleData(cmd)

            clear()
            print(settings.location)

            # print clocked in users
            for i in clocked:
                print(i[1])

            # get user input
            
            cmd = numInput(settings.user_prompt)

def init():

    # initialize global variables
    global clocked
    clocked = []
    
    global server
    server = serverOffloader()
    
    global handler
    handler = timeHandler()

    # start user interface
    interface()

if __name__ == "__main__":

    # check if were the main application to avoid imports.
    init()
