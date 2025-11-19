def Print(user,system,Param):
    x=''
    for i in Param:
        x+=i
        x+=' '
    return x
def Whoami(user,system):
    return f"You're {user.userName}, unc. Seems like your username is just like your new year's resolution."
FUNCTION_MAP={'PRINT':Print,'WHOAMI':Whoami}
