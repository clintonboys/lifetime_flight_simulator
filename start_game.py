import numpy as np
import pandas as pd
import random
import warnings
warnings.filterwarnings("ignore")
import player

def load_network():

	return pd.read_csv('world_network.csv')

def load_actuarial_table():

	return pd.read_csv('actuarial_table.csv')


def nice_print(l):
	if len(l) < 8:
		for entry in l:
			print entry
	else:
		cols = 4
		split=[l[i:i+len(l)/cols] for i in range(0,len(l),len(l)/cols)]
		for row in zip(*split):
			print "".join(str.ljust(i,20) for i in row)


def start_game():

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
 	print '-----------------------------------------------------------------'
 	name    = raw_input('What is your name?..      ')
 	country = raw_input('And where are you from?.. ')

 	current_player = player.Player(name, country, 0.0, 0.0, 0, 0.0)

 	print '-----------------------------------------------------------------'
 	print 'Welcome to the world!'
 	print ''
 	print 'This game simulates the exciting, low-risk world of air travel!'
 	print '....Loading airport data....'
 	network = load_network()
 	print '....Loading actuarial table....'
 	act = load_actuarial_table()
 	print '-----------------------------------------------------------------'
 	print 'Let \'s get started!'

 	print current_player

	network.columns = ['dep_airport', 'dep_city', 'dep_country', 'long_dep', 'lat_dep',
			 		     'arr_airport', 'arr_city', 'arr_country', 'long_arr', 'lat_arr',
			 		     'airline', 'airline_country', 'airline_active', 'distance', 'is_domestic']

 	print 'You have just been born in ' + country +'. Time for your first flight!'
 	print 'Select the airport your parents have chosen to depart from the'
 	print 'list of airports below.'

	nice_print(network[network.dep_country == country][['dep_airport']].dep_airport.unique().tolist())
 	dep = raw_input('Departing airport...')

 	while len(network[network.dep_airport == dep]) == 0:
 		print 'Cannot recognise departing airport. Please try again.'
 		dep = raw_input('Departing airport...')

 	print 'Welcome to ' + dep + ' airport!'

 	nice_print(network[network.dep_airport == dep].arr_airport.unique().tolist())

 	arr = raw_input('Where are you travelling to today?...')

 	while len(network[network.dep_airport == dep][network.arr_airport == arr]) == 0:
 		print 'Cannot recognise arriving airport. Please try again.'
 		arr = raw_input('Where are you travelling to today?...')

 	if len(network[network.dep_airport == dep][network.arr_airport == arr]) == 1:
 		this_airline = network[network.dep_airport == dep][network.arr_airport == arr].airline.iloc[0]
 	else:
 		print 'There is more than one carrier between the locations you have selected.'
 		nice_print(network[network.dep_airport == dep][network.arr_airport == arr].airline.unique().tolist())
 		this_airline = raw_input('Who would you prefer to fly with?..')
 		while len(network[network.dep_airport == dep][network.arr_airport == arr][network.airline == this_airline]) == 0:
 			print 'Cannot recognise airline. Please try again.'
 			this_airline = raw_input('Who would you prefer to fly with?..')

 	distance = network[network.dep_airport == dep][network.arr_airport == arr][network.airline == this_airline].distance.iloc[0]
 	print 'You have arrived!'
 	age_update =  raw_input('How long until your next flight? (months)..')

	current_player._age += np.round(float(age_update)/12.0,3)
	current_player._miles += np.round(distance,3)
	current_player._flights += 1
	current_player._money -= np.round(distance*(12000/2000),3)

	print current_player

	return current_player, act, network, arr

