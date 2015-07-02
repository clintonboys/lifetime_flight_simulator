''' 
        _____ _______ _______ _______ _____ _______ _______          
 |        |   |______ |______    |      |   |  |  | |______          
 |_____ __|__ |       |______    |    __|__ |  |  | |______          
                                                                     
 _______        _____  ______ _     _ _______                        
 |______ |        |   |  ____ |_____|    |                           
 |       |_____ __|__ |_____| |     |    |                           
                                                                     
 _______ _____ _______ _     _        _______ _______  _____   ______
 |______   |   |  |  | |     | |      |_____|    |    |     | |_____/
 ______| __|__ |  |  | |_____| |_____ |     |    |    |_____| |    \_
                                                                     
----------------------------------------------------------------------

'''

import pandas as pd
import numpy as np

class Player(object):

	def __init__(self, name, country, age, miles, flights, money):
		self._name = name
		self._country = country
		self._age = age
		self._miles = miles
		self._flights = flights
		self._money = money

	def print_player_stats(self):

		print '----------------------'
	 	print 'NAME:    ' + self._name
	 	print 'COUNTRY: ' + self._country
	 	print 'AGE:     ' + str(self._age) + ' years'
	 	print 'FLIGHTS: ' + str(self._flights) 
	 	print 'MILES:   ' + str(self._miles)
	 	print '----------------------'


class Flight(object):

	def __init__(self, origin, destination, time, distance, cost, carrier):
		self._origin = origin
		self._destination = destination
		self._time = time
		self._distance = distance
		self._cost = cost
		self._carrier = carrier

def load_airports():

	return pd.read_csv('airports.csv')

def compute_distance(lat1,long1,lat2,long2):
	r = 6371000
	phi1 = np.radians(lat1)
	phi2 = np.radians(lat2)
	dphi = np.radians(lat2 - lat1)
	dlam = np.radians(long2 - long1)

	a = np.sin(dphi/2) * np.sin(dphi/2) + np.cos(phi1) * np.cos(phi2) * np.sin(dlam/2) * np.sin(dlam/2)
	c = 2*np.arctan2(np.sqrt(a), np.sqrt(1-a))

	return r*c/1000

def main():
	print '---------------------------------------------------------------------'
	print '        _____ _______ _______ _______ _____ _______ _______          '
 	print ' |        |   |______ |______    |      |   |  |  | |______          '
 	print ' |_____ __|__ |       |______    |    __|__ |  |  | |______          '
 	print '                                                                     '
 	print '_______        _____  ______ _     _ _______                         '
 	print '|______ |        |   |  ____ |_____|    |                            '
 	print '|       |_____ __|__ |_____| |     |    |                            '
 	print '                                                                     '
 	print '_______ _____ _______ _     _        _______ _______  _____   ______ '
 	print '|______   |   |  |  | |     | |      |_____|    |    |     | |_____/ '
 	print '______| __|__ |  |  | |_____| |_____ |     |    |    |_____| |    \_ '
 	print '                                                                     '
 	print '----(c) 2015 Clinton Boys -------------------------------------------'

 	print 'Welcome to Lifetime Flight Simulator.'
 	name = raw_input('What is your name?.. ')
 	country = raw_input('And where are you from?.. ')

 	current_player = Player(name, country, 0, 0, 0, 0)

 	print 'Welcome to the world!'
 	print ''
 	print 'This game simulates the exciting, low-risk world of international'
 	print 'long-haul flights. '
 	print '....Loading airport data....'
 	airports = load_airports()
 	#print airports.head()
 	print 'Let \'s get started!'
 	current_player.print_player_stats()
 	airports.columns = ['row', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'long', 'alt', 'timezone', 'dst', 'time_area']
 	print 'You have just been born in ' + country +'. Time for your first flight!'
 	print 'Select the airport your parents have chosen to depart from...'
 	print airports[airports.country == country][['name', 'city', 'country', 'iata']]
 	row_no_dep = raw_input('Departing airport...')
 	row_no_arr = raw_input('Arriving airport...')
 	distance = compute_distance(airports.lat[int(row_no_dep)], airports.long[int(row_no_dep)], airports.lat[int(row_no_arr)], airports.long[int(row_no_arr)])
 	print 'You have arrived!'
 	age_update =  raw_input('How long until your next flight? (months)..')

	current_player._age += float(age_update)/12.0
	current_player._miles += distance
	current_player._flights += 1
	current_player._money -= distance*(12000/2000)

	current_player.print_player_stats()


if __name__ == '__main__':

	main()
