def sort_list(myList):
    list = []
    list.extend(myList)
    n = len(list)
    i = 0
    j = 0
    while i < n:
        while j < n-i-1:
            if list[i] > list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
            j+=1    
        i+=1        
    return list
