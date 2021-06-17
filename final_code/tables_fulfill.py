from dataclasses import dataclass
import numpy as np
import mariadb
import sys


@dataclass
class Fulfillment:
    vets_number: int = 3
    rooms_number: int = 5
    visits_number: int = 20

    def employees(self):
        