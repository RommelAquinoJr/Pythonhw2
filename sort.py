def sort_list(myList):
    list = []
    list.extend(myList)
    i = 0
    n = 1
    while i < len(list):
        while n <len(list):
            if i > n:
                temp = list[n]
                list[n] = list[i]
                list[i] = temp
            n+=1
        i+=1
    return list
