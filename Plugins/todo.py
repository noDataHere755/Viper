



def todo(user,system,Param):
    import os
    if Param[0]=="see":
        
        with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'r') as f:
            for line in f:
                a=line.strip()
                
                print(a,end=' ')
                print('\n')
    elif Param[0]=="add":
        task=' '.join(Param[1:])
        with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'a') as f:
            f.write(task)
            f.write('\n')

FUNCTION_MAP={"TODO":todo}
