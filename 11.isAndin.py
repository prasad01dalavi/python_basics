string = "abcde"
if 'a' in string:           # a is in string or not. if it is present then true
    print 'yes! a in string'

if 'ab' in string:
    print 'yes! ab in string'

myList1 = [1, 2, 3]
myList2 = [1, 2, 3]
if myList1 is myList2:      # it is not similar to == so this if will not execute
    print 'Yes! my two list are having same contents'

anotherlist1 = anotherlist2 = [1, 2, 3]
if anotherlist1 is anotherlist2:  # but it is similar to ==
    print 'This works actually!'
