#
def quick_sort(list, start=0, end=None, pivot = 0):
    if len(list) <= 1:
        return list
    # pivot is the left most of the
    left_cursor = start
    right = end if end else len(list) - 1

#    need to find the index to swap with the pivot to seperate to two part


    quick_sort(list, start, pivot)
    quick_sort(list, pivot)
