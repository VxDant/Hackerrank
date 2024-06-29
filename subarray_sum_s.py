def find_sum(array, n, s):
    # we will be using sliding window technique
    #lets expand the window first and then shrink it

    left_index = 0
    right_index = 0
    current_sum = 0

    # lets expand the window first 
    for right_index in range(n):
        current_sum += array[right_index]   

        while current_sum > s and left_index <= right_index:
            current_sum -= array[left_index]
            left_index += 1

        if current_sum == s:
            print(left_index, right_index)
            return (left_index,right_index)
    return(-1,-1)



print(find_sum([1, 2, 3, 7, 5], 5, 12))
print("++++++++++++++++")
print(find_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15))
