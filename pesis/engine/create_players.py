from ..objects import Player
from ..utils import dgv, prc_choice, rand_pick

def create_players(level_multiplier=1.):
    ps = []; lm = level_multiplier; nu = 2.
    gens = ('perusvarma','tulokas','konkari')
    ins  = ('lyöjä','etenijä','yleispelaaja')
    outs = ('koppari','sieppari','polttaja','lukkari')
    ps.append(Player('Player A', dgv(14,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player B', dgv(14,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player C', dgv(13,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player D', dgv(12,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player E', dgv(12,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player F', dgv(10,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player G', dgv(10,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player H', dgv(10,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player I', dgv(10,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player J', dgv(8,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player K', dgv(8,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player L', dgv(6,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player M', dgv(6,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player N', dgv(4,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    ps.append(Player('Player O', dgv(4,1)*lm, nu, rand_pick(gens),
                        rand_pick(ins), rand_pick(outs))
    return ps

