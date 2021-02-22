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

Version: Dev 0.1.0
Desc: A user front end for time clocking.
Notes: shutdown feature currently disabled
"""
import os
import time
import settings

# universal functions

def clear():
    """ clear screen """
    os.system("clear")
    
def shutdown():
    """ shutdown system """
    os.system("echo shutting down")
    pause()
    exit()

def pause():
    time.sleep(3)

def numInput(text):
    """ get only number inputs """
    cmd = input(text)
    if cmd != "":
        nums = "0123456789"
        good = True
        err = ""
        for i in cmd:
            if not (i in nums) and good:
                good = False
                err = i
    
        if not good:
            print("Invalid character \"" + err + "\".")
            pause()
            return "-error"
        else:
            return cmd
    else:
        print("no input given...")
        pause()
        return "-error"
        

class serverOffloader:
    
    def __init__(self):
        pass

    def sndPin(self, pin):
        return True, "name"

class timeHandler:

    def __init__(self):
        pass

    def handleData(self, pin):
        global clocked
        goodPin, user = server.sndPin(pin)
        if goodPin:
            new = True
            i = 0
            while i < len(clocked):
                if clocked[i][0] == pin:
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
                clocked.append([pin, user])
            
        

class interface:

    def __init__(self):
        clear()
        print(settings.welcomeMessage)
        print("    Librepunch  Copyright (C) 2021  Simon Bates\n    This program comes with ABSOLUTELY NO WARRANTY; for details type read the LICENSE file.")
        self.handler()
        
    def handler(self):
        cmd = numInput(settings.user_prompt)
        while True:
            if cmd == "-error":
                pass
            else:
                handler.handleData(cmd)
            clear()
            print(settings.location)
            for i in clocked:
                print(i[1])
            cmd = numInput(settings.user_prompt)

def init():
    global clocked
    clocked = []
    global server
    server = serverOffloader()
    global handler
    handler = timeHandler()
    interface()

if __name__ == "__main__":
    init()
