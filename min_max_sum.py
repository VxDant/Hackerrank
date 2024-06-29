arr = [1,2,3,4,5]

# we have to find min, max sum of 4 integers in the 5 integer array, so

arr.sort()

min_element = arr[0]
max_element = arr[4]

min_sum = sum(arr)- arr[4]
max_sum = sum(arr)- arr[0]

print(min_sum, max_sum)