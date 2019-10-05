import pandas as pd
from math import sqrt

GRAV_CONST = 9.8 # m/s^2


def calc_velocity(STRIDE_LENGTH, LEG_LENGTH, grav_const):
    """Calculate velocity of the dinossaur
    """
    return ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * grav_const)


def merge_datasets(filenames: list(), key='NAME'):
    """Get a list of csv filename paths and a key column to use to prior the merge
    
    Parameters:
    -----------     
    filenames: list
        list of csv filenames
    
    Returns
    -------
    pandas dataset
        A dataset containing the filename1 and filename2 csvs data merged
    """
    ds = pd.read_csv(filenames[0])
    for filename in filenames[1:]:
        ds = ds.merge(pd.read_csv(filename), on=key)
    return ds


def filter_by(dataset, key, condition):
    """Returns a filtered dataset taken from base the key and the condition
    
    Parameters
    ----------
    dataset: pandas dataset
        A dataset to be filtered
    key: string
        The column name of the dataset to be compared to the condition
    conditionm: string
        The value used to filter into the dataset from a gived key
    
    Returns
    -------
    pandas dataset:
        The filtered dataset
    """
    _filter = DATASET[key]==condition
    return DATASET[_filter]


def most_faster_dinos(dataset):
    """Iter into dataset calculing the velocity of each dinossaur
    Parameters
    ----------
    dataset: pandas dataset
        The dataset containing the clean dinossaur data
    Returns
    -------
    list:
        A list of objects containing the dinossaur previous data
        plus your velocity
    """
    results = []
    for _, dino in dataset.iterrows():
        vel = calc_velocity(dino['STRIDE_LENGTH'], dino['LEG_LENGTH'], GRAV_CONST)
        res = dict(dino)
        res['vel'] = vel
        results += [res]
    results.sort(key=lambda x: x['vel'], reverse=True)
    return results


DATASET = merge_datasets(['dataset1.csv', 'dataset2.csv'])
bipedals = filter_by(DATASET, 'STANCE', 'bipedal')
results = most_faster_dinos(bipedals)

# print the faster dinossaurs in order to the velocity
if __name__ == '__main__':
    for dino in results:
        print(dino['NAME'])