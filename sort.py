def sort_list(myList):
    list = myList
    n = len(list)
    i = 0
    while i < n:
        while n-i-1 < n:
            if list[i] > list[n]:
                temp = list[i]
                list[i] = list[n]
                lst[n] = temp
            n-=1
        i+=1
    return list
