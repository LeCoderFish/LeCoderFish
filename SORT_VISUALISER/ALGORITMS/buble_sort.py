
def algorithm(array,function):
    swap = False
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
                #visualise the sorting
                function(j, j+1)
        if swap == False:
            break