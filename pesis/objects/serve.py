from ..utils import dgv, prc_choice

serve_names = {'tolppa' : (3,2,2),
                'nopea' : (1,0,3),
                'perus' : (0,1,5)
              }

class Serve:
    def __init__(self, name, level, nu):
        self.name = name
        self.level = level
        self.nu = nu
        self.prop = {}
        if   name == 'tolppa':
            self.prop['syöttö'] = dgv(level,nu) + 3
            self.prop['korkeus'] = 2
            self.prop['yleisyys'] = 2
        elif name == 'nopea':
            self.prop['syöttö'] = dgv(level,nu) + 1
            self.prop['korkeus'] = 0
            self.prop['yleisyys'] = 3
        elif name == 'perus':
            self.prop['syöttö'] = dgv(level,nu)
            self.prop['korkeus'] = 1
            self.prop['yleisyys'] = 5

    def copy(self):
        return Serve(self.name, self.level, self.nu)

    def draw(No, level, nu):
        srvs = []
        normlz = float(sum([v[2] for v in serve_names.values()]))
        for s in range(No):
            sel = False
            while not sel:
                serve = list(serve_names.keys())[np.random.randint(3)]
                if prc_choice(serve_names[serve][2] / normlz):
                    srvs.append(Serve(serve, level, nu))
        return srvs
