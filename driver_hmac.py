#!/usr/bin/python3
# driver function for generating simulation results

import subprocess
import time
import matplotlib.pyplot as plt

# running ecdsa
list1_x = []
list1_y = []
list2_x = []
list2_y = []

# k = 1
# for i in range(50):
# 	start_time= time.time()
# 	st = "./ecdsa.py "+str(k)+" >in.txt"
# 	subprocess.call(st, stdout=False, shell=True)
# 	k += 10
# 	print("{0}  {1}".format(k, time.time() - start_time))
# 	list1_x.append(k)
# 	list1_y.append(time.time() - start_time)

# line_1, = plt.plot(list1_x,list1_y,label="TESLA")
# # formating the graph
# plt.title('TESLA broadcast based message authentication')
# plt.grid(True)
# plt.xlabel('No. of vehicles in simulation')
# plt.ylabel('Time taken')
# plt.legend(handles=[line_1], loc=1)
# plt.show()

k = 1
for i in range(50):
	start_time= time.time()
	st = "./hmac "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	k += 10
	print("{0}  {1}".format(k, time.time() - start_time))
	list1_x.append(k-1)
	list1_y.append(time.time() - start_time)

line_1, = plt.plot(list1_x,list1_y,label="MAC based protocol")
# formating the graph
plt.title('HMAC based message authentication')
plt.grid(True)
plt.xlabel('No. of vehicles in simulation')
plt.ylabel('Time taken')
plt.legend(handles=[line_1], loc=1)
plt.show()


