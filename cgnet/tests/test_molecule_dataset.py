import numpy as np
import torch

from cgtools.feature import MoleculeDataset

beads = np.random.randint(10)
dims = np.random.randint(5)

x = np.random.randn(20, beads, dims)
y = np.random.randn(20, beads, dims)


def test_adding_data():
    ds1 = MoleculeDataset(x, y)

    ds2 = MoleculeDataset(x, y, selection=np.arange(10))
    ds2.add_data(x, y, selection=np.arange(10, 20))

    np.testing.assert_array_equal(ds1.coordinates, ds2.coordinates)
    np.testing.assert_array_equal(ds1.forces, ds2.forces)


def test_stride():
    stride = np.random.randint(1, 4)
    ds = MoleculeDataset(x, y, stride=stride)

    strided_x = x[::stride]
    strided_y = y[::stride]

    np.testing.assert_array_equal(ds.coordinates, strided_x)
    np.testing.assert_array_equal(ds.forces, strided_y)