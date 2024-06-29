

arr = [1,2,3,4,5]
n = 5



def countTriplet(arr, n):
	    
    left_index = 0 
    
    element_set = set(arr)
    
    counter = 0
    
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i]+ arr[j]) in element_set:
                print(arr[i], arr[j])



countTriplet(arr,n)