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

file = open("new_protocol_data.dat","w")

k = 1
for i in range(100):
	start_time= time.time()
	st = "./hmac "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	st = "./sharing_initial.py "+str(k)
	subprocess.call(st, stdout=False, shell=True)
	k += 4
	print("{0}  {1}".format(k, time.time() - start_time))
	# list1_x.append((k-1)/4)
	# list1_y.append(time.time() - start_time)
	strin = str((k-1)/4)+" "+str(time.time()-start_time)
	file.write(strin+"\n")
	# file.write("")
file.close()
# line_1, = plt.plot(list1_x,list1_y,'g^',label="Proposed-Protocol")
# # formating the graph
# plt.title('Proposed protocol for message authentication')
# plt.grid(True)
# plt.xlabel('No. of vehicles in simulation')
# plt.ylabel('Time taken(s)')
# plt.legend(handles=[line_1], loc=1)
# plt.show()


