# executable file that runs tests on code in pesis/pesis/objects

# for now just trials, tidy later


import sys
import os
import importlib
import numpy as np

path, filename = os.path.split('../pesis')
sys.path.append(path)
pesis = importlib.import_module('pesis')
np.random.seed(1)


p1 = pesis.objects.Player('Player One', 10, 2, 'konkari', 'etenijä', 'lukkari')
print(repr(p1))
print(str(p1))

print('\n')
print(pesis.objects.shortest_path(pesis.objects.sites, "kotipesä", "1-pesä"))
print(pesis.objects.shortest_path(pesis.objects.sites, "1-pesä", "2-pesä"))
print(pesis.objects.shortest_path(pesis.objects.sites, "2-pesä", "3-pesä"))
print(pesis.objects.shortest_path(pesis.objects.sites, "3-pesä", "kotipesä"))

print('\n')

