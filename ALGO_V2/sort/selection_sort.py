#  for every loop of the list, the end of the selection sort will be sorted
def selection_sort(list):
    start_idx = 0 # the start of the unsorted part
    while start_idx < len(list) - 1:
        smallest_idx = start_idx
        for j in range(start_idx, len(list)):
            if list[j] < list[smallest_idx]:
                smallest_idx = j
        list[start_idx], list[smallest_idx] = list[smallest_idx], list[start_idx]
        start_idx += 1
    return list
# can just change the
before = [9,10,4,5,6,7, 0]
after = selection_sort(before)
print(after)
