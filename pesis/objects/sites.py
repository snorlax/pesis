import numpy as np

sites = {
        'kotipesä' : np.array((
                    ('1-pesä', 4),
                    ('etukenttä-k', 4),
                    ('etukenttä-2p', 4)
                             )),
        '1-pesä' : np.array((
                    ('etukenttä-k', 2),
                    ('kotipesä', 4),
                    ('3-pesä', 4),
                    ('polttoraja-3p', 4)
                             )),
        'etukenttä-k' : np.array((
                    ('1-pesä', 2),
                    ('kotipesä', 4),
                    ('etukenttä-2p', 2),
                    ('polttoraja-k', 4)
                             )),
        'etukenttä-2p' : np.array((
                    ('2-pesä', 4),
                    ('kotipesä', 4),
                    ('etukenttä-k', 2),
                    ('polttoraja-2p', 4)
                             )),
        '3-pesä' : np.array((
                    ('1-pesä', 4),
                    ('polttoraja-3p', 3)
                             )),
        '2-pesä' : np.array((
                    ('polttoraja-2p', 3),
                    ('etukenttä-2p', 4)
                             )),
        'polttoraja-3p' : np.array((
                    ('takakenttä-3p', 3),
                    ('3-pesä', 2),
                    ('1-pesä', 4),
                    ('polttoraja-k', 2)
                             )),
        'polttoraja-k' : np.array((
                    ('polttoraja-3p', 2),
                    ('etukenttä-k', 4),
                    ('polttoraja-2p', 2),
                    ('takakenttä-k', 4)
                             )),
        'polttoraja-2p' : np.array((
                    ('polttoraja-k', 2),
                    ('etukenttä-2p', 4),
                    ('2-pesä', 2),
                    ('takakenttä-2p', 4)
                             )),
        'takakenttä-3p' : np.array((
                    ('takakenttä-k', 4),
                    ('polttoraja-3p', 4)
                             )),
        'takakenttä-k' : np.array((
                    ('takakenttä-3p', 4),
                    ('takakenttä-2p', 4),
                    ('polttoraja-k', 4)
                             )),
        'takakenttä-2p' : np.array((
                    ('takakenttä-k', 4),
                    ('polttoraja-2p', 4)
                             ))
        }


def _find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start][:,0]:
        if node not in path:
            newpath = _find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def _find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start][:,0]:
        if node not in path:
            newpaths = _find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def _length_of_path(graph, path):
    l = 0; i = 0
    while i < len(path) - 1:
        edges = graph[path[i]]
        loc_next = np.where(edges[:,0] == path[i+1])
        l += int(edges[loc_next][0][1])
        i += 1
    return l

def shortest_path(graph, start, end):
    paths = _find_all_paths(graph, start, end)
    if len(paths) == 0:
        return None, None
    else:
        shortest = paths[0]
        len_shortest = _length_of_path(graph, paths[0])
        for path in paths:
            len_path = _length_of_path(graph, path)
            if len_path < len_shortest:
                shortest = path
                len_shortest = len_path
        return shortest, len_shortest



