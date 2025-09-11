
def Print(user,system,Param):
    for i in Param:
        print(i,end=' ')
    print('\n')
    
FUNCTION_MAP={'PRINT':Print}



def parse(Input, user, system):
    try:
        Input = Input.split()
        Length = len(Input)
        if Length == 1:
            if Input[0] in FUNCTION_MAP:
                
                return FUNCTION_MAP[Input[0]](user, system)
            else:
                return "Work in progress"

        elif Length >= 2:
            Action, *Param = Input
            if Action in FUNCTION_MAP:
                
                return FUNCTION_MAP[Input[0]](user,system,Param)
            else:
                return "Working on it"
    except Exception as e:
        err = f"[ERROR]: Parsing or execution failed: {e}"
        return err
