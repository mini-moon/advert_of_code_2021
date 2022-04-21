from pandas import DataFrame

from lib.data_handler import Datapoint
from lib.file_handler import FileHandler


def find_all_paths():
    data = [[m for m in line.replace('\n', '')] for line in FileHandler("input.txt").content_by_lines()]
    col_index = list(range(0,len(FileHandler("input.txt").content_by_lines()[0])))
    row_index = list(range(0,len(data)))
    d = DataFrame(data,index=[row_index],columns=col_index)
    e_positions = []
    for m in row_index:
        for i in col_index:
            e_positions.append((m,i))
    r = 0
    c = 0
    spot = Datapoint(r,c)
    print(spot.value(d))
    path = 0
    path, options = compare_paths(spot,path,d)
    while options:
        for opt in options:
            spot = Datapoint(opt[0],opt[1])
            print(spot.value(d),spot.down(d),spot.after(d))
            path, options = compare_paths(spot,path,d)
    return path


def compare_paths(spot,path,data_frame):
    if not spot.after(data_frame) and spot.down(data_frame):
        down_spot = [spot.row + 1, spot.col]
        return(path + spot.down(data_frame),[down_spot])
    if not spot.down(data_frame) and spot.after(data_frame):
        right_spot = [spot.row, spot.col + 1]
        return(path + spot.after(data_frame),[right_spot])
    if not spot.after(data_frame) and not spot.down(data_frame):
        return path, None
    else:
        go_right = path + spot.after(data_frame)
        go_down = path + spot.down(data_frame)
        if go_right and go_down:
            if go_down < go_right:
                down_spot = [spot.row +1, spot.col]
                return(go_down, [down_spot])
            elif go_right < go_down:
                right_spot = [spot.row, spot.col +1]
                return(go_right, [right_spot])
            else:
                down_spot = [spot.row +1, spot.col]
                right_spot = [spot.row, spot.col +1]
                m,options = compare_paths(Datapoint(down_spot[0],down_spot[1]),path,data_frame)
                n,options2 = compare_paths(Datapoint(right_spot[0],right_spot[1]),path,data_frame)
                if m > n:
                    return n,options2
                elif n > m:
                    return m, options
                else:



if __name__ == '__main__':
    print(find_all_paths())