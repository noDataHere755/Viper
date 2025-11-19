import importlib.util
import sys
from pathlib import Path
import os


def init(baseDir):
    plugins = {}
    path = Path(baseDir) / "Plugins"

    try:
        if not path.exists():
            return f"[ERROR]: Plugin directory not found at {path}"

        for file in path.glob("*.py"):
            try:
                spec = importlib.util.spec_from_file_location(file.stem, file)
                if spec is None or spec.loader is None:
                    return f"[ERROR]: Could not load plugin spec for {file}"

                module = importlib.util.module_from_spec(spec)

                try:
                    spec.loader.exec_module(module)
                except Exception as e:
                    return f"[ERROR]: Failed to execute plugin {file.stem}. Reason:{e}"

                if hasattr(module, "FUNCTION_MAP") and isinstance(module.FUNCTION_MAP, dict):
                    plugins.update(module.FUNCTION_MAP)
                else:
                    # Not fatal, but consistent with your format
                    pass

            except Exception as e:
                return f"[ERROR]: Plugin {file.stem} failed to load. Reason:{e}"

    except Exception as e:
        return f"[ERROR]: Reason:{e}, plus ur lunacy"

    return plugins




def do(Input, user, system):
    plugins = user.plugins
    try:
        if not isinstance(Input, list):
            return f"[ERROR]: Reason:Command input not a list, plus ur lunacy"

        if len(Input) == 0:
            return f"[ERROR]: Reason:Empty input, plus ur lunacy"

        if Input[0] not in plugins:
            return f"[ERROR]: Reason:Unknown command '{Input[0]}', plus ur lunacy"

        if len(Input) == 1:
            try:
                return plugins[Input[0]](user, system)
            except Exception as e:
                return f"[ERROR]: Reason:{e}, plus ur lunacy"

        elif len(Input) >= 2:
            Action, *Param = Input
            try:
                return plugins[Input[0]](user, system, Param)
            except Exception as e:
                return f"[ERROR]: Reason:{e}, plus ur lunacy"

        else:
            return f"[ERROR]"

    except Exception as e:
        return f"[ERROR]: Reason:{e}, plus ur lunacy"




def parse(Input, user, system):
    try:
        if not isinstance(Input, str):
            return f"[ERROR]: Parsing failed: expected string but got {type(Input)}, just like your life"

        Input = Input.split()
        Length = len(Input)

        if Length == 0:
            return f"[ERROR]: Parsing failed: empty input, just like your life"

        if Length == 1:
            return do(Input, user, system)

        elif Length >= 2:
            Action, *Param = Input
            return do(Input, user, system)

    except Exception as e:
        err = f"[ERROR]: Parsing or execution failed: {e}. This seems to be broken, just like your life"
        return err

