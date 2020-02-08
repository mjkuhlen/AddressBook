from Contacts import Contacts
from person import Person

def menu():
    running = True
    while running:
        print('-- OPTIONS --')
        print('1: Add New Contact')
        print('2: Update Contact')
        print('3: Delete Contact')
        print('4: Print all Contacts')
        print('5: Search Contacts')
        print('6: Find Birthdays by Month')
        print('7: Quit')
        select = input("Make a Selection: ")
        if select == '7':
            running = False
            break
        elif select == '6':
            test.find_birthday_month()
        elif select == '5':
            test.find_person()
        elif select == '4':
            test.print_contacts()
        elif select == '3':
            test.remove_person()
        elif select == '2':
            test.update_person()
        elif select == '1':
            test.add_person()
        else:
            print('Invalid Response Choose Again')


test = Contacts()
test.populate()
menu()