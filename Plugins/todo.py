



def todo(user,system,Param):
    import os
    if Param[0]=="see":
        if os.stat(os.path.join(system.baseDir,"Data", "tasks.txt")).st_size==0:
            print("Welp, you have no tasks")
        else:
            with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'r') as f:
                for line in f:
                    a=line.strip()
                    num,task=a.split(':')
                    print(f"{num}.{task}")
                
    elif Param[0]=="add":
        print(Param)
        task=' '.join(Param[1:])
        print(task)
        try:
            with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'r') as f:
                l=f.readlines()[-1].strip()
                num,a=l.split(':')
        except:
            num=0
        Next=int(num)+1
        with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'a') as f:
            f.write(f"{Next}:{task}")
            f.write('\n')

FUNCTION_MAP={"TODO":todo}
