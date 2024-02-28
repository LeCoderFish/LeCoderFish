def algorithm(array,function, L = None, H = None):
        if L is None and H is None:
            L = 0
            H = len(array) - 1
        if (array[L] > array[H]):
            array[L], array[H] = array[H], array[L]
            #visualise the sorting
            function(L, H)
        if H-L >= 2:
            X = int((H-L+1)/3)
            algorithm(array,function,L, H-X)
            algorithm(array,function,L+X, H)
            algorithm(array,function,L, H-X)