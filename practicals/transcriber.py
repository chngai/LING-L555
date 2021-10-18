#This program convert the written srting into IPA transcription.
#It it replaceing the 8th tab to "IPA="kat

#Flowchart: read the output from tokeniser.py
#look for stuff after a "numeric plus a tab"
#store that away and compare it with the tr list
#store the results of the output in a separate variable
#convert the 8th tab to the following format (IPA=.......)
#print the output of the all the lines
import sys



tr = {'a': 'a', 
'u': 'ʌ',
'at':'æ',
'ə':'aw',
'e':'ɪ',
'ee':'ɪ',
'oo': 'ɒ'} #keep filling up this list

for line in sys.stdin.readlines():
	row = line.split('\t')
# if there are not 10 cells, skip the line
	if len(row) != 10:
		print (line.strip())
		continue
	#now we have the string or the target token stored away in form
	form = row[1]
	#After storing the word, it is now sorting the list transcriber list 
	chs = list (tr.keys())
	chs. sort(key= lambda x: len(x), reverse=True)
	transliterated = form
	for c in chs:
		transliterated = transliterated.replace(c, tr[c])
	row[9]= 'IPA=' + transliterated
	print ('\t'.join(row))
