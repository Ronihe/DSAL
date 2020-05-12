# three steps:
# 1. split the unsorted the list to half until there is only element or none per group
# 2. merge the two splitted groups into one
# 3. repeat the above two steps

def merge_sort(list):
    if len(list) <= 1:
        return list

    #     split
    mid = len(list) // 2
    sublist_left = list[:mid]
    sublist_right = list[mid:]
    return merge(merge_sort(sublist_left), merge_sort(sublist_right))


def merge(left, right):
    print(left, right)
    left_cursor, right_cursor = 0, 0
    merged = []
    while left_cursor < len(left) and right_cursor < len(right):
        # sort each one and place into the result
        left_val = left[left_cursor]
        right_val = right[right_cursor]
        if left_val <= right_val:
            merged.append(left_val)
            left_cursor += 1
        else:
            merged.append(right_val)
            right_cursor += 1

    # dont not forget to
    merged.extend(left[left_cursor:])
    merged.extend(right[right_cursor:])
    return merged


test = [1, 2, 3, 8, 100, -100, 0, 0]
merge_sort_list = merge_sort(test)
print(merge_sort_list)
