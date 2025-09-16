# Viper: A CLI for You

Viper is a command-line interface coded entirely in Python, made for you. Yes, just you.

It's in development right now (version 0.3), so expect an absolutely horrible user experience.
As of now, it does have account creation (for one person—*you*), password security,
and a plugin system you can use to plug in your homebrew commands into Viper.

## Table of Contents
- [Introduction](#introduction)
- [Installation and Dependencies](#installation-and-dependencies)
- [Commands List](#commands-list)
- [Code Plugins](#code-plugins)
- [To-Do List](#to-do-list)

## Introduction
Oh hell, let's just get on with it.

## Installation and Dependencies
Clone the repo and install:

```bash
git clone https://github.com/YOUR-USERNAME/viper.git
cd viper
pip install -e .
```

Dependencies:
- `bcrypt` (for password hashing)

Run with:

```cd Viper
python __main__.py

```

If you add an entry point later, you’ll be able to just type `viper`.

## Commands List
```
PRINT [thing]  → prints thing to console (thing is treated as a string)
WHOAMI         → displays your username
```

That’s all for now. But why wait for me when you can add your own neat stuff...

## Code Plugins
Plugins work like this:

1. Create a Python file.
2. Write whatever function(s) you want your command(s) to do.
3. At the very end of your code, include a `FUNCTION_MAP` dictionary:

```python
FUNCTION_MAP = {
    "CMD": Cmd
}
```

4. Put your code inside `Viper/Plugins` and start playing bug whac-a-mole.

Notes:
- When your command has no input, you must still import `user` and `system` objects.
- Useful attributes:
  - `user.userName` → username of user
  - `user.pluginsList` → list of installed plugins
  - `system.baseDir` → base directory path

## To-Do List
- Add more plugins for 'productivity' (alien word, I know) and utilities.
- Implement a `help` command to list available commands and plugins.
- Implement a `run` command to execute Python files directly from Viper.
- Possibly add file management commands: create, delete, move, and manipulate files.But meh, I'm just an overcaffeinated teenage racoon. 




