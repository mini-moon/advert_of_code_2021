from pprint import pprint

from lib.file_handler import FileHandler


def calc_bits(data):
    mark_map = {}.fromkeys(list(range(0,len(data[0]))))
    for i in mark_map.keys():
        mark_map[i] = {1:0,0:0}
        for line in data:
            if int(line[i]) ==1:
                mark_map[i][1] +=1
            else:
                mark_map[i][0] +=1
    print(mark_map.keys())
    rate_map = {k:{'epsilon': None,'gamma':None} for k in mark_map.keys()}
    for k, item in mark_map.items():
        for s_k,v in item.items():
            print(s_k,v)
            if v == max(item.values()):
                rate_map[k]["gamma"]=s_k
            else:
                rate_map[k]["epsilon"]=s_k
        print(rate_map)
    gamma_rate = ''.join([str(v['gamma']) for k,v in rate_map.items()])
    epsilon_rate = ''.join([str(v['epsilon']) for k,v in rate_map.items()])
    print(gamma_rate)
    return binary_to_int(gamma_rate) * binary_to_int(epsilon_rate)

def binary_to_int(num):
    return int(num,2)



if __name__ == '__main__':
    data = FileHandler('input.txt').content_by_lines()
    pprint(calc_bits(data))