def sort_list(myList):
    list = []
    list.extend(myList)
    i = 0
    n = 1
    while n <= len(list) - 1:
        #while n <len(list):
        if list[i] > list[n]:
            temp = list[n]
            list[n] = list[i]
            list[i] = temp
        #    n+=1
        i = i+1
        n = n+1
    return list
    
