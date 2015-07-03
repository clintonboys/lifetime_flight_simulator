import pandas as pd
import numpy as np
import random
import warnings
warnings.filterwarnings("ignore")

class Player(object):

	def __init__(self, name, country, age, miles, flights, money, is_dead = False):
		self._name = name
		self._country = country
		self._age = age
		self._miles = miles
		self._flights = flights
		self._money = money
		self._is_dead = is_dead
		self._frequent = {}

	def __str__(self):

		return '----------------------' +'\n' + 'NAME:    ' + self._name +'\n'  + 'COUNTRY: ' + self._country +'\n' + 'AGE:     ' + str(self._age) + ' years' +'\n' + 'FLIGHTS: ' + str(self._flights) +'\n'+ 'KM:      ' + str(self._miles) +'\n'  + '----------------------'
