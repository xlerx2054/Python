lst = []
def pattern(num):
    # traverse through the elements
    # in n assuming it as a string
    for i in num:
 
        # print | for every line
        lst.append("|")
 
        # print i number of * s in
        # each line
        lst.append("*" * int(i))
    return lst
print(pattern('1322'))
