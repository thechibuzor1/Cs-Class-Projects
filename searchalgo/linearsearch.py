def linearsearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


emp = [10,20,30,40]


def linear_delete(array, value):
    pos = linearsearch(array, value)
    if pos == -1:
       return array--
    for i in range(pos, len(array)):
        array[i] = array[i+1]
        
        
        
        
        
        