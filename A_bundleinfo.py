bundle = "3.1(2f)"
bundlefile = "3.1.2f"
fout = open('r_Infrastructure_Bundles_in_3-1-2f.xml', 'w')
array = []
temp = []
readin = open('testAbundle.txt', 'r')
for line in readin:
    temp = line.strip()  # removes extra whitespaces
    array.append(temp)
print (array)
fout.write ('<?xml version="1.0" encoding="UTF-8"?>\n')
fout.write ('<!DOCTYPE reference PUBLIC "-//CISCO//DTD DITA 1.2 Reference v1.0//EN" "cisco-reference.dtd" []>\n')
fout.write ('<reference xml:lang="en_US">\n')
fout.write ("<title>SWT Unified Computing System (UCS) Infrastructure Software Bundle for " + bundle + "</title>\n")
fout.write ("<refbody><section>\n")
fout.write ("<title>UCS-FI-6332 and UCS-FI-6332 16UP</title>\n")
fout.write ("<p>ucs-6300-k9-bundle-infra." + bundlefile + ".A.bin contains the following images:</p>\n")
fout.write ("<ul>\n")
fout.write ("<li><p>" + array[16] + "</p></li>\n")
fout.write ("<li><p>" + array[17] + "</p></li>\n")
fout.write ("<li><p>" + array[18] + "</p></li>\n")
fout.write ("<li><p>" + array[19] + "</p></li>\n")
fout.write ("<li><p>" + array[20] + "</p></li>\n")
fout.write ("</ul>\n")
fout.write ("<title>UCS-FI6248UP and UCS-FI6296UP</title>\n")
fout.write ("<p>ucs-k9-bundle-infra." + bundlefile + ".A.bin contains the following images:</p>\n")
fout.write ("<ul>\n")
fout.write ("<li><p>" + array[9] + "</p></li>\n")
fout.write ("<li><p>" + array[10] + "</p></li>\n")
fout.write ("<li><p>" + array[11] + "</p></li>\n")
fout.write ("<li><p>" + array[12] + "</p></li>\n")
fout.write ("</ul>\n")
fout.write ("<title>UCS-FI-6324</title>\n")
fout.write ("<p>ucs-mini-k9-bundle-infra." + bundlefile + ".A.bin contains the following images:</p>\n")
fout.write ("<ul>\n")
fout.write ("<li><p>" + array[2] + "</p></li>\n")
fout.write ("<li><p>" + array[3] + "</p></li>\n")
fout.write ("<li><p>" + array[4] + "</p></li>\n")
fout.write ("<li><p>" + array[5] + "</p></li>\n")
fout.write ("</ul></section></refbody></reference>\n")
fout.close()

# Debugging print statements
# print ('<?xml version="1.0" encoding="UTF-8"?>')
# print ('<!DOCTYPE reference PUBLIC "-//CISCO//DTD DITA 1.2 Reference v1.0//EN" "cisco-reference.dtd" []>')
# print ('<reference xml:lang="en_US">')
# print ("<title>SWT Unified Computing System (UCS) Infrastructure Software Bundle for " + bundle + "</title>")
# print ("<refbody><section>")
# print ("<title>UCS-FI-6332 and UCS-FI-6332 16UP</title>")
# print ("<p>ucs-6300-k9-bundle-infra." + bundlefile + ".A.bin contains the following images:</p>")
# print ("<ul>")
# print ("<li><p>" + array[16] + "</p></li>")
# print ("<li><p>" + array[17] + "</p></li>")
# print ("<li><p>" + array[18] + "</p></li>")
# print ("<li><p>" + array[19] + "</p></li>")
# print ("<li><p>" + array[20] + "</p></li>")
# print ("</ul>")
# print ("<title>UCS-FI6248UP and UCS-FI6296UP</title>")
# print ("<p>ucs-k9-bundle-infra." + bundlefile + ".A.bin contains the following images:</p>")
# print ("<ul>")
# print ("<li><p>" + array[9] + "</p></li>")
# print ("<li><p>" + array[10] + "</p></li>")
# print ("<li><p>" + array[11] + "</p></li>")
# print ("<li><p>" + array[12] + "</p></li>")
# print ("</ul>")
# print ("<title>UCS-FI-6324</title>")
# print ("<p>ucs-mini-k9-bundle-infra." + bundlefile + ".A.bin contains the following images:</p>")
# print ("<ul>")
# print ("<li><p>" + array[2] + "</p></li>")
# print ("<li><p>" + array[3] + "</p></li>")
# print ("<li><p>" + array[4] + "</p></li>")
# print ("<li><p>" + array[5] + "</p></li>")
# print ("</ul></section></refbody></reference>")