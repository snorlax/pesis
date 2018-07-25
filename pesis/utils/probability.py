from scipy.stats import norm
import numpy as np

def dgv(mu, nu, minv=1, maxv=20):
    "Discrete Gaussian variate"
    rv = round(norm.rvs(mu,nu))
    return min( max(rv,minv), maxv)

def cgv(mu, nu, minv=0., maxv=1.):
    "Continuous Gaussian variate"
    rv = norm.rvs(mu,nu)
    return min( max(rv,minv), maxv)

def rand_pick(l):
    return l[np.random.randint(len(l))]

def prc_choice(p):
    "Percentage choice"
    if np.random.rand() <= p:
        return True
    else:
        return False
