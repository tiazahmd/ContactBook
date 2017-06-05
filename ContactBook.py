# ContactBook Version 1.0
# Feature: Login menu, add, remove and search contacts, capacity - 10 contacts
# Using lists.

# Declaring global variables
contactName = ['open', 'open', 'open', 'open', 'open', 'open', 'open', 'open', 'open', 'open']
contactNumber = ['open', 'open', 'open', 'open', 'open', 'open', 'open', 'open', 'open', 'open']
contactEmail = ['open', 'open', 'open', 'open', 'open', 'open', 'open', 'open', 'open', 'open']
conCount = 0
# End declaring global variables

# Declaring search function
def search(term):
    for numSearCount in range(0, conCount, 1):
        if term == contactName[numSearCount]:
            return numSearCount
        elif term == contactNumber[numSearCount]:
            return numSearCount
        elif term == contactEmail[numSearCount]:
            return numSearCount
    return -1
# End search function

# Login Module Start
print('ContactBook V1.0')
print('Login Menu')
import sys
userName = 'monty'
userPass = 'python'
userChance = 3
while (userChance > 0):
    userTypedName = input('Username: ')
    userTypedPass = input('Password: ')
    if (userTypedName == userName and userTypedPass == userPass):
        break
    else:
        userChance = userChance - 1
        if userChance == 0:
            print('Access denied. No attempts left. Program terminating.')
            sys.exit()
        else:
            print('Wrong username & password combo. ' + str(userChance) + ' attempts left')
print('Access Granted.')
# Login Module End

# Menu Module Begin
userChoice = 0
while (userChoice != '5'):
    print('Please select an option - type the # and press enter')
    print('1. Add a new contact.')
    print('2. Remove a contact.')
    print('3. Show all contacts.')
    print('4. Search a contact.')
    print('5. Exit')
    userChoice = input('Enter your choice: ')

    # User choice - add a new contact
    if userChoice == '1':
        contactAddAnother = 0
        while (contactAddAnother != 'n'):
            contactName[conCount] = input('Enter Contact Name: ')
            contactNumber[conCount] = input('Enter Contact Number: ')
            contactEmail[conCount] = input('Enter Contact Email: ')
            print('Contact Added.')
            conCount = conCount + 1
            contactAddAnother = input('Do you want to add another contact? (y/n) ')
    # End user choice - add a new contact

    # User choice - remove a contact
    if userChoice == '2':
        delAnother = 0
        delNumber = 0
        for numCount in range(0, conCount, 1):
            print(str(numCount+1) + '. ' + contactName[numCount] + ' - ' + contactNumber[numCount] + ' - ' + contactEmail[numCount])
        while delAnother != 'n':
            delNumber = int(input('Enter the # of contact you want to delete: '))
            del contactName[delNumber - 1]
            del contactNumber[delNumber - 1]
            del contactEmail[delNumber - 1]
            conCount = conCount - 1
            delAnother = input('Do you want to delete another contact? (y/n)')
        for numCount in range(0, conCount, 1):
            print(str(numCount+1) + '. ' + contactName[numCount] + ' - ' + contactNumber[numCount] + ' - ' + contactEmail[numCount])
    # End User choice - remove a contact

    # User choice - show all contacts
    if userChoice == '3':
        for numCount in range(0, conCount, 1):
            print(str(numCount+1) + '. ' + contactName[numCount] + ' - ' + contactNumber[numCount] + ' - ' + contactEmail[numCount])
    # End user choice - show all contacts

    # User choice - search contacts
    if userChoice == '4':
        searchTerm = 0
        searchTerm = input('Enter your search: ')
        if search(searchTerm) != -1:
            print('Contact Exists')
            print(contactName[search(searchTerm)] + ' - ' + contactNumber[search(searchTerm)] + ' - ' + contactEmail[search(searchTerm)])
        else:
            print('Contact does not exist.')
    # End user choice - search contacts

# Menu Module End
