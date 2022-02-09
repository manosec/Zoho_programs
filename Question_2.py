def func(list1, l, r):
    if list1[l-1] == 1 and list1[r-1] == 4:
        reverse = list1[::-1]
        return reverse
    
    elif list1[l-1] == 2 and list1[r-1] == 4:
        ch = list1[l-1]
        list1[l-1] = list1[r-1]
        list1[r-1] = ch
        return list1
    
print(func([1,6,7,4],1, 4))    
print(func([1,2,3,4,5,6,7], 2, 4))














    