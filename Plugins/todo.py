
def stats(baseDir, chtype, c):
    import os
    from datetime import date
    file_path = os.path.join(baseDir, "Data", "stats.txt")
    today = date.today().isoformat()  # 'YYYY-MM-DD'

    # Ensure the file exists
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        with open(file_path, 'w') as f:
            f.write(f"{today}:0,0\n")
        a = b = 0
    else:
        # Read all non-empty lines
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        # Parse last line
        last_line = lines[-1]
        try:
            d, v = last_line.split(':')
            a, b = map(int, v.split(','))
        except ValueError:
            # If line is malformed, reset counts
            d = today
            a = b = 0

        # Add new line for today if last date isn't today
        if d != today:
            lines.append(f"{today}:0,0")
            a = b = 0

    # Update counters
    if chtype == 'tasksS':
        if c == '+':
            b += 1
        elif c == '-':
            b -= 1
    elif chtype == 'tasksC':
        if c == '+':
            a += 1
        elif c == '-':
            a -= 1

    # Replace or append today's line
    updated_line = f"{today}:{a},{b}"
    if 'lines' in locals() and lines[-1].startswith(today):
        lines[-1] = updated_line
    else:
        lines.append(updated_line)

    # Write back all lines
    with open(file_path, 'w') as f:
        f.write("\n".join(lines) + "\n")
            
        
                
        



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
                           
    elif Param[0]=="stats":

        from datetime import date, timedelta, datetime

        tDate = date.today()
        statsDic = {}

        a = os.path.join(system.baseDir, "Data", "stats.txt")

# Load stats.txt into dict
        with open(a, 'r') as f:
            for line in f:
                d, v = line.strip().split(":")
                statsDic[d] = v

# If user wants last week
        if Param[1] == "week":
            oDate = tDate - timedelta(days=6)  # keep it as a date!

# Output dict
        result = {}

# Iterate through stats dictionary
        for item in statsDic:
            citem = datetime.strptime(item, "%Y-%m-%d").date()  # parse string key to date
            if citem == oDate:
                result[item] = statsDic[item]
            elif oDate < citem <= tDate:  # strictly within week up to today
                result[item] = statsDic[item]

# Print results
        for item in result:
            print(item, ":", result[item])
                
            
                    
                                    
                                                
                        
                
        
FUNCTION_MAP={"TODO":todo}
