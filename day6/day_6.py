from pprint import pprint

from lib.file_handler import FileHandler

if __name__ == '__main__':
    fishes = [int(fish) for fish in FileHandler("input.txt").str_content_to_list()]
    days = list(range(0,256+1))
    daily_fishes = {day:[] for day in days}
    for day in days:
        if day >=1:
            day_fishes = []
            counter = 0
            previous_day = day -1
            for fish in daily_fishes[previous_day]:
                if fish >=1:
                    day_fishes.append(fish -1)
                elif fish==0:
                    day_fishes.append(fish +6)
                    counter +=1
                else:
                    continue
            for c in list(range(0,counter)):
                day_fishes.append(8)
            daily_fishes[day] = day_fishes
        else:
            daily_fishes[day] = fishes
    print(len(daily_fishes[days[-1]]))
