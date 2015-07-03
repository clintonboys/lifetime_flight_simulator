import pandas as pd
import numpy as np
import random
import warnings
warnings.filterwarnings("ignore")
from start_game import start_game

def nice_print(l):
	if len(l) < 8:
		for entry in l:
			print entry
	else:
		cols = 4
		split=[l[i:i+len(l)/cols] for i in range(0,len(l),len(l)/cols)]
		for row in zip(*split):
			print "".join(str.ljust(i,20) for i in row)


def main():

	current_player, act, network, arr = start_game()

	while not current_player._is_dead:
		death_chance = np.random.randint(0,100000)
		if death_chance < int((act.prob_1[int(current_player._age)]*100000 + act.prob_2[int(current_player._age)]*100000)/2):
			print 'Sorry, you died of natural causes at the ripe old age of ' + str(current_player._age) + '.'
			current_player._is_dead = True
			break

		dep = arr

		print '-----------------------------------------------------------------'
		print 'Welcome to ' + dep + ' airport!'

		nice_print(network[network.dep_airport == dep].arr_airport.unique().tolist())

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

	 	try:
	 		current_player._frequent[this_airline] += distance
	 	except KeyError:
	 		current_player._frequent[this_airline] = distance

 		plane_death_chance = np.random.randint(0,1000000000000)
 		if plane_death_chance < int(5*distance):
 			print 'How unlucky. You died in a plane crash.'
 			current_player._is_dead = True
 			print current_player
 			print 'You can rest in peace for eternity having accrued the '
 			print 'following impressive collection of frequent flyer miles:'
 			for key in current_player._frequent:
 				print key, frequent[key]
 			break
 		else:
 			age_update = raw_input('How long until your next flight? (months)..')

 			current_player._age += np.round(float(age_update)/12.0,3)
 			current_player._miles += np.round(distance,3)
 			current_player._flights += 1
 			current_player._money -= np.round(distance*(12000/2000),3)

 			print current_player

if __name__ == '__main__':

	main()
