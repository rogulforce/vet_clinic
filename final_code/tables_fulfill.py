from dataclasses import dataclass
import numpy as np
import mariadb
import sys


@dataclass
class Fulfillment:
    vets_number: int = 3
    rooms_number: int = 5
    visits_number: int = 20

    def employees(self, name, surname, sex, phone, position, salary):
        qr = 'INSERT INTO vet_clinic.employees (name, surname, sex, phone, position, salary) VALUES (?, ?, ?, ?, ?, ?)'
        self.cursor.execute(qr, (name, surname, sex, phone, position, salary))

    def rooms(self, number, name):
        self.cursor.execute('INSERT INTO vet_clinic.rooms (number, name) VALUES (?, ?)', (number, name))

    def equipment(self, eqName, status, room_number, number):
        qr = 'INSERT INTO vet_clinic.equipment (eqName, status, room_number, number) VALUES (?, ?, ?, ?)'
        self.cursor.execute(qr, (eqName, status, room_number, number))

    def visits(self, petID, employeeID, registration_date, planned_date, real_date, status, cost, number):
        qr = '''INSERT INTO vet_clinic.visits
        (petID, employeeID, registration_date, planned_date, real_date, status, cost, number) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        self.cursor.execute(qr, (petID, employeeID, registration_date, planned_date, real_date, status, cost, number))

    def pets(self, ownerID, sex, atype, birthdate, weight, height):
        qr = 'INSERT INTO vet_clinic.pets (ownerID, sex, type, birthdate, weight, height) VALUES (?, ?, ?, ?, ?, ?)'
        self.cursor.execute(qr, (ownerID, sex, atype, birthdate, weight, height))

    def owners(self, name, surname, phone, mail):
        qr = 'INSERT INTO vet_clinic.owners (name, surname, phone, mail) VALUES (?, ?, ?, ?)'
        self.cursor.execute(qr, (name, surname, phone, mail))


def fill(cursor):
    # zmienić później na rand values
    vets_number = 3
    rooms_number = vets_number + 2
    visits_number = 20
    people = pd.read_csv(r'../data/users_randomized.csv').sample(1000)
    vet = Fulfillment(cursor)

    def employee_fill():
        # Recepcjonista
        vet.employees(people.iloc[0, 0], people.iloc[0, 1], people.iloc[0, 3], str(people.iloc[0, 2]), 'Recepcjonista',
                      int(np.random.randint(3080, 4240)))
        # Księgowa/y int(np.random.randint(5361, 10000))
        vet.employees(people.iloc[1, 0], people.iloc[1, 1], people.iloc[1, 3], str(people.iloc[1, 2]), 'Księgowy',
                      int(np.random.randint(3920, 5990)))
        # Szef/owa int(np.random.randint(3920, 5990))
        vet.employees(people.iloc[2, 0], people.iloc[2, 1], people.iloc[2, 3], str(people.iloc[2, 2]), 'Szef',
                      int(np.random.randint(5361, 10000)))
        # Sprzątaczka na B2B
        vet.employees(people.iloc[3, 0], people.iloc[3, 1], people.iloc[3, 3], str(people.iloc[3, 2]), 'Konserwator Powierzchni Płaskich',
                      int(np.random.randint(2600, 3220)))

        # weterynarze int(np.random.randint(3670, 5360)))
        for i in range(vets_number):
            vet.employees(people.iloc[i+4, 0], people.iloc[i+4, 1], people.iloc[i+4, 3], str(people.iloc[i+4, 2]), 'Weterynarz', int(np.random.randint(3670, 5360)))

    def room_fill():
        rooms = {1: 'recepcja', 2: 'gabinet 1', 3: 'gabinet 2', 4: 'socjal', 5: 'zaplecze'}
        for key, val in rooms.items():
            vet.rooms(key+100, val)

    def equipment_fill():
        pass

    def meds_fill():
        pass

    def visits_fill():
        # tutaj przy okazji meds described?
        pass

    def owners_fill():
        # tutaj owner?
        pass

    def pets_fill():
        # tutaj owner?
        pass

    employee_fill()
    room_fill()
    equipment_fill()
    meds_fill()
    visits_fill()
    owners_fill()
    pets_fill()