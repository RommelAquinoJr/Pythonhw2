def sort_list(myList):
    list = []
    list.extend(myList)
    n = len(list)
    i = 0
    j = 1
    while i <= n-1:
        while j < n:
            if list[i] > list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
            j+=1
        i+=1
    return list
