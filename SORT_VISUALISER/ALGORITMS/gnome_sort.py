
def algorithm(array,function):
    i = 0
    while i < len(array):
        if i == 0 or array[i] >= array[i-1]:
            i += 1
        else:
            array[i], array[i-1] = array[i-1], array[i]
            #visualise the sorting
            function(i-1)
            i -= 1