# This script filters through the nightly engineering builds for UCS Manager and finds the first bundle affected for a logged defect.

# test2 = '3.1(2.191)A 2.2(8f)AS8 3.1(2e)AS8 3.1(2)BS18' 
# small testcase passes

test3 = '3.1(2.41a) 3.1(2.42)A 3.1(2.67b) 3.1(2.68)A 3.1(2.68)T 3.1(2.79c) 3.1(2.80)A 2.2(8d)AS2 2.2(8e)A 3.1(2e)AS11 2.2(3i)B'
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