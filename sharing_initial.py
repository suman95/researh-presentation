#!/usr/bin/python2.7
from secretsharing import PlaintextToHexSecretSharer
import sys
import math
import time

def share_generate():
	return PlaintextToHexSecretSharer.split_secret("this is the secret",2,3);

def share_recover(shares):
	PlaintextToHexSecretSharer.recover_secret(shares)

if __name__=="__main__":
	shares = ['1-567718946e1d59d4736a328a6ce', '2-57d2c80ddca5647ce5a415d026a', '3-d382393362b85b255a226fe273', '4-7fcba97acd2a0247509f134b941', '5-38b1d81af41b1f0e63d587ef931', '6-410f2dc9fd7920da1c80322149b']
	reps = int(str(sys.argv[1]))
	time.sleep(reps/2500.0)
	# if(reps > 30):
	# 	reps = 30
	for i in range(int(math.floor(reps))):
		share_recover(shares[0:4])