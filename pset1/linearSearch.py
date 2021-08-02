def simpleSearch(ls,num):

    for i in range (len(ls)):
        if ls[i] == num:
            return i

    return -1

test_list = [1,2,3,4,5,6]
x = 6

print(simpleSearch(test_list,6))
