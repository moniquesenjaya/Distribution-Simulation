import numpy as np
from scipy import stats

def uniforming(a, b):
    height = 1 / (b - a)
    mean = (a + b) / 2
    sd = (b - a) / 12 ** (1/2)
    lin = np.linspace(0, (a + b), 100)
    return [a, b - a, height, mean, sd, lin]

def normaling(mean, std):
    x = stats.norm(loc = mean, scale = std)
    xRvs = x.rvs(500)
    pdf = x.pdf(np.sort(xRvs))

    z = stats.zscore(xRvs)
    return [x, xRvs, pdf, z]
