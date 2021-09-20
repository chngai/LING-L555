import sys

#This  function will segment text into sentence
#The basic appraoch is to search for instances of period+space
#Then replace it with \n

text = sys.stdin.readlines() #read input

#split replacing inputted text into sentences
for line in text: 
	line = line.replace('.','.\n')
	print (line)


#end of function
