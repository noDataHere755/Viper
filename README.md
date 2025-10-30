# Viper: A CLI for the average Joe

Viper is a command-line interface coded entirely in Python, made for people. Not for developers, so if you were expecting |s and greps, just click away.

It's in development right now (version 0.3 or something? I forget), so expect an absolutely horrible user experience.
As of now, it does have account creation (for one person—*you*), password security,
and a plugin system you can use to plug in your homebrew commands into Viper.

## Table of Contents

* [Introduction](#introduction)
* [Installation and Dependencies](#installation-and-dependencies)
* [Commands List](#commands-list)
* [Code Plugins](#code-plugins)
* [To-Do List](#to-do-list)

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

* `bcrypt` (for password hashing)

Run with:

```cd Viper
python __main__.py

```

If you add an entry point later, you’ll be able to just type `viper`.

## Commands List

```
PRINT thing  → prints thing to console (thing is treated as a string)
WHOAMI         → displays your username
TODO see       → shows your to-do list
TODO add task  → adds a task
TODO complete task → checks off a task for you, you can specify either index (1,2...) or task name
TODO cancel task → cancels the task specified, specification is just like complete
TODO stats period→ prints out your awesome(read: absolutely trash) productivity data with period being either a number or 'week'
```

BTW, the TODO plugin fills up a neat little stats.csv in Viper/Data/stats.csv with the columns:

```
date,tasks_done,tasks_scheduled
```

Y'know, just in case you wanna keep your glorious record of procrastination for future you to spit on

That’s all for now. But why wait for me when you can add your own neat stuff...

## Code Plugins

Plugins work like this:

1. Create a Python file.
2. Write whatever function(s) you want your command(s) to do.
3. At the very end of your code, include a `FUNCTION\_MAP` dictionary:

```python
FUNCTION\_MAP = {
    "CMD": Cmd
}
```

4. Put your code inside `Viper/Plugins` and start playing bug whac-a-mole.

Notes:

* When your command has no input, you must still import `user` and `system` objects.
* Useful attributes:

  * `user.userName` → username of user
  * `user.pluginsList` → list of installed plugins
  * `system.baseDir` → base directory path

## Advanced Plugin Magic:

*IMPORTANT*: Never, ever, ever have your plugin print directly to console. Yes, it works, but why do it when you can return? And if you still want more 'control'...

1. Make your plugin spew out a list instead of a string.
2. And you get all the stuff in your list, printed on consecutive lines.
   Aaand if one of these strings happens to be in your list:

```
[STATIC]    → Stops the cursor on the line its on
[NEWLINE]   → Sends the cursor onto a new line. Helpful for stopping a [STATIC]
[WAIT]x     → Waits for x seconds, then continues
[AUDIO]path → Plays an audio file at the path specified. It plays side-by-side and doesn't stop the rest of the list from executing
```
So yes, you're one for loop away from total control.


## To-Do List
- A FOCUS plugin that starts a pomodoro timer while you pretend to work
- A HELP command
- Maybe even a CALC and file system for this.





