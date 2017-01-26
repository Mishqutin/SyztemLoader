# SyztemLoader.

I don't really know how to describe what is it, so I will just write here the functions.

syz.bat:
Just helps programs start.

Nowy plik wsadowy Windows.bat (New batch file Windows.bat or something):
It should be deleted long time ago....

config.py:
Used to make changes in load.txt.

load.txt:
There is everything that Syztem need to orientate in directories. I could make this automatic but it is more fun.

syztem.py:
Module. Offers baisc functions like removing files etc. (Will offer that soon).
Also things like SCommands (explained later).

exec.py:
Main file. Brings program to life.
Things will work in this scope/environment or something like this. More info in code's comemnts.

ISC: 
I don't have idea to name it properly, but Internal Syztem Code sounds nice. There was no reason to name it 'Internal'.
ISC have got two data types: SVar and SCmd. Each stored in sz.SZdata dictionary.
The syntax is: { 'name': {'type', 'value'} }

Example:
sz.SZdata = { 'print': {'SCmd', 'print("abc")'},  'argExample': {'SCmd', 'print(args[0])'}, 'varibale': {'SVar', '123'} }

Code:

print

argExample 'Hello!'

variable

variable 128

variable

Result:

abc

Hello!

123

128


How it works:

SVar holds a string that could be later converted from string to other data type.

SCmd holds a string that is converted via ast.literal_eval() to function.

If SVar is called without arguments then it's value is printed.

If SVar is called with one argument then it's value is set to that. Other arguments are ignored.

If SCmd is called, the function assigned to it is executed. If function takes any arguments and you provide any then it is saved to

list args and like in 'argExample' you can use args[int].


To execute SCmds and SVars there are functions: sz.SCmd(); sz.SCmdv2(); sz.SVar()

In exec.py is an ISC class with do() function. There I described how it works.

Both SVar and SCmd can be executed in console that I will make later and by ISC.do(string) like it is done in exec.py.


Directories:

data/config/autorun:

exec.py executes every file by file in this dir. First '.py' by Python and then '.sz' by ISC. Used to configure functions on startup.
The file funcSetup.py defines SCmds and SVars.

data/backup:

There is no backup. Just couple of files that is no longer used.

data/local:

No desc

data/stools

There should be modules, libraries etc.

<<<<<<< HEAD
(It is a shorcut of 'Syztem Tools' :P )
=======
(It is a shorcut of 'Syztem Tools' :P )
>>>>>>> a8da99066959a0996dda3e4b91322b23fa8f07cd
