def sort_list(myList):
    list = []
    list.extend(myList)
    n = len(list)
    i = n
    j = n-i-1
    while i > 0:
        while j >= 0:
            if list[i] < list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
            j-=1    
        i-=1        
    return list
