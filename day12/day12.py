from lib.file_handler import FileHandler


def _find_all_caves():
    data = [i.split("\n") for i in FileHandler('input.txt').str_content_to_list()][0]
    data = [i.split("-") for i in data]
    all_caves = []
    for i in data:
        all_caves.extend(i)
    all_caves = set(all_caves)
    move_map = {i: [] for i in all_caves}
    for pair in data:
        try:
            move_map[pair[0]].append(pair[1])
            move_map[pair[1]].append(pair[0])
        except Exception as e:
            pass
    return move_map

class Cave:
    def __init__(self,value):
        self.value = value

    def cave_type(self):
        if self.value.capitalize() == self.value:
            self.type = "big"
        else:
            self.type = "small"
        return self.type

    def linked_caves(self,cave_map):
        return cave_map[self.value]

    def _if_start(self):
        return self.value == "start"

    def _if_end(self):
        return self.value == "end"

def find_all_paths():
    all_caves = _find_all_caves().keys()
    cave_map = _find_all_caves()
    all_paths = []
    cave = Cave("start")
    path = ""
    while not cave._if_end():
        path = path + cave.value
        linked_caves = iter(cave.linked_caves(cave_map))
        path = ','.join([path,cave.value])
        all_paths.append(path)
    cave = Cave(next(linked_caves))
    return all_paths

if __name__ == '__main__':
    print(find_all_paths())