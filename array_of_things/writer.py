import pandas as pd
import h5py


def make_group(hdf5_file, group_name):
    hdf5_file.create_group(group_name)


def init_dataset(subgrp_name, subgroup, column):
    return subgroup.create_dataset(subgrp_name,
                                   column.shape,
                                   dtype=column.dtypes)


def write_column(group, subgroup):
    for row in enumerate(group[subgroup]):
        group[row[0]] = row[1]


def main():
    # input parameters
    filename = 'chicago_test.h5'

    # open csv files to be converted
    nodes = pd.read_csv('nodes.csv')
    sensors = pd.reawd_csv('sensors.csv')
    data = pd.read_csv('data.csv')

    file = h5py.File(filename, 'a')


if __name__ == "__main__":
    main()
