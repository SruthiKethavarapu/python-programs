# print given name given number of times

import sys

def printName(name, count):
	for counter in range(count):
		print(name)

argCount = len(sys.argv) - 1
if argCount == 1:
	if sys.argv[1].isdigit():
		print("Error: Name expected, not a number")
		sys.exit()
	name = sys.argv[1]
	printName(name = name, count = 1)
	sys.exit()
elif argCount == 2:
	if sys.argv[1].isdigit():
		count = int(sys.argv[1])
		name = sys.argv[2]
	else:
		name = sys.argv[1]
		count = int(sys.argv[2])

# if(len(sys.argv)) != 3:
# 	sys.exit()
# name = sys.argv[1]
# count = int(sys.argv[2])
printName(name = name, count = count)