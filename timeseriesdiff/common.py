import collections

import numpy as np


data = collections.namedtuple('data', 'xmin xmax')


def overlap(x0, x1):
    """
    """
    xmin = max(np.min(x0), np.min(x1))
    xmax = min(np.max(x0), np.max(x1))
    return data(xmin, xmax)
