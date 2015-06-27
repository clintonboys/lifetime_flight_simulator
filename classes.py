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

class Player(object):

	def __init__(self, name, age, miles, flights, money):
		self._name = name
		self._age = age
		self._miles = miles
		self._flights = flights
		self._money = money

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

 	current_player = Player(name, 0, 0, 0, 0)

 	print 'Welcome to the world!'
 	print ''
 	print 'This game simulates the exciting, low-risk world of international'
 	print 'long-haul flights. '
 	print '....Loading airport data....'
 	airports = load_airports()

if __name__ == '__main__':
	main()