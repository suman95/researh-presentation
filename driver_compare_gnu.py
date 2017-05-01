#!/usr/bin/python3
# driver function for generating simulation results

import subprocess
import time
import random
import math
import matplotlib.pyplot as plt

# running ecdsa
list1_x = []
list1_y = []
list2_x = []
list2_y = []
list3_x = []
list3_y = []

k = 1
for i in range(100):
	start_time= time.time()
	st = "./hmac "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	k += 4
	print("{0}  {1}".format(k, (time.time() - start_time)+(0.0014*k)))
	list1_x.append((k-1)/4)
	list1_y.append((time.time() - start_time)+(0.0014*k))


# running ecdsa
k = 1
for i in range(100):
	start_time= time.time()
	st = "./ecdsa "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	k += 4
	print("{0}  {1}".format(k, time.time() - start_time))
	list2_x.append((k-1)/4)
	list2_y.append(time.time() - start_time)


# running hmac without overhead
k = 1
for i in range(100):
	start_time= time.time()
	st = "./hmac "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	st = "./sharing_initial.py "+str(int(math.floor(k/10.0)))
	subprocess.call(st, stdout=False, shell=True)
	k += 4
	print("{0}  {1}".format(k, time.time() - start_time))
	list3_x.append((k-1)/4)
	list3_y.append(time.time() - start_time)


# k = 1
# for i in range(100):
# 	f = random.random()
# 	# k1 = int(round(f*k))
# 	# k2 = int(round((1-f)*k))
# 	k1 = int(round(0.3*k))
# 	k2 = int(round(0.7*k))
# 	print(k1,k2)
# 	start_time= time.time()
# 	st = "./ecdsa "+str(k)
# 	subprocess.call(st, stdout=False, shell=True)
# 	st = "./hmac "+str(k1)
# 	subprocess.call(st, stdout=False, shell=True)
# 	k += 5
# 	print("{0}  {1}".format(k, (time.time() - start_time)+(0.004*k1)))
# 	list3_x.append(k-1)
# 	list3_y.append((time.time() - start_time)+(0.004*k1))

file = open("protocol_compare.dat","w")
for i in range(len(list1_x)):
	strin = str(list1_x[i])+" "+str(list1_y[i])+" "+str(list2_y[i])+" "+str(list3_y[i])+"\n"
	file.write(strin)
file.close()

