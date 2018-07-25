from ..utils import dgv, prc_choice

hit_names = {    
    'koppi':
        (-2,-2,4,5,('takakenttä-2p','takakenttä-k','takakenttä-3p')),
    'rajakova':
        (3,2,0,4,('2-pesä','3-pesä')),
    'luukku':
        (3,2,0,4,('polttoraja-2p', 'polttoraja-3p')),
    'jatke':
        (3,2,2,4,('takakenttä-2p','takakenttä-3p')),
    'varsilyönti':
        (1,4,1,2,('etukenttä-k')),
    'pomppu':
        (4,4,0,1,('etukenttä-2p', 'etukenttä-k','1-pesä')),
    'pussi':
        (1,2,0,3, ('polttoraja-2p','polttoraja-3p')),
    'ohitus':
        (0,3,0,3,('etukenttä-k')),
    'koukkunäpy':
        (0,2,0,4,('1-pesä', 'etukenttä-2p')),
    'perusnäpy':
        (0,1,0,4,('etukenttä-2p','etukenttä-k','1-pesä')),
    'pitkänäpy':
        (1,2,0,2,('1-pesä', 'etukenttä-2p')),
    'tuppinäpy':
        (0,4,0,2,('1-pesä', 'etukenttä-2p')),
    'pystynäpy':
        (0,0,1,2,('etukenttä-2p', 'etukenttä-k', '1-pesä')),
    'kumura':
        (3,4,3,1,('takakenttä-2p', 'takakenttä-k', 'takakenttä-3p')),
    'vapaa':
        (4,3,4,3,('takakenttä-2p', 'takakenttä-k', 'takakenttä-3p'))
        }

class Hit:

    def __init__(self, name, level, nu, prop=None):
        self.name = name
        self.level = level
        self.nu = nu
        if prop is not None:
            self.prop = prop
        else:
            self.prop = {}
            self.prop['voima'] = dgv(level,nu) + hit_names[name][0]
            self.prop['tarkkuus'] = dgv(level,nu) + hit_names[name][1]
            self.prop['korkeus'] = hit_names[name][2]
            self.prop['yleisyys'] = hit_names[name][3]
            self.prop['suuntaus'] = hit_names[name][4]


    def copy(self):
        return Hit(self.name, self.level, self.nu, self.prop.copy())

    @staticmethod
    def _sum_yleisyys():
        return sum([v[3] for v in hit_names.values()])

    @staticmethod
    def draw(No, level, nu):
        hits = []
        sy = float(Hit._sum_yleisyys())
        for h in range(No):
            sel = False
            while not sel:
                hit = list(hit_names.keys()) \
                      [np.random.randint(len(hit_names))]
                if prc_choice(hit_names[hit][3] / sy):
                    hits.append(hit)
                    sel = True
        for i in range(len(hits)):
            hits[i] = Hit(hits[i], level, nu)
        return hits


