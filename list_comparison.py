y = [1, 2, 3, 4,5]
x = [5, 6, 7, 8, 9]
def list_comp(a,b): #comparing two list to see if one of the element is in the other list.
    for arr in a: 
        for brr in b:
            if arr == brr:
                print("Yes")
                return 
                break
        else:
            print("No")
            return
        
list_comp(x,y)