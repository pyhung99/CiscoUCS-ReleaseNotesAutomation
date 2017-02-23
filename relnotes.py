test = 'CSCvc95647,CimcLowMem alert triggered due to KVM scriptable vmedia mount,3.1(2c)B'
# CSCvc89242,
# Description FI rebooted due to CDP hap reset,
# FBA 2.2(6e)A,
# Resolved in 3.1(2.191)A 2.2(8f)AS8 3.1(2e)AS8,
# Verified in 3.1(2.194)A

test2 = '3.1(2.191)A 2.2(8f)AS8 3.1(2e)AS8'		
## passes but needs string slicing to remove spin builds
## needs truncation of 'S' then digit 8

# test2 = '3.1(2.64)B 3.1(2.64)A 3.1(2b)B'  	
## only passes with reverse sorting
## 3.1(2.64)B converts to 3.1(3a) or next available released build
## since current patch build is 3.1(2f) discard the 3.1(3a) build as it is Granada MR2

# test2 = '3.1(2c)A 3.1(1e)A' 		## pass
# test2 = '3.1(2b)A 2.2(8c)A' 		## pass

#delimiter = ','
# arr = []
# arr = test.split(delimiter)
delimiter = ','
arr = test.split(delimiter)

delimiter = ' '
arr2 = test2.split(delimiter)
# arr2 = sorted(arr2, reverse=True) ### reverses the sorting
arr2 = sorted(arr2)

#fba = arr[2]

print ('DEFECT = ' + arr[0])
print ('Description = ' + arr[1])
print ('FBA = ' + arr2[0])
print ('Fixed in: 3.1(2f)')  ## Missing bundle build info A,B, or C?

# print (arr2)
# print (test)
# print ('     This string has '+ str(len(test)) + ' characters.')
# print ('This is the value of the array: ' + str(arr))
# print ('This is first array ' + arr[0] +
# 	' This is second array ' + arr[1] +
# 	' This is third array ' + arr[3] +
# 	' This is fourth array ' + arr[4]
# 	)
# print (len(test))
# print (' characters.')

# arr.append('CSCvc95647')
# print (arr)
# arr.append('CimcLowMem alert triggered due to KVM scriptable vmedia mount')
# print (arr)
# arr.append('3.1(2c)B')
# print (arr)
# arr.append('3.1(22a)S1,3.1(22a)S1')
# print (arr)