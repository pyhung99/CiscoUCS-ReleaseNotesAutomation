bundle = "3.1(2f)"
bundlefile = "3.1.2f"
fout = open('r_C_Series_Server_SW_Bundle_3-1-2f.xml', 'w')
array = []
temp = []
readin = open('testCbundle.txt', 'r')
for line in readin:
    temp = line.strip()  # removes extra whitespaces
    array.append(temp)
print (array)
fout.write ('<?xml version="1.0" encoding="UTF-8"?>\n')
fout.write ('<!DOCTYPE reference PUBLIC "-//CISCO//DTD DITA 1.2 Reference v1.0//EN" "cisco-reference.dtd" [\n')
fout.write (')]>\n')
fout.write ('<reference xml:lang="en_US">\n')
fout.write ("<title>SWT Unified Computing System (UCS) Server Software (C-Series) for " + bundle + "</title>\n")
fout.write ("<refbody><section>\n")
fout.write ("<p>ucs-k9-bundle-c-series." + bundlefile + ".C.bin contains the following images:</p>\n")
fout.write ("<ul>\n")
for i in array:
    fout.write ("<li><p>" + i + "</p></li>\n")
fout.write ("</ul></section></refbody></reference>\n")
fout.close()

# Debugging print statements
# print ('<?xml version="1.0" encoding="UTF-8"?>\n')
# print ('<!DOCTYPE reference PUBLIC "-//CISCO//DTD DITA 1.2 Reference v1.0//EN" "cisco-reference.dtd" [\n')
# print (')]>\n')
# print ('<reference xml:lang="en_US">\n')
# print ("<title>SWT Unified Computing System (UCS) Server Software (C-Series) for " + bundle + "</title>\n")
# print ("<refbody><section>\n")
# print ("<p>ucs-k9-bundle-c-series." + bundlefile + ".C.bin contains the following images:</p>\n")
# print ("<ul>\n")
# for i in array:
#     print ("<li><p>" + i + "</p></li>\n")
# print ("</ul></section></refbody></reference>\n")