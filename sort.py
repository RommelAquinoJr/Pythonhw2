def sort_list(myList):
    list = myList
    n = len(list)
    i = 0
    j = 0
    while i < n:
        while j < n-i-1:
            if list[i] > list[n]:
                temp = list[i]
                list[i] = list[n]
                lst[n] = temp
            j+=1
        i+=1
    return list
