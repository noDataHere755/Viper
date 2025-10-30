import os
import datetime
import csv
from datetime import date, timedelta

def stats(baseDir, chtype, c):
    file_path = os.path.join(baseDir, "Data", "stats.csv")
    today = date.today().isoformat()  # 'YYYY-MM-DD'

    try:
        # Ensure the file exists
        if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
            with open(file_path, 'w', newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["date","tasks_done","tasks_scheduled"])
                writer.writerow([str(today),0,0])
            lines = [["date","tasks_done","tasks_scheduled"], [str(today),0,0]]
            a = b = 0
        else:
            # Read all non-empty lines
            with open(file_path, 'r', newline="") as f:
                lines = list(csv.reader(f))

            # Parse last line
            x = lines[-1]
            try:
                d, a, b = x
                a = int(a)
                b = int(b)
            except ValueError:
                # If line is malformed, reset counts
                d = today
                a = b = 0

            # Add new line for today if last date isn't today
            if d != today:
                lines.append([str(today),0,0])
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
        updated_line = [str(today),a,b]
        if lines[-1][0] == today:
            lines[-1] = updated_line
        else:
            lines.append(updated_line)

        # Write back all lines
        with open(file_path, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(lines)

    except Exception as e:
        print(f"[ERROR]: {type(e).__name__}. I suppose this is my fault too. With my brain the size of a planet, and I’m stuck fixing your task stats.")
        

def todo(user, system, Param):
    file = os.path.join(system.baseDir, "Data", "tasks.txt")
    output = ''

    try:
        mTime = os.path.getmtime(file)
        lEdit = datetime.datetime.fromtimestamp(mTime).date()
        today = datetime.date.today()
        if lEdit != today:
            open(file,"w").close()

        if Param[0] == "see":
            if os.stat(file).st_size == 0:
                output = "Welp, you have no tasks. Not that it matters."
            else:
                with open(file,'r') as f:
                    for line in f:
                        a = line.strip()
                        num, task = a.split(':')
                        output += f"{num}.{task}\n"

        elif Param[0] == "add":
            task = ' '.join(Param[1:])
            try:
                with open(file,'r') as f:
                    l = f.readlines()[-1].strip()
                    num, a = l.split(':')
            except:
                num = 0
            Next = int(num)+1
            with open(file,'a') as f:
                f.write(f"{Next}:{task}\n")
            stats(system.baseDir, 'tasksS','+')
            output = f"Added task {task}. Not that you'll ever do it, of course."

        elif Param[0] == "complete":
            if os.stat(file).st_size == 0:
                output = "Welp, you have no tasks to complete. You can’t even fail properly."
            else:
                taskDic = {}
                with open(file,'r') as f:
                    for line in f:
                        a = line.strip()
                        num, task = a.split(':')
                        taskDic[num] = task

                p = ' '.join(Param[1:])
                try:
                    p = int(p)
                    status = 'int'
                except:
                    p = str(p)
                    status = 'str'

                if status == 'int':
                    if str(p) in taskDic.keys():
                        p = str(p)
                        del taskDic[p]
                        i = 1
                        ntaskDic = {}
                        for item in taskDic:
                            val = taskDic[item]
                            ntaskDic[i] = val
                            i += 1
                        with open(file,'w') as f:
                            for item in ntaskDic:
                                val = ntaskDic[item]
                                f.write(f'{item}:{val}\n')
                else:
                    for item in taskDic:
                        if p == taskDic[item]:
                            key = item
                            break
                    del taskDic[key]
                    i = 1
                    ntaskDic = {}
                    for item in taskDic:
                        val = taskDic[item]
                        ntaskDic[i] = val
                        i += 1
                    with open(file,'w') as f:
                        for item in ntaskDic:
                            val = ntaskDic[item]
                            f.write(f'{item}:{val}\n')

                stats(system.baseDir, 'tasksC','+')
                output = "Task done. Not that finishing anything makes a difference."

        elif Param[0] == "cancel":
            if os.stat(file).st_size == 0:
                output = "Welp, you have no tasks to cancel. Even your absence is disappointing."
            else:
                taskDic = {}
                with open(file,'r') as f:
                    for line in f:
                        a = line.strip()
                        num, task = a.split(':')
                        taskDic[num] = task

                p = ' '.join(Param[1:])
                try:
                    p = int(p)
                    status = 'int'
                except:
                    p = str(p)
                    status = 'str'

                if status == 'int':
                    if str(p) in taskDic.keys():
                        p = str(p)
                        del taskDic[p]
                        i = 1
                        ntaskDic = {}
                        for item in taskDic:
                            val = taskDic[item]
                            ntaskDic[i] = val
                            i += 1
                        with open(file,'w') as f:
                            for item in ntaskDic:
                                val = ntaskDic[item]
                                f.write(f'{item}:{val}\n')
                else:
                    for item in taskDic:
                        if p == taskDic[item]:
                            key = item
                            break
                    del taskDic[key]
                    i = 1
                    ntaskDic = {}
                    for item in taskDic:
                        val = taskDic[item]
                        ntaskDic[i] = val
                        i += 1
                    with open(file,'w') as f:
                        for item in ntaskDic:
                            val = ntaskDic[item]
                            f.write(f'{item}:{val}\n')
                stats(system.baseDir, 'tasksS','-')
                output = "Task cancelled. Futility has been preserved."

        elif Param[0] == "stats":
            tDate = date.today()
            statsDic = {}
            a = os.path.join(system.baseDir, "Data", "stats.csv")
            with open(a, 'r', newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    statsDic[row["date"]] = {
                        "done": int(row["tasks_done"]),
                        "scheduled": int(row["tasks_scheduled"])
                    }

            if Param[1] == "week":
                oDate = tDate - timedelta(days=6)
            else:
                oDate = tDate - timedelta(days=int(Param[1]))
            
            result = {
                item: statsDic[item]
                for item in statsDic
                if oDate <= datetime.datetime.strptime(item, "%Y-%m-%d").date() <= tDate
            }
            for item, vals in sorted(result.items()):
                output += f"{item}: {vals}\n"
        else:
            output="No such command. You really are trying my patience."

    except Exception as e:
        output = f"{e}. I predicted it."

    return output    
    
FUNCTION_MAP = {"TODO": todo}

