def sort_list(myList):
    list = []
    list.extend(myList)
    n = len(list)
    i = 0
    j = 1
    while i < n:
        while j < n:
            if list[j] > list[j+i]:
                temp = list[j]
                list[j] = list[j+i]
                list[j+i] = temp
            j+=1    
        i+=1        
    return list
