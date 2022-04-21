from lib.file_handler import FileHandler

MOVE_MAP = {"up":"depth","down":"depth","forward":"horizontal"}

def move(data):
    data = [{i.split(' ')[0]:int(i.split(' ')[1])} for i in data]
    position = {"depth":0,"horizontal":0}
    for move in data:
        for move_type, length in move.items():
            if move_type == "down":
                position[MOVE_MAP[move_type]] -= length
            else:
                position[MOVE_MAP[move_type]] += length
    return abs(position["depth"] * position["horizontal"])

if __name__ == '__main__':
    data = FileHandler('input.txt').content_by_lines()
    print(move(data))