import os
import pytest

import pandas as pd
from pandas.testing import assert_frame_equal

from main import (
    calc_velocity,
    merge_datasets,
    filter_by,
    GRAV_CONST
)

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

@pytest.fixture
def dataset():
    ds1 = pd.read_csv(os.path.join(FIXTURES_DIR, 'dataset1.csv'))
    ds2 = pd.read_csv(os.path.join(FIXTURES_DIR, 'dataset2.csv'))
    return ds1.merge(ds2, on='NAME')


def test_filter_by_bipedal(dataset):
    ds = filter_by(dataset, 'STANCE', 'bipedal')
    assert len(ds.index) == 4


def test_calc_velocity_success():
    assert calc_velocity(1.4, 1.2, GRAV_CONST) == 0.5715476066494085


def test_merge_datasets_success(dataset):
    ds = merge_datasets([
        os.path.join(FIXTURES_DIR, 'dataset1.csv'),
        os.path.join(FIXTURES_DIR, 'dataset2.csv')
    ])
    assert_frame_equal(ds, dataset, check_dtype=False)
