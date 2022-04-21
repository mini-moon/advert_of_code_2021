from lib.file_handler import FileHandler

def sum_chars(data):
    data = [int(i) for i in data]
    counter = 0
    map = {}
    for index in list(range(0,len(data)-2)):
        map[index]=data[index]+data[index+1]+data[index+2]
        if index >0 and map[index] > map[index-1]:
            counter +=1
    return counter


if __name__ == '__main__':
    data = FileHandler('input.txt').content_by_lines()
    print(sum_chars(data))