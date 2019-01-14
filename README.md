# pyconsole_util
The python console utility is a basic set of functions that print to the console in different formats for debugging, exploring, or printing nicely.

You can see some samples below and in the source code itself

![alt text](https://i.imgur.com/8F4wQcm.png "Overview of all Functions in the Code")

## util.startup(\*args)
\*args can be anything normally able to be printed with print()

When you are initializing variables, uploading to documents, setting up pins on a board, etc- use this to print out that those things are initializing.

Sends in yellow

## util.title(\*args)
\*args can be anything normally able to be printed with print()

Whenever a new block of your code begins, use this block of code to display that.

Sends in white text with a green background

## util.endline(\*args)
\*args can be anything normally able to be printed with print()

Whenever a block of code ends, use this to signal that

## util.debug(\*args, title=None)
\*args can be anything normally able to be printed with print()
title is an optional parameter that appears to the left of the location

Displays the absolute path to the file and the line number the function was called on, underlined. The other arguments will be printed out. All in red.

## util.info(\*arg)
\*arg can be any object

Prints out all of the members of an object in teal, organizes dictionaries and arrays for print.
