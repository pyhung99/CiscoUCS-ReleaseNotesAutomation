# This script filters through the nightly engineering builds for UCS Manager and finds the first bundle affected for a logged defect.

# test2 = '3.1(9.999)A 2.2(8f)AS9 3.1(2e)AS9 3.1(2)BS99' 
# small testcase passes

test3 = '3.1(1.99a) 3.1(2.99)A 3.1(3.99b) 3.1(4.99)A 3.1(5.99)T 3.1(6.99c) 3.1(7.99)A 2.2(8d)AS9 2.2(8e)A 3.1(2e)AS99 2.2(3i)B'
# Larger testcase passes now too 2.2(8e)A build and 2.2(3i)B released builds are the final 2 builds that should appear.
# After sorting the last 2 results, only 2.2(3i)B which is the lowest build should be returned.
print ('This is the list of builds to search through:  ' + str(test3))
delimiter = ' '
arr2 = test3.split(delimiter)
x = []
y = []
for i in range(len(arr2)):
    # print (i)
    if len (arr2[i]) < 9:
        y.append(arr2[i])
        # print (y)
y.sort()
print ('Verify that builds are filtered and sorted:    ' + str(y))
print ('The first bundle affected for this defect is:  ' + str(y[0]) )

# Possible returned output checks below:
# print (y)
# print (arr2)
# print (type (arr2[0])) ## shows type inside the array which is a string
# arr2.pop(i)
# print (len(arr2))
# print (arr2)
# print (arr2[0])
# print (len (arr2[0]))
# print (arr2[1])
# print (len (arr2[1]))