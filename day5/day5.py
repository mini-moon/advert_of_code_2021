import string
from pprint import pprint

from pandas import DataFrame

from lib.file_handler import FileHandler


def get_lines():
    data = [line.replace("\n","").split(" -> ") for line in FileHandler("input.txt").content_by_lines()]
    lines = []
    for line in data:
        n = [i.split(',') for i in line]
        if any([n[0][0] == n[1][0] or n[0][1] == n[1][1],
              n[0][0] == n[1][1] and n[1][1] == n[1][0],
             n[0][1] == n[1][0] and n[1][1] == n[0][0],
               int(n[0][0]) - int(n[1][0]) == int(n[0][1]) - int(n[1][1]),
                abs(int(n[0][0]) - int(n[1][0])) == abs(int(n[0][1]) - int(n[1][1]))]):
            n = [[int(i) for i in m] for m in n]
            lines.append(n)
    return lines

def get_spots_in_line(line):
    start = line[0]
    end = line[1]
    if start[0]== end[0]:
        spots_in_line = [(end[0],x) for x in list(range(min(start[1],end[1]),max(start[1],end[1])+1))]
    elif start[1]== end[1]:
        spots_in_line = [(x,end[1]) for x in list(range(min(start[0],end[0]),max(start[0],end[0]) +1))]
    elif end[0] - start[0] == end[1] - start[1]:
        spots_in_line = list(zip(list(range(min(start[0],end[0]),max(start[0],end[0])+1)),list(range(min(start[1],end[1]),max(start[1],end[1])+1))))
    elif abs(end[0] - start[1]) == abs(end[1] - start[0]):
        spots_in_line = list(zip(list(range(min(start[0], end[0]), max(start[0], end[0]) + 1))[::-1],
                                 list(range(min(start[1], end[1]), max(start[1], end[1]) + 1))))
    else:
        spots_in_line = []
    return spots_in_line


def calc_crossed_spots():
    lines = get_lines()
    pprint(lines)
    lines_collection = []
    for line in lines:
        spots_in_line = get_spots_in_line(line)
        print(spots_in_line)
        lines_collection.extend(spots_in_line)
    spot_point_map = {}.fromkeys(set(lines_collection))
    for i in lines_collection:
        if i in spot_point_map.keys():
            if spot_point_map[i]:
                spot_point_map[i] +=1

            else:
                spot_point_map[i] =1
    new_map = {k:v for k,v in spot_point_map.items() if v >=2}
    return len(new_map)


if __name__ == '__main__':
    print(calc_crossed_spots())