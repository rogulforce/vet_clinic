import random
from dataclasses import dataclass
import numpy as np
import pandas as pd
import typing
from datetime import datetime, timedelta
from generate import breeds


@dataclass
class Fulfillment:
    cursor: 'typing.Any'

    def employees(self, name, surname, sex, phone, position, salary):
        qr = 'INSERT INTO vet_clinic.employees (name, surname, sex, phone, position, salary) VALUES (?, ?, ?, ?, ?, ?)'
        self.cursor.execute(qr, (name, surname, sex, phone, position, salary))

    def rooms(self, number, name):
        self.cursor.execute('INSERT INTO vet_clinic.rooms (number, name) VALUES (?, ?)', (number, name))

    def equipment(self, eqName, status, room_number, quantity):
        qr = 'INSERT INTO vet_clinic.equipment (eqName, status, room_number, quantity) VALUES (?, ?, ?, ?)'
        self.cursor.execute(qr, (eqName, status, room_number, quantity))

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

    def meds(self, name, in_stock, ordered, discontinued, price):
        qr = 'INSERT INTO vet_clinic.meds (name, in_stock, ordered, discontinued, price) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(qr, (name, in_stock, ordered, discontinued, price))

    def meds_prescribed(self, drugID, visitID, amount):
        qr = '''INSERT INTO vet_clinic.meds_prescribed (drugID, visitID, amount) VALUES (?, ?, ?)'''
        self.cursor.execute(qr, (drugID, visitID, amount))

    def cash_flow(self, date, amount, atype):
        qr = 'INSERT INTO vet_clinic.cash_flow(date, amount, type) VALUES(?, ?, ?)'
        self.cursor.execute(qr, (date, amount, atype))


def fill(cursor):
    # zmienić później na rand values
    vets_number = 3
    owners_number = 200
    people = pd.read_csv(r'../data/users_randomized.csv').sample(1000)
    meds = pd.read_csv(r'../data/drugs.csv')
    vet = Fulfillment(cursor)
    start_date = datetime(2020, 1, 1)
    end_date = datetime.today() - timedelta(days=1)

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
        vet.employees(people.iloc[3, 0], people.iloc[3, 1], people.iloc[3, 3], str(people.iloc[3, 2]),
                      'Konserwator Powierzchni Płaskich', int(np.random.randint(2600, 3220)))

        # weterynarze int(np.random.randint(3670, 5360)))
        for i in range(vets_number):
            vet.employees(people.iloc[i + 4, 0], people.iloc[i + 4, 1], people.iloc[i + 4, 3],
                          str(people.iloc[i + 4, 2]), 'Weterynarz', int(np.random.randint(3670, 5360)))

    def room_fill():
        rooms = {1: 'recepcja', 2: 'gabinet 1', 3: 'gabinet 2', 4: 'socjal', 5: 'zaplecze', 6: 'gabinet zabiegowy'}
        for key, val in rooms.items():
            vet.rooms(key + 100, val)

    def equipment_fill():
        names = pd.read_excel('../generate/meds.xlsx', names=['name'])['name']
        for name in names.values:
            vet.equipment(str(name), True, random.randint(2, 3) + 100, random.randint(0, 5))

    def meds_fill():
        for name in meds.values:
            in_stock = np.random.randint(0, 10)
            ordered = np.random.randint(0, 5)
            discontinued = 0
            if in_stock + ordered == 0:
                discontinued = 1
            price = np.random.randint(5, 161)
            vet.meds(str(name[0]), in_stock, ordered, discontinued, price)

    def owners_and_pets_fill():
        all_pets = 0

        number_of_pets = {1: 0.7, 2: 0.15, 3: 0.075, 4: 0.05, 5: 0.025}
        number_of_pets_cum = np.array(list(number_of_pets.values())).cumsum()
        pet_probs = {'dog': 0.4, 'cat': 0.385, 'hamster': 0.075, 'rabbit': 0.06, 'rat': 0.025,
                     'guinea_pig': 0.005, 'chinchilla': 0.01, 'turtle': 0.01, 'canary': 0.01,
                     'budgerigar': 0.01, 'iguana': 0.01}
        pet_attributes = {'dog': breeds.dogs, 'cat': breeds.cats, 'hamster': breeds.hamsters,
                          'rabbit': breeds.rabbits, 'rat': breeds.rats,
                          'guinea_pig': breeds.guinea_pigs, 'chinchilla': breeds.chinchillas, 'turtle': breeds.turtles,
                          'canary': breeds.canaries, 'budgerigar': breeds.budgerigars, 'iguana': breeds.iguanas}
        pet_probs_cum = np.array(list(pet_probs.values())).cumsum()
        pet_types = list(pet_probs.keys())

        # generating owners
        for i in range(owners_number):  # owners_number
            name = people.iloc[-(i + 1), 0]
            surname = people.iloc[-(i + 1), 1]
            phone = str(people.iloc[-(i + 1), 2])
            mail = f'{name}.{surname}@mail.com'
            # adding owner to db
            vet.owners(name, surname, phone, mail)
            owner_pets = np.sum(number_of_pets_cum <= random.random()) + 1
            # generating pets for owners
            for pet in range(owner_pets):
                # 0 - male, 1 - female
                if random.random() < 0.5:
                    sex = 'Male'
                else:
                    sex = 'Female'
                #
                pet_type = pet_types[np.sum(pet_probs_cum <= random.random())]
                height, weight, birth_date = pet_attributes[pet_type]()
                vet.pets(i + 1, sex, pet_type, birth_date, weight, height)
                all_pets += 1

        return all_pets

    def visits_fill(num_of_pets):
        # dziennie n wizyt
        # dla każdej wizyty losujemy zwierzaka
        # dodajemy wizyte, koszt, przepisane leki, weterynarza

        visitID = 0
        cursor.execute('select salary from employees')
        salaries = [float(res[0]) for res in cursor]

        pet_to_vet = {}
        # przypisanie lekarza prowadzacego
        for pet in range(1, num_of_pets + 1):
            pet_to_vet[pet] = random.randint(5, 7)

        for i in range(abs((end_date - start_date).days)):
            day = start_date + timedelta(days=i)
            # addnig salaries to db
            if day.day == 1:
                if (day.month != start_date.month) or (day.year != start_date.year):
                    for salary in salaries:
                        vet.cash_flow(day, -salary, 'wyplata')
            if day.weekday() not in [5, 6]: # poza sobotą i niedzielą
                n = random.randint(16, 24)
                for j in range(n):
                    visitID += 1
                    petID = random.randint(1, num_of_pets)
                    employeeID = pet_to_vet[petID]
                    registation_day = day - timedelta(days=random.randint(7, 14))
                    # nie odbyla się
                    planned_date = day + timedelta(hours=9, minutes=j * 30)
                    if random.random() < 0.05:
                        status = False
                        real_date = None
                        cost = 50
                    else:
                        status = True
                        real_date = planned_date
                        cost = random.randint(50, 200)
                        if random.random() < 0.1:
                            cost += random.randint(200, 500)

                    vet.visits(petID=petID, employeeID=employeeID, registration_date=registation_day,
                               planned_date=planned_date, real_date=real_date, status=status, cost=cost,
                               number=random.randint(102, 103))

                    # wylosować lek i ilość
                    med_prescribed = meds.sample(random.randint(0, 3))
                    for k in range(med_prescribed.shape[0]):
                        drugID = med_prescribed.index[k] + 1
                        qty = random.randint(1, 3)
                        vet.meds_prescribed(drugID=int(drugID), visitID=visitID, amount=qty)

    employee_fill()
    room_fill()
    equipment_fill()
    meds_fill()
    num_of_pets = owners_and_pets_fill()
    visits_fill(num_of_pets)
