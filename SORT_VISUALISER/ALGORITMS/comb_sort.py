def algorithm(array,function):
        n = len(array)
        gap = n
        swapped = True
        while swapped is True:
            gap = int(gap/1.3)
            if gap <= 1:
                swapped = False
                gap = 1
            for i in range(n-gap):
                if  array[i] > array[i+gap]:
                    array[i], array[i+gap] = array[i+gap], array[i]
                    swapped = True
                    #visualise the sorting
                    function(i, i+gap)