from ..objects import Player
from ..utils import dgv, prc_choice, rand_pick

def draw_players(level_multiplier=1.):
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

def game(ui, pj1, pj2):

    # TODO make this much more simply, own functions for jakso, vuoropari, vuoro jne.
    
    # draw players
    pj1_roster = draw_players()
    pj2_roster = draw_players()

    # select rosters for game
    pj1_roster = ui.select_players(pj1, pj1_roster)
    pj2_roster = ui.select_players(pj2, pj2_roster)

    # hutunkeitto and starter
    hk1 = ui.select_hutunkeittaja(pj1, pj1_roster)
    hk2 = ui.select_hutunkeittaja(pj2, pj2_roster)
    winner = hutunkeitto(ui, hk1, hk2)
    if winner == hk1:
        starts_in = ui.select_turn(pj1)
        if starts_in:
            starter = pj1
        else:
            starter = pj2
    else:
        starts_in = ui.select_turn(pj2)
        if starts_in:
            starter = pj2
        else:
            starter = pj1

    # play one game
    jakso = 1; vp = [1,1]
    inpj = starter
    if inpj == pj1: outpj = pj2
    else: outpj = pj1

    # play first jakso
    lyoja1 = 1, lyoja2 = 1
    while vp[0] <= 4:
        # play one vuoropari
        palot = 0
        while palot < 3:
            # play one serve
            
                





