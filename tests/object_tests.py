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
