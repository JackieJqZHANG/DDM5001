# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:40:43 2020

@author: ZJQ
"""
f = open("blocklist.xml")
numline = 0
line = f.readline()  
while(line): 
    numline+=1
    if '@' in  line:
        p = line
        pl = p.split()
        #print(line)
        for i in pl:
            if len(i)>=3 and i[0:3] == 'id=':
                if i.find('@')>4 and i.find('/')==-1 and i.find('\ ')==-1 and i.find('^')==-1:
                  print(line)  
    line = f.readline()  
