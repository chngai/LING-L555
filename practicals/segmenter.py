import sys

line = sys.stdin.readline()
while line:
	pars = line.split('. ')
	for cent in pars:
		print (cent)
	line = sys.stdin.readline()
