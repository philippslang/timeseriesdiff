import numpy as np
import timeseriesdiff as td


def test_overlap():
    x0 = np.array(np.arange(0.0, 11.0))
    x1 = np.array(np.arange(4.0, 14.0))
    overlap = td.common.overlap(x0, x1)
    assert overlap.xmin == 4.0
    assert overlap.xmax == 10.0
