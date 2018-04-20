import collections

import numpy as np
from scipy import interpolate, integrate

from . import common


data = collections.namedtuple('data', 'x0 x1 overlap interpolation')


def preprocess(x0, x1):
    overlap = common.overlap(x0, x1)
    return data(x0, x1, overlap, None)


def area(y0, y1, data, npoints=10):
    f0 = interpolate.interp1d(data.x0, y0)
    f1 = interpolate.interp1d(data.x1, y1)

    def fdelta(x):
        return f1(x) - f0(x)

    integral = integrate.quad(fdelta, data.overlap.xmin, data.overlap.xmax)
    return integral[0]
