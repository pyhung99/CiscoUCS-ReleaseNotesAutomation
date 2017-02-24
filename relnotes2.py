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
def find_fba(k):
    delimiter = ' '
    fba = k.split(delimiter)
    if len(k) > 8:
        # print ('Length is great than 8 and so this internal build number must be discarded.')
        fba = sorted(fba)
        print (fba[0])
        x = fba[0]
        # print ('=== String Length ===') 
        # print (len(i[2]))
        return x
    # else:
    #     print ('This build value is ok.')
        # return x
x = []
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
    print ('Resolved in: 3.1(2f)')
    # find_fba(i[2])
    # i[2] = x
    # print (x)
    # print ('=== String Length ===') 
    # print (len(i[2]))
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

