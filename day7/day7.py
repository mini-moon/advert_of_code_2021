import logging

from lib.file_handler import FileHandler


def get_gap_between_min_and_max(data):
    return max(data) - min(data)

def get_all_possible_possitions(data):
    return(list(range(min(data),max(data)+1)))

def calc_move_fuel_map():
    data = FileHandler("input.txt").str_content_to_list()
    data = [int(i) for i in data]
    move_position_map = {k:[] for k in get_all_possible_possitions(data)}
    position_fuel_map = {k:0 for k in get_all_possible_possitions(data)}
    for position in move_position_map.keys():
        for move in data:
            move_position_map[position].append(move)
            position_fuel_map[position]+= (abs(move-position))
            position_fuel_map[position]+= (sum(list(range(abs(move-position)))))

    optimized_position = [v for k,v in position_fuel_map.items() if v == min(position_fuel_map.values())]

    print(position_fuel_map)
    return optimized_position

if __name__ == '__main__':
    print(calc_move_fuel_map())

