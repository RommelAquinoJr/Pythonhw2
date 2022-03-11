def sort_list(myList):
    list = []
    list.extend(myList)
    n = len(list)
    i = 0
    j = 0
    while i < n:
        while j < n-i:
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
            j+=1    
        i+=1        
    return list
