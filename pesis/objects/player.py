from ..utils import dgv

class Player:
    def __init__(self, name, level, nu, gen_type, in_type, out_type):
        self.name = name
        self.level = level
        self.nu = nu
        self.gen_type = gen_type
        gen_charac = self.gen_characs(gen_type)
        self.in_type = in_type
        in_charac = self.in_characs(in_type)
        self.out_type = out_type
        out_charac = self.out_characs(out_type)

        # skills
        self.sk = {}
        self.sk['PS'] = dgv(level, nu) + gen_charac[0]
        self.sk['HN'] = dgv(level, nu) + gen_charac[1]
        self.sk['RH'] = dgv(level, nu) + gen_charac[2]
        self.sk['KA'] = dgv(level, nu) + gen_charac[3]
        self.sk['NP'] = dgv(level, nu) + in_charac[0]
        self.sk['VM'] = dgv(level, nu) + in_charac[1]
        self.sk['TK'] = dgv(level, nu) + in_charac[2]
        self.sk['SY'] = dgv(level, nu) + out_charac[0]
        self.sk['KP'] = dgv(level, nu) + out_charac[1]
        self.sk['HT'] = dgv(level, nu) + out_charac[2]

    @staticmethod
    def props_dict():
        ls = {
            'Pelisilmä'     : 'PS', # general
            'Havainnointi'  : 'HN', # general
            'Rohkeus'       : 'RH', # general
            'Kurinalaisuus' : 'KA', # general
            'Nopeus'        : 'NP', # inside
            'Voima'         : 'VM', # inside
            'Tarkkuus'      : 'TK', # inside
            'Syöttö'        : 'SY', # outside
            'Koppaus'       : 'KP', # outside
            'Heitto'        : 'HT' # outside
              }
        sl = {v:k for k,v in ls.items()}
        return ls, sl

    @staticmethod
    def gen_characs(gtype):
        "(PS,HN,RH,KA)"
        if   gtype == "perusvarma":
            return (-1,1,-2,2)
        elif gtype == "tulokas":
            return (-3,1,2,0)
        elif gtype == "konkari":
            return (2,0,0,-2)
        else:
            raise TypeError("Invalid gen_charac + '" + gtype + "'")

    @staticmethod
    def in_characs(itype):
        "(NP,VM,TK)"
        if   itype == "lyöjä":
            return (-3,2,1)
        elif itype == "etenijä":
            return (3,-2,-1)
        elif itype == "yleispelaaja":
            return (0,-1,1)
        else:
            raise TypeError("Invalid in_charac + '" + itype + "'")

    @staticmethod
    def out_characs(otype):
        "(SY,KP,HT)"
        if   otype == "koppari":
            return (-3,0,3)
        elif otype == "sieppari":
            return (-3,3,0)
        elif otype == "pesävahti":
            return (-2,1,1)
        elif otype == "lukkari":
            return (2,-1,-1)
        else:
            raise TypeError("Invalid out_charac + '" + otype + "'")


    def __repr__(self):
        s = self.name + " ("
        s += "PS:%-2i"%(self.sk['PS']) + " "
        s += "HN:%-2i"%(self.sk['HN']) + " "
        s += "RH:%-2i"%(self.sk['RH']) + " "
        s += "KA:%-2i"%(self.sk['KA']) + " "
        s += "NP:%-2i"%(self.sk['NP']) + " "
        s += "VM:%-2i"%(self.sk['VM']) + " "
        s += "TK:%-2i"%(self.sk['TK']) + " "
        s += "SY:%-2i"%(self.sk['SY']) + " "
        s += "KP:%-2i"%(self.sk['KP']) + " "
        s += "HT:%-2i"%(self.sk['HT']) + ")"
        return s

    def __str__(self):
        s  = "{:^36}\n".format("-" + self.name + "-")
        s += "Pelisilmä:     %2i"%(self.sk['PS']) + "  "
        s += "Havainnointi:  %2i"%(self.sk['HN']) + "\n"
        s += "Rohkeus:       %2i"%(self.sk['RH']) + "  "
        s += "Kurinalaisuus: %2i"%(self.sk['KA']) + "\n"
        s += "Nopeus:        %2i"%(self.sk['NP']) + "  "
        s += "Voima:         %2i"%(self.sk['VM']) + "\n"
        s += "Tarkkuus:      %2i"%(self.sk['TK']) + "  "
        s += "Syöttö:        %2i"%(self.sk['SY']) + "\n"
        s += "Koppaus:       %2i"%(self.sk['KP']) + "  "
        s += "Heitto:        %2i"%(self.sk['HT']) + "\n"
        return s

