# CRUD for bank domain

import os
import sys

FILENAME = "bankAccounts.dat"

class Customer():
	def __init__(self, accountNumber, name, balance, status = True):
		self.accountNumber = accountNumber
		self.name = name
		self.balance = balance
		self.status = status

def loadAccounts():
	accounts = []
	with open(FILENAME, "r") as fpAccounts:
		for account in fpAccounts:
			data = eval(account.strip())
			customer = Customer(data[0], data[1], data[2], data[3])
			accounts.append(customer)
	return accounts

def saveAccounts(accounts):
	with open(FILENAME, "w") as fpAccounts:
		for account in accounts:
			fpAccounts.write(str([account.accountNumber, account.name, account.balance, account.status]) + "\n")

def findCustomer():
	accountNumber = input("Enter account number: ")
	accounts = loadAccounts()
	for customer in accounts:
		if customer.accountNumber == accountNumber:
			return customer, accounts
	return None, accounts


def createAccount():
	accountNumber = input("Enter Account Number: ")
	name = input("Enter Customer Name: ")
	balance = int(input("Enter Balance: "))
	customer = Customer(accountNumber, name, balance)
	accounts = loadAccounts()
	accounts.append(customer)
	saveAccounts(accounts)

def showAllAccounts():
	accounts = loadAccounts()
	for account in accounts:
		print("Account Number: ", account.accountNumber)
		print("Name: ", account.name)
		print("Balance: ", account.balance)
		print(f"Status: {'Active' if account.status else 'Inactive'}\n")
		print("-" * 20)

def updateAccount():
    customer, accounts = findCustomer()
    if customer:
        customer.name = input("Enter new name of the customer: ")
        saveAccounts(accounts)
        return 1
    return 0

def deleteAccount():
    customer, accounts = findCustomer()
    if customer:
        choice = input("Do you really want to delete the account: ")
        if choice.lower() == 'y':
            customer.status = False
            saveAccounts(accounts)
            return 1
    return 0

def exit():
    print("Exiting program\n")
    sys.exit()

def main():
    while True:
        print("1. Open an Account")
        print("2. Show All accounts")
        print("3. Update Account")
        print("4. Delete Account")
        print("5. Exit")
        choice = int(input("Enter your option: "))

        options = [createAccount, showAllAccounts, updateAccount, deleteAccount, exit]
        options[choice - 1]()

if __name__ == "__main__":
	main()
