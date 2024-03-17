def algorithm(array, temp_array = [], index = 0):
        if temp_array == []:
            temp_array = array.copy()

        if len(temp_array) > 1:
            m = len(temp_array)//2
            left = temp_array[:m]
            right = temp_array[m:]

            yield from algorithm(array,left, index)
            yield from algorithm(array,right, index+m)

            #i - index of left array, j - index of right array, k - index of temp merged array
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    if array[index] != left[i]:
                        array[index], array[index-j+m] = left[i], array[index]
                        yield index, index-j+m
                    else:
                        array[index] = left[i]
                    temp_array[k] = left[i]
                    i += 1
                else:
                    array[index], array[index-i+m] = right[j], array[index]
                    yield index,index-i+m
                    temp_array[k] = right[j]
                    j += 1
                #visualise the sortingm+k
                index += 1
                k += 1

            while i < len(left):
                array[index] = left[i]
                temp_array[k] = left[i]
                #visualise the sorting
                index += 1
                i += 1
                k += 1

            while j < len(right):
                array[index] = right[j]
                temp_array[k] = right[j]
                #visualise the sorting
                index += 1
                j += 1
                k += 1