# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:57:53 2020

@author: ZJQ
"""


import os
f = open("blocklist.xml")
numline = 0
line = f.readline()  
while(line): 
    numline+=1
    #print(numline)
    if 'blockID' in line:
        ll = line
        p = ll.find('blockID')
        if (ll[p+9]=='i' or ll[p+9]=='g') and ll[ll.find('"',p+9)-1].isdigit():
            print(line)
    line = f.readline() 
f.close()
# tree = ET.parse('D:/DDMstudy/tools/1/blocklist.xml')
# root = tree.getroot()\

# for elem in tree.iter():
#     if 'blockID' in elem.attrib:
#         tmp = elem.attrib
#         if (tmp['blockID'][0]=='i' or tmp['blockID'][0]=='g') and tmp['blockID'][-1].isdigit():
#             kk = elem
#             print(elem.attrib)
