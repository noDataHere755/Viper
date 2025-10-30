import importlib.util
import sys
from pathlib import Path
import os
def Print(user,system,Param):
    x=''
    for i in Param:
        x+=i
        x+=' '
    return x
def Whoami(user,system):
    return f"You're {user.userName}, unc. Seems like your username is just like your new year's resolution."
FUNCTION_MAP={'PRINT':Print,'WHOAMI':Whoami}

def pluginCall(Input,user,system,Length):
    
    pfiles=user.pluginsList
    
    loaded_mods=[]
    
    uPlugDir=Path(system.baseDir)/"Plugins"
    for path_str in pfiles:
        path=uPlugDir/path_str
        if path.exists():
            try:
                module_name=path.stem
                spec=importlib.util.spec_from_file_location(module_name,str(path))
                module=importlib.util.module_from_spec(spec)
                sys.modules[module_name]=module
                spec.loader.exec_module(module)
                loaded_mods.append(module)
            except Exception as e:
                return f"[ERROR]:Plugin {module_name} failed to load. Reason:{e}, and your idiocy"
        else:
            return f"[ERROR]:Failed to load plugin {path}"
    for module in loaded_mods:
        try:
            if hasattr(module,"FUNCTION_MAP") and isinstance(module.FUNCTION_MAP,dict):
                if Length==1 and Input[0] in module.FUNCTION_MAP:
                    return module.FUNCTION_MAP[Input[0]](user,system)
                elif Length>=2 and Input[0] in module.FUNCTION_MAP:
                    Action,*Param=Input
                    return module.FUNCTION_MAP[Input[0]](user,system,Param)
                else:
                    continue
        
    
        except Exception as e:
            return f"[ERROR]:Plugin {module_name} failed to execute command {Input[0]}. Reason:{e}, plus ur lunacy"
    return f"[ERROR]: No command called {Input[0]}, just like you have no command called 'USE commonsense'"
def parse(Input, user, system):
    try:
        Input = Input.split()
        Length = len(Input)
        if Length == 1:
            if Input[0] in FUNCTION_MAP:
                
                return FUNCTION_MAP[Input[0]](user, system)
            else:
                return pluginCall(Input,user,system,Length)

        elif Length >= 2:
            Action, *Param = Input
            if Action in FUNCTION_MAP:
                
                return FUNCTION_MAP[Input[0]](user,system,Param)
            else:
                return pluginCall(Input,user,system,Length)
    except Exception as e:
        err = f"[ERROR]: Parsing or execution failed: {e}. This seems to be broken, just like your life"
        return err
