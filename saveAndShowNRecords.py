# save and show N records

import sys

FILENAME = "records.dat"

def saveRecord():
	count = int(input("Enter how many records you want to save: "))
	with open(FILENAME, "a") as file:
		for counter in range(count):
			userID = input("Enter userID: ")
			name = input("Enter name: ")
			value = int(input("Enter value: "))
			record = [userID, name, value]
			file.write(str(record) + "\n")

def showAllRecords():
	with open(FILENAME, "r") as fpRecords:
		records = fpRecords.readlines()
		for record in records:
			data = eval(record.strip())
			print("userID: ", data[0])
			print("Name: ", data[1])
			print("value: ", data[2])
			print("-" * 20)

def exit():
	print("Exiting program.")
	sys.exit()

def main():
	while True:
		print("1. Save Records")
		print("2. Show All Records")
		print("3. Exit")
		choice = int(input("Enter your choice: "))
		options = [saveRecord, showAllRecords, exit]
		options[choice - 1]()

if __name__ == "__main__":
	main()