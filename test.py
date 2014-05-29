#!/usr/bin/python

import time
from getch import getch

def test():
	array = [0]*52 #alphabet (0->25 : uppercase, 26->51 : lowercase)
	count = [0]*52 #counts the number of values (to calculate the average)
	for i in range(52):
		array[i] = [0]*52
		count[i] = [0]*52

	c1 = getch()
	while c1 != '\r':
		start = time.time()
		c2 = getch()
		end = time.time()
		t = end - start
		if c1.isalpha() and c2.isalpha():
			if c1.isupper():
				i1 = ord(c1)-65
			else:
				i1 = ord(c1)-71
			if c2.isupper():
				i2 = ord(c2)-65
			else:
				i2 = ord(c2)-71

			array[i1][i2] += t
			count[i1][i2] += 1
			print c1, '->', c2, ' : ', t
		#end if isalpha
		c1 = c2
	#end while

	for i in range(52):
		for j in range(52):
			if count[i][j] > 0:
				array[i][j] /= count[i][j] #average
	#end for

	return array
#end function
