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
    array = line.split(delimiter)
    # print (temp)
    # print (line)
    # array.append(line)
    print (array)
    print (array[0])
    print (array[1])
    print (array[1])
    print (array[2])
    print (array[2])
    print (array[2])

    
