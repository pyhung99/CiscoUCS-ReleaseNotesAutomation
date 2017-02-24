# with open("test1.csv") as f:
#     content = f.readlines()
# # to remove whitespace characters at the end of each line
# content = [x.strip() for x in content] 
# print (content)

# with open("test1.csv", "r") as ins:
#     array = []
#     for line in ins:
#         array.append(line)
#         print (array)
#         print ("\n" + "\n")
array = []
temp = []
readin = open('test1.csv', 'r')
for line in readin:
    delimiter = ','
    temp = line.strip().split(delimiter)  # removes extra whitespaces then splits each cell into the array
    array.append(temp)
# print (array[0])
# print (array[1])
# print (array[2])
for i in array:
    print ("===========================")
    # print (len(i))
    print ('Defect:      ' + i[0])
    print ('Description: ' + i[1])
    print ('FBA:         ' + i[2])
    # print ('              String Length==') 
    # print (len(i[2]))
    print ('Resolved in: 3.1(2f)')
    # for j in i:
    #     print ("the length of array j is")
    #     print (len(j))
    #     print (j)
    #     print ("\n")
        # print (len(j))
        # print ('DEFECT = ' + j[0])
        # print ('Description = ' + j[1])
        # print ('FBA = ' + j[2])
        # print ('Fixed in: 3.1(2f)')
    # print (i)
    # print ("\n")
