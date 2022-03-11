def sort_list(myList):
    list = myList
    n = len(list)
    i = 0
    j = 1
    while i < n - 1:
        while j < n:
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                lst[j] = temp
            j+=1
        i+=1
    return list
