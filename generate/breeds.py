import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import random as r
import datetime


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = r.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def dogs_regression():
    # tabela z rasami psów, ich wysokością i masą
    df = pd.read_excel('dogs.xlsx')

    # kolumny z górną i dolną granicą wysokości dla ras
    h_low = df['height_low_m']
    h_high = df['height_high_m']

    # średnia wysokość dla każdej z ras
    h_mean = (h_low + h_high)/2

    # kolumny z górną i dolną granicą masy dla ras
    w_low = df['weight_low_kg']
    w_high = df['weight_high_kg']

    # numpaje do regresji (tak, można to zrobić krok wcześniej)
    y_low = np.array(w_low)
    y_high = np.array(w_high)
    x_mean = np.array(h_mean).reshape((-1, 1))

    # regresja dla dolnych i górnych przedziałów
    # (czyli pseudomatematyka xd)
    mean_low = LinearRegression().fit(x_mean, y_low)
    mean_high = LinearRegression().fit(x_mean, y_high)

    return [mean_low.intercept_, mean_low.coef_[0], mean_high.intercept_, mean_low.coef_[0], min(h_low), max(h_high)]


def dogs(b):
    # zmienna objaśniająca to wysokość psa, więc losujemy jakąś
    gen_height = r.uniform(b[4], b[5])

    # przewidywalna masa psa o zadanej wysokości
    lower_predict = b[0] + b[1] * gen_height
    higher_predict = b[2] + b[3] * gen_height

    # i losujemy masę z tego przedziału
    gen_weight = r.uniform(lower_predict, higher_predict)

    # zostaje data urodzenia
    age = r.randint(1, 20)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'dog', gen_height, gen_weight, birthdate


def cats():
    weight = r.uniform(2.5, 7)
    height = r.uniform(0.15, 0.30)

    age = r.randint(1, 18)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'cat', height, weight, birthdate


def hamsters():
    weight = r.uniform(0.03, 0.1)
    height = r.uniform(0.02, 0.03)

    age = r.randint(1, 3)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'hamster', height, weight, birthdate


def rabbits():
    weight = r.uniform(0.1, 2.5)
    height = r.uniform(0.12, 0.25)

    age = r.randint(1, 12)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'rabbit', height, weight, birthdate


def rats():
    weight = r.uniform(0.25, 0.7)
    height = r.uniform(0.06, 0.09)

    age = r.randint(1, 3)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'rat', height, weight, birthdate

def guinea_pigs():
    weight = r.uniform(0.7, 1.2)
    height = r.uniform(0.085, 0.105)

    age = r.randint(1, 7)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'guinea_pig', height, weight, birthdate

def chinchillas():
    weight = r.uniform(0.8, 1.1)
    height = r.uniform(0.105, 0.175)

    age = r.randint(1, 20)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'chinchilla', height, weight, birthdate

def turtles():
    weight = r.uniform(0.5, 2)
    height = r.uniform(0.05, 0.1)

    age = r.randint(1, 80)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'turtle', height, weight, birthdate

def canaries():
    weight = r.uniform(0.0084, 0.023)
    height = r.uniform(0.1, 0.12)

    age = r.randint(1, 15)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'canary', height, weight, birthdate

# papużki faliste xd
def budgerigars():
    weight = r.uniform(0.03, 0.04)
    height = r.uniform(0.17, 0.19)

    age = r.randint(1, 8)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'canary', height, weight, birthdate

def iguanas():
    weight = r.uniform(0.03, 0.04)
    height = r.uniform(0.13, 0.15)

    age = r.randint(1, 8)
    now = datetime.datetime.now()
    end = datetime.date(now.year, now.month, now.day)
    start = datetime.date(end.year - age, end.month, end.day)

    birthdate = random_date(start, end)
    birthdate.strftime('%Y-%m-%d')

    return 'canary', height, weight, birthdate


if __name__ == "__main__":
    # kilka przykładowych rezultatów
    a = dogs_regression()
    doggo_size = dogs(a)
    print(doggo_size)
    cat_size = cats()
    print(cat_size)
    hamster_size = hamsters()
    print(hamster_size)
    rabbit_size = rabbits()
    print(rabbit_size)
    rat_size = rats()
    print(rat_size)
    guinea_pig_size = guinea_pigs()
    print(guinea_pig_size)
    chinchilla_size = chinchillas()
    print(chinchilla_size)
    turtle_size = turtles()
    print(turtle_size)
    canary_size  = canaries()
    print(canary_size)
