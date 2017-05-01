#!/usr/bin/python3

#scrapper tool for python

import sys

file = open("shares.txt")
t=file.readlines()
k = int(sys.argv[1])
list1 = []
for l in t:
	if(len(list1) >= k):
		break
	# print("test : "+l)
	l=l.replace(' ','')
	# print("test : "+l)
	l=l.replace('=','')
	# print("test : "+l)
	try:
		l=int(l)
		list1.append(l)
	except:
		continue
file2 = open("for_combine.txt","w")
for x in list1:
	file2.write(str(x)+"\n")

file.close()
file2.close()