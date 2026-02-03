# read and show one record

import sys

FILENAME = "records.dat"

def saveRecord():
	userID = input("Enter userID: ")
	name = input("Enter name: ")
	value = int(input("Enter value: "))
	record = [userID, name, value]
	with open(FILENAME, "a") as file:
		file.write(str(record) + "\n")

def showRecord():
	with open(FILENAME, "r") as records:
		record = records.readline().strip()
		records = eval(record)
		print("userID: ", records[0])
		print("Name: ", records[1])
		print("value: ", records[2])

def exit():
	print("Exiting program.\n")
	sys.exit()

def main():
	while True:
		print("1. Save a record")
		print("2. Show record")
		print("3. Exit")
		choice = int(input("Enter your choice: "))
		options = [saveRecord, showRecord, exit]
		options[choice - 1]()

if __name__ == "__main__":
    main()