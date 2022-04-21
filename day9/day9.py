import logging
from pprint import pprint

from lib.data_handler import Datapoint
from lib.file_handler import FileHandler

from pandas import DataFrame


def calc_if_low_spot():
    data = [[m for m in line.replace('\n', '')] for line in FileHandler("input.txt").content_by_lines()]
    print(data)
    col_index = list(range(0,len(FileHandler("input.txt").content_by_lines()[0])))
    row_index = list(range(0,len(data)))
    d = DataFrame(data,index=[row_index],columns=col_index)
    e_positions = []
    for m in row_index:
        for i in col_index:
            e_positions.append((m,i))
    low_spots = []
    for pos in e_positions:
        r = pos[0]
        c = pos[1]
        spot = Datapoint(r,c)
        # print(spot.value(d), spot.neighbors(d))
        if all(spot.value(d) < i for i in spot.neighbors(d)):
            low_spots.append(int(spot.value(d)))
    print(low_spots)
    return sum(low_spots) + len(low_spots)



if __name__ == '__main__':
    d = calc_if_low_spot()
    print(d)
