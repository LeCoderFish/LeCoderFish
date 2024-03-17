def algorithm(array, L = None, H = None):
        if L is None and H is None:
            L = 0
            H = len(array)-1
        if (array[L] > array[H]):
            array[L], array[H] = array[H], array[L]
            #visualise the sorting
            yield L, H
        if H-L >= 2:
            X = int((H-L+1)/3)
            yield from algorithm(array,L, H-X)
            yield from algorithm(array,L+X, H)
            yield from algorithm(array,L, H-X)