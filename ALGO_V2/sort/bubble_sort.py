# every loop the end elment should be sorted
# we also need an indicator to see all swapped or not, if in one loop there is no wap action needed, we will just stop

def bubble_sort(list):
    swap = True
    sorted_num = 0

    while swap:
        swap = False
        print(list)
        for i in range(0, len(list) - sorted_num -1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                print(list)
                swap = True
        sorted_num += 1
    return list, sorted_num

print(bubble_sort([10, 3, 2, 1, 9, 8]))
