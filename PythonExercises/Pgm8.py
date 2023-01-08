#!/bin/usr/env python 3
# example of numpy array

import numpy as np                                              # import is not recogined as key word, also looks like path/ access issue

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
weight_lbs = []                                                 # not required

np_weight_kg = np.array(weight_kg)
np_weight_lbs = np.array(weight_lbs)

np_weight_lbs = 2.2 * np_weight_kg

print(np_weight_lbs)
