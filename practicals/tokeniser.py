import sys

sent_id = 0

c = 0

count = 0

for line in sys.stdin.readlines():
	line = line.strip()
	if line == '': #skip empty lines
		continue
	token_id = 0
	#break text into sentences
	#if c == '. ':
	#	c.replace('. ', '.\n')
	print ('# sent_id = %d' % (sent_id))
	print ("# text=",line)
	#break sentencs into tokens
	for c in ',"()':
		line = line.replace(c, ' '+c+' ')
	tokenes= line.split()
	for token in tokenes:
		count = count + 1
		#print (token)
		print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_'% (count, token))
		sent_id = sent_id + 1
	count = 0
	print('')
