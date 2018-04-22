import numpy as np
import timeseriesdiff as td


def test_area_linear():
    x = np.arange(0.0, 11.0)
    y0 = np.zeros_like(x)
    y1 = x * 2.0
    data = td.interpolate.preprocess(x, x)
    diff = td.interpolate.area(y0, y1, data)
    assert np.allclose([diff], [100.0])


def test_area_adversarial():
    x = np.linspace(0.0, 6.0 * np.pi, 100)
    y0 = np.zeros_like(x)
    y1 = np.sin(x)
    data = td.interpolate.preprocess(x, x)
    diff = td.interpolate.area(y0, y1, data)
    assert np.allclose([diff], [0.0])
