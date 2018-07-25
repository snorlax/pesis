import numpy as np

class Roster:
    def __init__(self):
        self.turn      = 0
        self.players   = [None]*12
        self.locations = [None]*12

    def get_location(self, player):
        return self.locations(np.where(
                    np.array(self.players) == player)
                             )

    def get_occupation(self, location):
        ind = np.where(np.array(self.locations) == location)[0]
        occ = None if ind.size == 0 else self.players[ind]
        return occ

    def __str__(self):
        s = ""
        for i in range(12):
            s += self.players[i] + " at " + self.locations[i] + "\n"
