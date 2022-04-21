from lib.file_handler import FileHandler
CHAR_PAIRS = {"(":")","{":"}","[":"]","<":">"}
ILLEGAL_CHAR_POINTS = {")":3,"}":1197,"]":57,">":25137}
MISSING_CHAR_POINTS = {")":1,"}":3,"]":2,">":4}


def _check_full_data(data):
    broke_lines = []
    missing_chars_scores =[]
    for line in data:
        m = _check_if_match_char(line)
        if not m:
            pass
        elif _check_if_incomplete(m):
            chars_missing = _complete_line(line)
            score = _calc_missing_points(chars_missing)
            missing_chars_scores.append(score)
            print("incomplete line:", line,"score:",score)
        else:
            broke_lines.extend([i for i in m if i in CHAR_PAIRS.values()][0])
    middle_score = _find_middle_score(missing_chars_scores)
    print(sorted(missing_chars_scores))
    return middle_score


def _check_if_match_char(chars):
    bucket = []
    for char in chars:
        if bucket and char == CHAR_PAIRS.get(bucket[-1]):
            bucket = bucket[:-1]
        else:
            bucket.append(char)
    return bucket


def _check_if_incomplete(chars):
    m = _check_if_match_char(chars)
    if all(char in CHAR_PAIRS.keys() for char in m):
        return True
    else:
        return False

def _complete_line(chars):
    missing_elements = []
    if _check_if_incomplete(chars):
        chars_missing_end = _check_if_match_char(chars)
        for char in chars_missing_end[::-1]:
            missing_elements.append(CHAR_PAIRS[char])
    return missing_elements

def _calc_missing_points(chars):
    sum_of_missing_chars = 0
    for i in chars:
        sum_of_missing_chars = sum_of_missing_chars * 5 + MISSING_CHAR_POINTS[i]
    return sum_of_missing_chars

def _find_middle_score(scores):
    scores = sorted(scores)
    middle_point = len(scores)/2
    if len(scores)%2 == 1:
        middle_point -= 0.5
        return scores[int(middle_point)]
    else:
        return min(scores[int(middle_point)],scores[int(middle_point)-1])

if __name__ == '__main__':
    data = FileHandler("input.txt").content_by_lines()
    print(_check_full_data(data))
    # print(_find_middle_score([1,2,3,4]))

