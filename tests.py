
import pandas as pd
import numpy as np
import random
airports = pd.read_csv('airports.csv')
act = pd.read_csv('actuarial_table.csv')
airports.columns = ['row', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'long', 'alt', 'timezone', 'dst', 'time_area']
print len(airports)
airports = airports[pd.notnull(airports.iata)]
print len(airports)
network = pd.read_csv('world_network.csv')
network.columns = ['dep_airport', 'dep_city', 'dep_country', 'long_dep', 'lat_dep',
			 		     'arr_airport', 'arr_city', 'arr_country', 'long_arr', 'lat_arr',
			 		     'airline', 'airline_country', 'airline_active', 'distance', 'is_domestic']
print network[network.dep_airport == 'Dubbo'][network.arr_airport == 'Sydney Intl']