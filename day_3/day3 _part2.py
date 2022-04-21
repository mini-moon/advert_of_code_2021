from pprint import pprint

from lib.file_handler import FileHandler

#
# def calc_bits(data):
#     mark_map = {}.fromkeys(list(range(0,len(data[0]))))
#     collection = data.copy()
#     for i in mark_map.keys():
#         mark_map[i] = {1:0,0:0}
#         for line in data:
#             if int(line[i]) ==1:
#                 mark_map[i][1] +=1
#             else:
#                 mark_map[i][0] +=1
#     rate_map = {k:{'epsilon': None,'gamma':None} for k in mark_map.keys()}
#     for k, item in mark_map.items():
#         for s_k,v in item.items():
#             print(s_k,v)
#             if v == max(item.values()):
#                 rate_map[k]["gamma"]=s_k
#             else:
#                 rate_map[k]["epsilon"]=s_k
#     for index in list(rate_map.keys()):
#         for i in collection:
#             if not i[index] == str(rate_map[index]['gamma']):
#                 collection.remove(i)
#                 print(collection)
#     return collection
def _get_max_and_min(data):
    mark_map = {}.fromkeys(list(range(0,len(data[0]))))
    for i in mark_map.keys():
        mark_map[i] = {1:0,0:0}
        for line in data:
            if int(line[i]) ==1:
                mark_map[i][1] +=1
            else:
                mark_map[i][0] +=1
    return mark_map

def keep_majority(data):
    positions = list(range(0,len(data[0])))
    rounds = list(range(0,len(data[0])+1))
    oxgen_items=data.copy()
    for m in rounds:
            for p in positions:
                if not len(oxgen_items) ==1:
                    mark_map = _get_max_and_min(oxgen_items)
                    # print("index",p,"items",oxgen_items)
                    for i in oxgen_items:
                        for k,v in mark_map[p].items():
                            max_ks = [k for k,v in mark_map[p].items() if v ==max(mark_map[p].values())]
                            if len(max_ks) == 1:
                                max_k = max_ks[0]
                                if v == max(mark_map[p].values()):
                                    max_k = k
                            else:
                                max_k = 1
                            for d in oxgen_items:
                                if int(d[p]) == max_k:
                                    continue
                                else:
                                    # print("to remove:", d)
                                    oxgen_items.remove(d)
                else:
                    return oxgen_items[0]

def keep_minority(data):
    positions = list(range(0,len(data[0])))
    rounds = list(range(0,len(data[0])+1))
    co2_items=data.copy()
    for m in rounds:
            for p in positions:
                if not len(co2_items) ==1:
                    mark_map = _get_max_and_min(co2_items)
                    print("index",p,"items",co2_items)
                    for i in co2_items:
                        for k,v in mark_map[p].items():
                            max_ks = [k for k,v in mark_map[p].items() if v ==min(mark_map[p].values())]
                            if len(max_ks) == 1:
                                max_k = max_ks[0]
                                if v == min(mark_map[p].values()):
                                    max_k = k
                            else:
                                max_k = 0
                            for d in co2_items:
                                if int(d[p]) == max_k:
                                    continue
                                else:
                                    # print("to remove:", d)
                                    co2_items.remove(d)
                else:
                    return co2_items[0]



def binary_to_int(num):
    return int(num,2)



if __name__ == '__main__':
    data = FileHandler('input.txt').content_by_lines()
    result = binary_to_int(keep_minority(data)) * binary_to_int(keep_majority(data))
    print(result)