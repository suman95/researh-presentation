#!/usr/bin/python3
# driver function for generating simulation results

import subprocess
import time
import random
import matplotlib.pyplot as plt

# running ecdsa
list1_x = []
list1_y = []
list2_x = []
list2_y = []
list3_x = []
list3_y = []

k = 1
for i in range(200):
	start_time= time.time()
	st = "./hmac "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	k += 2
	print("{0}  {1}".format(k, (time.time() - start_time)+(0.0014*k)))
	list1_x.append(k-1)
	list1_y.append((time.time() - start_time)+(0.0014*k))


# running dsa
k = 1
for i in range(200):
	start_time= time.time()
	st = "./ecdsa "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	k += 2
	print("{0}  {1}".format(k, time.time() - start_time))
	list2_x.append(k-1)
	list2_y.append(time.time() - start_time)


k = 1
for i in range(200):
	f = random.random()
	# k1 = int(round(f*k))
	# k2 = int(round((1-f)*k))
	k1 = int(round(0.3*k))
	k2 = int(round(0.7*k))
	print(k1,k2)
	start_time= time.time()
	st = "./ecdsa "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	st = "./hmac "+str(k1)
	subprocess.call(st, stdout=False, shell=True)
	k += 2
	print("{0}  {1}".format(k, (time.time() - start_time)+(0.0014*k1)))
	list3_x.append(k-1)
	list3_y.append((time.time() - start_time)+(0.0014*k1))


line1,=plt.plot(list1_x,list1_y,label="Protocol based on MAC")
line2,=plt.plot(list2_x,list2_y,label="Protocol based on ECDSA")
line3,=plt.plot(list3_x,list3_y,label="Priority based differential protocol")

# formating the graph
plt.grid(True)
plt.legend(handles=[line1,line2,line3],loc=1)
plt.title('Comparison of VANET message authentication schemes')
plt.xlabel('No. of Vehicles in simulation')
plt.ylabel('Time taken(s)')


# showing the graph
plt.show()
