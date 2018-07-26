from .create_players import create_players
from play_action import select_actions, action

def vuoro(ui, ins_pj, out_pj):
    palot = 0; lyoja = ins_pj.ros.turn(); vl = (lyoja-1)%10
    juoksut = 0
    ins_pj.roster.init_ins_turn()
    out_pj.roster.init_out_turn()
    while palot < 3:
        if lyoja == vl:
            ui.lyojat_ended()
            break
        select_actions(ui, ins_pj, out_pj, lyoja)
        action(ui, ins_pj.ros, out_pj.ros, lyoja, palot, juoksut)
    ui.three_paloa()
    return juoksut

def vuoronvaihto(ins_pj, out_pj):
    return out_pj, ins_pj

def game(ui, pj1, pj2):
    ui.game_begins()

    # create players, select rosters
    pj1.ros = ui.select_roster(pj1, create_players())
    pj2.ros = ui.select_roster(pj2, create_players())

    # set initial values, TODO hutunkeitto
    ins_pj = pj1; out_pj = pj2
    jaksovoitot = [0,0]

    # play first jakso
    jakso = 1; vp = 1; juoksut = [0,0]
    ui.jakso_begins(jakso)
    while vp <= 4:
        ui.vuoropari_begins(vp)
        juoksut[0] += vuoro(ui, ins_pj, out_pj)
        ui.vuoronvaihto(ins_pj, out_pj)
        ins_pj, out_pj = vuoronvaihto(ins_pj, out_pj)
        juoksut[1] += vuoro(ui, ins_pj, out_pj)
        ui.vuoronvaihto(ins_pj, out_pj)
        ins_pj, out_pj = vuoronvaihto(ins_pj, out_pj)
    if juoksut[0] > juoksut[1]:
        jaksovoitot[0] += 1
    elif juoksut[0] < juoksut[1]:
        jaksovoitot[1] += 1

    # play second jakso
    jakso = 2; vp = 1; juoksut = [0,0]
    ui.jakso_begins(jakso)
    while vp <= 4:
        ui.vuoropari_begins(vp)
        juoksut[0] += vuoro(ui, ins_pj, out_pj)
        ui.vuoronvaihto(ins_pj, out_pj)
        ins_pj, out_pj = vuoronvaihto(ins_pj, out_pj)
        juoksut[1] += vuoro(ui, ins_pj, out_pj)
        ui.vuoronvaihto(ins_pj, out_pj)
        ins_pj, out_pj = vuoronvaihto(ins_pj, out_pj)
    if juoksut[0] > juoksut[1]:
        jaksovoitot[0] += 1
    elif juoksut[0] < juoksut[1]:
        jaksovoitot[1] += 1    

    # finalize game
    ui.game_ended


