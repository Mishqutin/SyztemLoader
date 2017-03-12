import os
import ast
from msvcrt import getch
print("Checking load.txt ......")
f = open("load.txt", "r+")
read = f.read()
f.close()
print(read)
read = ast.literal_eval(read)
curDir = str(os.getenv("WorkingPath"))
if not read["complete"]:
	print("First start configuration needed...")
	read = '{"complete": True, "sDir": "' + curDir + '", "runDir": "' + curDir + '\data\local", "first": "A", "second": "B", "third": "C"}'
	os.system("del load.txt")
	f = open("load.txt", "w")
	f.write(read)
	f.close()
	os.system("mkdir {}\\documents\\Syztem\\prgs".format(os.getenv('userprofile')))
	exit()
lista = [read["first"], read["second"], read["third"]]
if lista[0]=="A":
	data1 = str(os.getenv("SyztemDataA"))
if lista[0]=="B":
	data1 = str(os.getenv("SyztemDataB"))
if lista[0]=="C":
	data1 = str(os.getenv("SyztemDataC"))
if lista[1]=="A":
	data2 = str(os.getenv("SyztemDataA"))
if lista[1]=="B":
	data2 = str(os.getenv("SyztemDataB"))
if lista[1]=="C":
	data2 = str(os.getenv("SyztemDataC"))
if lista[2]=="A":
	data3 = str(os.getenv("SyztemDataA"))
if lista[2]=="B":
	data3 = str(os.getenv("SyztemDataB"))
if lista[2]=="C":
	data3 = str(os.getenv("SyztemDataC"))
readWork = read
os.system("cls")
def main():
	print("Startup configuration |")
	print("Current directory: {}".format(curDir))
	print("-------------------------------------------------------------------------------")
	print("Syztem will start up with these options.")
	print("")
	print("--------Directories------------------------------------------------------------")
	print("Syztem main directory: {}".format(readWork["sDir"]))
	print("Loaded program running directory: {}".format(readWork["runDir"]))
	print("")
	print("--------Load priority----------------------------------------------------------")
	print("First:")
	print(readWork["first"] + " | " + data1)
	print("Second:")
	print(readWork["second"] + " | " + data2)
	print("Third:")
	print(readWork["third"] + " | " + data3)
	print("-------------------------------------------------------------------------------")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("_______________________________________________________________________________")
	print(" q - Exit without saving | w - Save | e - Edit options | Shift+R - Defaults")
	lol = getch()
	if lol == b"q":
		exit()
	elif lol == b"w":
		edit(10)
	elif lol == b"e":
		edit(1)
	elif lol == b"R":
		edit(11)
	else:
		main()
def edit(page):
	global read
	global readWork
	global data1
	global data2
	global data3
	global curDir
	os.system("cls")
	if page == 1:
		print("Startup configuration |")
		print("Current directory: {}".format(curDir))
		print("-------------------------------------------------------------------------------")
		print("Edit Syztem start up options.")
		print("")
		print("--------Select option----------------------------------------------------------")
		print("1 | Syztem main directory: {}".format(readWork["sDir"]))
		print("")
		print("2 | Loaded program running directory: {}".format(readWork["runDir"]))
		print("")
		print("3 | Edit load priority.")
		print("")
		print("")
		print("Select option number.")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("_______________________________________________________________________________")
		print(" q - Exit without saving | w - Save | e - Go back")
		lol = getch()
		if lol == b"q":
			exit()
		elif lol == b"w":
			edit(10)
		elif lol == b"e":
			main()
		elif lol == b"1":
			edit(4)
		elif lol == b"2":
			edit(3)
		elif lol == b"3":
			edit(2)
		else:
			edit(1)
	if page==2:
		print("Startup configuration |")
		print("Current directory: {}".format(curDir))
		print("-------------------------------------------------------------------------------")
		print("Edit Syztem programs load priority.")
		print("")
		print("--------Change load priority---------------------------------------------------")
		print("======")
		print(">>> First: " + readWork["first"] + " | " + data1 + " <<<")
		print("======")
		print("Second: " + readWork["second"] + " | " + data2)
		print("======")
		print("Third: " + readWork["third"] + " | " + data3)
		print("======")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("_______________________________________________________________________________")
		print(" 1-3 - Move selected | 0 - Skip selected")
		lol = getch()
		if lol == b"1" or lol == b"0":
			edit(21)
		elif lol == b"2":
			lel = readWork["first"]
			readWork["first"] = readWork["second"]
			readWork["second"] = lel
			lel = data1
			data1 = data2
			data2 = lel
			edit(21)
		elif lol == b"3":
			lel = readWork["first"]
			readWork["first"] = readWork["third"]
			readWork["third"] = lel
			lel = data1
			data1 = data3
			data3 = lel
			edit(21)
		else:
			edit(2)
	if page==21:
		print("Startup configuration |")
		print("Current directory: {}".format(curDir))
		print("-------------------------------------------------------------------------------")
		print("Edit Syztem programs load priority.")
		print("")
		print("--------Change load priority---------------------------------------------------")
		print("======")
		print("First: " + readWork["first"] + " | " + data1)
		print("======")
		print(">>> Second: " + readWork["second"] + " | " + data2 + " <<<")
		print("======")
		print("Third: " + readWork["third"] + " | " + data3)
		print("======")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("_______________________________________________________________________________")
		print(" 1-3 - Move selected | 0 - Skip selected")
		lol = getch()
		if lol == b"2" or lol == b"0":
			edit(22)
		elif lol == b"1":
			lel = readWork["first"]
			readWork["first"] = readWork["second"]
			readWork["second"] = lel
			lel = data1
			data1 = data2
			data2 = lel
			edit(22)
		elif lol == b"3":
			lel = readWork["second"]
			readWork["second"] = readWork["third"]
			readWork["third"] = lel
			lel = data2
			data2 = data3
			data3 = lel
			edit(22)
		else:
			edit(21)
	if page==22:
		print("Startup configuration |")
		print("Current directory: {}".format(curDir))
		print("-------------------------------------------------------------------------------")
		print("Edit Syztem programs load priority.")
		print("")
		print("--------Change load priority---------------------------------------------------")
		print("======")
		print("First: " + readWork["first"] + " | " + data1)
		print("======")
		print("Second: " + readWork["second"] + " | " + data2)
		print("======")
		print(">>> Third: " + readWork["third"] + " | " + data3 + " <<<")
		print("======")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("_______________________________________________________________________________")
		print(" 1-3 - Move selected | 0 - Skip selected")
		lol = getch()
		if lol == b"3" or lol == b"0":
			edit(1)
		elif lol == b"2":
			lel = readWork["third"]
			readWork["third"] = readWork["second"]
			readWork["second"] = lel
			lel = data3
			data3 = data2
			data2 = lel
			edit(1)
		elif lol == b"1":
			lel = readWork["first"]
			readWork["first"] = readWork["third"]
			readWork["third"] = lel
			lel = data1
			data1 = data3
			data3 = lel
			edit(1)
		else:
			edit(22)
	if page == 4:
		print("Startup configuration |")
		print("Current directory: {}".format(curDir))
		print("-------------------------------------------------------------------------------")
		print("Syztem main directory (where is syz.bat).")
		print("")
		print("--------Select option----------------------------------------------------------")
		print("Syztem main directory: {}".format(readWork["sDir"]))
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("Type in new value.")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("_______________________________________________________________________________")
		lol = str(input(">>> "))
		readWork["sDir"] = lol
		edit(1)
	if page == 3:
		print("Startup configuration |")
		print("Current directory: {}".format(curDir))
		print("-------------------------------------------------------------------------------")
		print("Syztem running directory (where Syztem will store data).")
		print("")
		print("--------Select option----------------------------------------------------------")
		print("Syztem running directory: {}".format(readWork["runDir"]))
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("Type in new value.")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
		print("_______________________________________________________________________________")
		lol = str(input(">>> "))
		readWork["runDir"] = lol
		edit(1)
	if page==10:
		read = readWork
	if page==11:
		readWork = {"complete": True, "sDir": curDir, "runDir": curDir + "\data\local", "first": "A", "second": "B", "third": "C"}
		os.system("mkdir {}\\documents\\Syztem\\prgs".format(os.getenv('userprofile')))
		main()


main()
os.system("del load.txt")
f = open("load.txt", "w")
f.write(str(read))