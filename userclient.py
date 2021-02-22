"""
Version: Dev 0.1.0
Desc: A user front end for time clocking.
Notes: shutdown feature currently disabled
"""
import os
import time

def clear():
    os.system("clear")

def shutdown():
    os.system("echo shutting down")
    pause()
    exit()

def pause():
    time.sleep(3)

def numInput(text):
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
    defPASS = "1234"
    def __init__(self):
        pass
    
    def getPASS(self):
        return self.defPASS

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

    welcome = "welcome!"
    user_prompt  = "[user pin]$ "

    def __init__(self):
        print(self.welcome)
        self.handler()

    def handler(self):
        cmd = numInput(self.user_prompt)
        while True:
            if cmd == "-error":
                pass
            else:
                handler.handleData(cmd)
            clear()
            print("In bathroom:")
            for i in clocked:
                print(i[1])
            cmd = numInput(self.user_prompt)

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
