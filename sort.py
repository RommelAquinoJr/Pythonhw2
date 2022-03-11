def sort_list(list):
    list = []
    list.extend(myList)
    i = 0
    n = 1
    while i < len(list):
        #while n <len(list):
        if list[i] > list[n]:
            temp = list[n]
            list[n] = list[i]
            list[i] = temp
        #    n+=1
        i = i+1
        n = n+1
    return list
