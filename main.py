#Imports:
import os
import sys
import bcrypt
from viper import commands

#Classes:
class User:
    def __init__(self,userName,appsList,pluginsList):
        self.userName=userName
        self.appsList=appsList
        self.pluginsList=pluginsList
class System:
    def __init__(self,baseDir,goAhead):
        self.baseDir=baseDir
#Functions:
def initUser(name,baseDir):
    appsList=[]
    f=os.path.join(baseDir,"Apps")
    for file in os.listdir(f):
        if file.endswith(".py"):
            appsList.append(file)
    pluginsList=[]
    f=os.path.join(baseDir,"Plugins")
    for file in os.listdir(f):
        if file.endswith(".py"):
            pluginsList.append(file)
    return name,appsList,pluginsList
            
    


#Body:
def strt():
    yield "[INFO]:WELCOME"
    system = System(os.path.dirname(os.path.abspath(__file__)), False)    
    file = os.path.join(system.baseDir, "user.txt")

    if os.path.getsize(file) == 0:
        # Setup new account
        yield "[INFO]:Let's setup this bad boy"
        name = yield "[QUERY]:Account name:"
        password = yield "[QUERY]Password:"
        check = yield "[QUERY]:Again:"

        if check == password:
            yield "[INFO]:Creating that account..."
            password = password.encode()
            put = bcrypt.hashpw(password, bcrypt.gensalt())
            with open(file, 'w') as f:
                f.write(f"{name}:{put.decode()}")  # store hash as string
            yield "[SUCCESS]:Account created!"
            name, appsList, pluginsList = initUser(name, system.baseDir)
            user = User(name, appsList, pluginsList)
            goAhead = True
        else:
            yield "[ERROR]: Both don't match. Get checked for dementia."
            goAhead = False

    else:
        # Existing user login
        with open(file, 'r') as f:
            for line in f:
                u, p = line.strip().split(':')
                stored_hash = p.encode()  # turn hash back to bytes

        n = 1
        while n <= 5:
            guess = yield "[QUERY]:Password:"
            guess = guess.encode()
            if bcrypt.checkpw(guess, stored_hash):
                yield "[INFO]:Logging in..."
                yield "[SUCCESS]:Logged in"
                name, appsList, pluginsList = initUser(u, system.baseDir)
                user = User(name, appsList, pluginsList)
                goAhead = True
                break
            else:
                yield "[ERROR]: Incorrect password. Just go get your brain examined, unc"
                n += 1
        else:
            yield "[ERROR]: Hacking attempt. FUCK OFF YA HACKER"
            sys.exit()

    if goAhead:
        while True:
            Input = yield ">>>"
            msg = commands.parse(Input, user, system)
            yield msg

            
       

        
