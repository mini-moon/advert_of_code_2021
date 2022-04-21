from pprint import pprint

from pandas import DataFrame

from lib.data_handler import Datapoint
from lib.file_handler import FileHandler
import itertools as it

class Board:
    def __init__(self,data):
        self.data = data
        self.cols = list(range(0,len(data[0])))
        self.rows = list(range(0,len(data)))

    def size(self):
        pos_map = []
        for c in self.cols:
            for r in self.rows:
                pos_map.append((c,r))
        return pos_map

    def data_frame(self):
        return DataFrame(self.data, index=self.rows,columns=self.cols)

    def col_as_board(self):
        col_list = {col:[] for col in self.cols}
        for c in self.cols:
            for pos in self.size():
                r_of_e = pos[0]
                c_of_e = pos[1]
                if c_of_e == c:
                    col_list[c].append(Datapoint(r_of_e,c_of_e).value(self.data_frame()))
        return list(col_list.values())


def get_boards(data):
    n = 5
    boards = list(it.zip_longest(*[iter(data)] * n))
    new_boards = []
    for b in boards:
        new_line = []
        for line in b:
            new_line.append([int(i) for i in line.strip(" ").split(" ")])
        new_boards.append(new_line)
    return new_boards

def board_as_cols(board):
    col_c = Board(board).col_as_board()
    return col_c

def board_as_rows(board):
    row_c = Board(board).data
    return row_c

def get_board_map(board):
    board_recorder = []
    for collection in board:
        new_col = [{i:-1} for i in collection]
        board_recorder.append(new_col)
    return board_recorder

def call_nums(bingo_nums,r_b,c_b):
    num_win = None
    for num_called in bingo_nums:
        for m in r_b + c_b:
            m_values = []
            for i in m:
                for k,v in i.items():
                    if k == num_called[1]:
                        i[k] = num_called[0]
                    m_values.extend(list(i.values()))
                    num_win = num_called[1]
            if all(i > -1 for i in m_values) and len(m_values)==5:
                print("bingo",num_win)
                print("bingo_board",r_b,c_b)
                return num_win


def get_score_board(board,score_board):
    new_board = []
    for item in board:
        for map in score_board:
            map_c = []
            for i in map:
                map_c.extend(list(i.keys()))
            if item == map_c:
                new_board.append(map)
    unmarked = []
    for i in new_board:
        for m in i:
            for k,v in m.items():
                if v == -1:
                    unmarked.append(k)
    return sum(unmarked)



if __name__ == '__main__':
    data = FileHandler('input.txt').raw_content()
    bingo_nums = list(enumerate([int(i) for i in data.split("\n")[0].split(",")],start=0))
    print(bingo_nums)
    boards = [i.replace("  "," ") for i in data.split("\n")[1:] if i != '']
    boards = get_boards(boards)
    for board in boards:
        r_b = board_as_rows(board)
        c_b = board_as_cols(board)
        r_score_board = get_board_map(r_b)
        c_score_board = get_board_map(c_b)
        final = None
        if call_nums(bingo_nums,r_score_board,c_score_board):
            new_board = get_score_board(board, r_score_board)
            final = new_board * call_nums(bingo_nums,r_score_board,c_score_board)
            break
        print(final)




