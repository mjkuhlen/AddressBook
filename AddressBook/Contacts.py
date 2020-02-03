from person import Person
import csv

class Contacts(object):
    def __init__(self):
        self.people = {}
        self.total_contacts = 0

    def populate(self):
        with open('MOCK_DATA.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                new_person = Person(row["first_name"], row["last_name"], row["street"], row["city"], row["state"], row["zipcode"], row["day"], row["month"], row["year"])
                line_count += 1
                self.total_contacts += 1
                self.people[self.total_contacts] = new_person

    def add_person(self):
        fname = input("Enter First Name: ")
        lname = input("Enter Last Name: ")
        street = input("Enter Street Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zipcode = input("Enter Zip Code: ")
        day = input("Enter Birth Day: ")
        month = input("Enter Birth Month: ")
        year = input("Enter Birth Year: ")
        new_person = Person(fname,lname,street,city,state,zipcode,day,month,year)
        self.total_contacts += 1
        self.people[self.total_contacts] = new_person

    def remove_person(self):
        lname = input("Search by Last Name: ")
        found = False
        for contact in self.people:
            if self.people[contact].last_name == lname:
                found = True
                searched_person = contact
                break
        if found == True:
            self.people.pop(searched_person)
        else:
            print(f"{lname} NOT FOUND")

    def update_person(self):
        lname = input("Search by Last Name: ")
        found = False
        for contact in self.people:
            if self.people[contact].last_name == lname:
                found = True
                searched_person = self.people[contact]
                break
        if found:
            updating = True
            while updating:
                print('--UPDATE CONTACT--')
                print(f"1 First Name: {searched_person.first_name}")
                print(f"2 Last Name: {searched_person.last_name}")
                print(f"3 Street Address: {searched_person.street_address}")
                print(f"4 City: {searched_person.city_address}")
                print(f"5 State: {searched_person.state_address}")
                print(f"6 Zip Code: {searched_person.zip_address}")
                print(f"7 Birth Day: {searched_person.birth_day}")
                print(f"8 Birth Month: {searched_person.birth_month}")
                print(f"9 Birth Year: {searched_person.birth_year}")
                print(f"10 Done Updating")
                selection = input("Choose a field to Update: ")
                if selection == '1':
                    update = input("Update First Name: ")
                    searched_person.first_name = update
                elif selection == '2':
                    update = input("Update Last Name: ")
                    searched_person.last_name = update
                elif selection == '3':
                    update = input("Update Street Address: ")
                    searched_person.street_address = update
                elif selection == '4':
                    update = input("Update City Address: ")
                    searched_person.city_address = update
                elif selection == '5':
                    update = input("Update State: ")
                    searched_person.state_address = update
                elif selection == '6':
                    update = input("Update Zip Code: ")
                    searched_person.zip_address = update
                elif selection == '7':
                    update = input("Update Birth Day: ")
                    searched_person.birth_day = update
                elif selection == '8':
                    update = input("Update Birth Month: ")
                    searched_person.birth_month = update
                elif selection == '9':
                    update = input("Update Birth Year: ")
                    searched_person.birth_year = update
                elif selection == '10':
                    updating = False
                    break



    def find_person(self):
        lname = input("Search by Last Name: ")
        found = False
        for contact in self.people:
            if self.people[contact].last_name == lname:
                found = True
                searched_person = self.people[contact]
                break
        if found == True:
            print(f"NAME - {searched_person.first_name} {searched_person.last_name}")
            print(f"ADDRESS - {searched_person.street_address} {searched_person.city_address}, {searched_person.state_address} {searched_person.zip_address}")
        else:
            print(f"{lname} NOT FOUND")

    def find_birthday_month(self):
        month = input("Search Birthdays by Month: ")
        found = False
        results = {}
        results_count = 0
        for contact in self.people:
            if self.people[contact].birth_month == month:
                found = True
                results_count += 1
                results[results_count] = self.people[contact]
        if found:
            for contact in results:
                print(f"NAME - {results[contact].first_name} {results[contact].last_name}")
                print(f"ADDRESS - {results[contact].street_address} {results[contact].city_address}, {results[contact].state_address} {results[contact].zip_address}")
                print(f"BIRTHDAY - {results[contact].birth_month} / {results[contact].birth_day} / {results[contact].birth_year}")
        else:
            print('No Birthdays in that Month')

    def print_contacts(self):
        for contact in self.people:
            print(f"NAME - {self.people[contact].first_name} {self.people[contact].last_name}")
            print(f"ADDRESS - {self.people[contact].street_address} {self.people[contact].city_address}, {self.people[contact].state_address} {self.people[contact].zip_address}")

