
def stats(baseDir,chtype,c):
    import os
    from datetime import date
    tDate=str(date.today())
    if os.stat(os.path.join(baseDir,"Data", "stats.txt")).st_size==0:
        
        with open(os.path.join(baseDir,"Data", "stats.txt"),'w') as f:
            f.write(f"{tDate}:0,0")
            a=0
            b=0
    else:
        with open(os.path.join(baseDir,"Data", "stats.txt"),'r') as f:
            l=f.readlines()[-1].strip()
            d,v=l.split(':')
            a,b=v.split(',')
            a=int(a)
            b=int(b)
            
        if d!=tDate:
            with open(os.path.join(baseDir,"Data", "stats.txt"),'a') as f:
                f.write('\n')
                f.write(f"{tDate}:0,0")
                a=0
                b=0
   
    if chtype=='tasksS':
        if c=='+':
            newB=b+1
        elif c=='-':
            newB=b-1
        with open(os.path.join(baseDir,"Data", "stats.txt"),'r') as f:
            lines=f.readlines()
        lines[-1]=f"{tDate}:{a},{newB}"
        with open(os.path.join(baseDir,"Data", "stats.txt"),'w') as f:
            f.writelines(lines)
    elif chtype=='tasksC':
        if c=='+':
            newA=a+1
        elif c=='-':
            newA=a-1
        with open(os.path.join(baseDir,"Data", "stats.txt"),'r') as f:
            lines=f.readlines()
        lines[-1]=f"{tDate}:{newA},{b}"
        with open(os.path.join(baseDir,"Data", "stats.txt"),'w') as f:
            f.writelines(lines)    
            
        
                
        



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
        
        task=' '.join(Param[1:])
        
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
        stats(system.baseDir, 'tasksS','+')
    elif Param[0]=="complete":
        if os.stat(os.path.join(system.baseDir,"Data", "tasks.txt")).st_size==0:
            print("Welp, you have no tasks to complete. Loser.")
        else:
            taskDic={}
            with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'r') as f:
                for line in f:
                    a=line.strip()
                    num,task=a.split(':')
                    taskDic[num]=task

          
            p=' '.join(Param[1:])
            
            try:
                p=int(p)
                status='int'
            except:
                p=str(p)
                status='str'
            if status=='int':
            
                if str(p) in taskDic.keys():
                    
                    p=str(p)
                    del taskDic[p]
                    
                    
                    i=1
                    
                    ntaskDic={}
                    for item in taskDic:
                        val=taskDic[item]
                        ntaskDic[i]=val
                        i+=1
                    
                    with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'w') as f:
                        for item in ntaskDic:
                            val=ntaskDic[item]
                            f.write(f'{item}:{val}')
                            f.write('\n')
            else:
                for item in taskDic:
                    if p==taskDic[item]:
                        key=item
                        break
                del taskDic[key]
                    
                    
                i=1
                    
                ntaskDic={}
                for item in taskDic:
                    val=taskDic[item]
                    ntaskDic[i]=val
                    i+=1
                    
                with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'w') as f:
                    for item in ntaskDic:
                        val=ntaskDic[item]
                        f.write(f'{item}:{val}')
                        f.write('\n')
            stats(system.baseDir, 'tasksC','+')
    elif Param[0]=="cancel":
        if os.stat(os.path.join(system.baseDir,"Data", "tasks.txt")).st_size==0:
            print("Welp, you have no tasks to cancel. Loser.")
        else:
            taskDic={}
            with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'r') as f:
                for line in f:
                    a=line.strip()
                    num,task=a.split(':')
                    taskDic[num]=task

          
            p=' '.join(Param[1:])
            
            try:
                p=int(p)
                status='int'
            except:
                p=str(p)
                status='str'
            if status=='int':
            
                if str(p) in taskDic.keys():
                    
                    p=str(p)
                    del taskDic[p]
                    
                    
                    i=1
                    
                    ntaskDic={}
                    for item in taskDic:
                        val=taskDic[item]
                        ntaskDic[i]=val
                        i+=1
                    
                    with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'w') as f:
                        for item in ntaskDic:
                            val=ntaskDic[item]
                            f.write(f'{item}:{val}')
                            f.write('\n')
            else:
                for item in taskDic:
                    if p==taskDic[item]:
                        key=item
                        break
                del taskDic[key]
                    
                    
                i=1
                    
                ntaskDic={}
                for item in taskDic:
                    val=taskDic[item]
                    ntaskDic[i]=val
                    i+=1
                    
                with open(os.path.join(system.baseDir,"Data", "tasks.txt"),'w') as f:
                    for item in ntaskDic:
                        val=ntaskDic[item]
                        f.write(f'{item}:{val}')
                        f.write('\n')
            stats(system.baseDir, 'tasksS','-')   
                           
                        
                                                
                        
                
        
FUNCTION_MAP={"TODO":todo}
