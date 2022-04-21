def wash_till_clean(data):
    pos1 = list(range(len(data)-1))
    pos2 = list(range(1,len(data)))
    for p2 in pos2:
        for p1 in pos1:
            if not data[p1] < data[p2]:
                data[p1],data[p2] = data[p2],data[p1]
    return data



if __name__ == '__main__':
    data = [3,4,6,1,99,8,7,33]
    print(wash_till_clean(data))







































