from scipy.stats import norm

def dgv(mu, nu, minv=1, maxv=20):
    "Discrete Gaussian variate"
    rv = round(norm.rvs(mu,nu))
    return min( max(rv,minv), maxv)

def cgv(mu, nu, minv=0., maxv=1.):
    "Continuous Gaussian variate"
    rv = norm.rvs(mu,nu)
    return min( max(rv,minv), maxv)

