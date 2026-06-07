#Dictionary & DATAframe

import pandas as pd
import numpy as np

countries = ['United States', 'Australia', 'Japan', 
             'India','Russia', 'Morocco', 'Egypt']

drives_right = [True, False, False, False, True, True, True]

cars_per_capita = [809, 731, 588, 18, 200, 70, 45]

cars_dict = {
    'country': countries,
    'drives_right': drives_right,
    'cars_per_capita': cars_per_capita
}

cars = pd.DataFrame(cars_dict)

cars.loc[0:6, 'country']
cars.loc[0:6, ['country', 'drives_right']]
cars.loc[:6, 'drives_right']
cars.loc[5:6, 'drives_right']
cars.loc[:1, ['country','drives_right','cars_per_capita']]

cars.iloc[0:7, 0]
cars.iloc[0:7, 0:2]
cars.iloc[:6, 1]
cars.iloc[5:6, 1]
cars.iloc[:1, 0:3]

#List

Europe_list = []

spain = {'capital': 'madrid', 'population': 46.77}
france = {'capital': 'paris', 'population': 66.03}
germany = {'capital': 'berlin', 'population': 80.62}
norway = {'capital': 'oslo', 'population': 5.084}
italy = {'capital': 'rome', 'population': 59.83}

Europe_list.append(spain)
Europe_list.append(france)
Europe_list.append(germany)
Europe_list.append(norway)
Europe_list.append(italy)

#Matrix

import numpy as np 
matrix = np.array ([ 
['aa', 'ab', 'ac'], 
['ba', 'bb', 'bc'], 
['ca', 'cb', 'cc'] 
]) 

for row in matrix:
    for item in row:
        print(item)