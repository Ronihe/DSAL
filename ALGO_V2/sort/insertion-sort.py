
def insertion_sort(list):

    for i in range(1, len(list)):
        current_value = list[i]
        pointer_idx = i
        while list[pointer_idx -1] > current_value and pointer_idx >0:
        #     move to the next position
            list[pointer_idx] = list[pointer_idx -1]
            pointer_idx -= 1
        list[pointer_idx] = current_value

    return list
test = [5,7,8,3,1,5,3]
sorted =  insertion_sort(test)
print(sorted)