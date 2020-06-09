# https://www.lintcode.com/problem/first-unique-character-in-a-string/description?_from=ladder&&fromId=1

def first_unique_char(str):
    counter = {}
    for c in str:
        counter[c] = counter.get(c, 0) + 1

    for c in str:
        if counter[c] == 1:
            return c
