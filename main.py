#!/usr/bin/python

from test import test

print "Personne 1 :\n"
array1 = test()
print "\nPersonne 2 :\n"
array2 = test()

error = 0.05
total = 0

for i in range(52):
	for j in range(52):
		if array1[i][j] != 0 and array2[i][j] != 0 and abs(array1[i][j] - array2[i][j]) > error:
			total += 1
#end for

if total > 5:
	print "\nPersonnes differentes"
else:
	print "\nMeme personne"

#je fais nimp la, si ya 0.05 sec de differences pour un couple de lettres, j'incremente le total
#si le total est superieur a 5, c'est pas la meme personne