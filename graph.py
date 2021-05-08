import numpy as np
from scipy import stats

def uniforming(a, b):
    height = 1 / (b - a)
    mean = (a + b) / 2
    sd = (b - a) / 12 ** (1/2)
    lin = np.linspace(0, (a + b), 100)
    return [a, b - a, height, mean, f"{sd:.4f}", lin]

def normaling(mean, std, rvs, xval=0):
    x = stats.norm(loc = mean, scale = std)
    xRvs = x.rvs(rvs)
    pdf = x.pdf(np.sort(xRvs))

    z = (xval-mean)/std
    return [x, xRvs, pdf, z]
