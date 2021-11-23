import sys
from collections import Counter

m={}
POS={}

for line in sys.stdin.readlines():
		row = line.split('\t')
# if there are not 10 cells, skip the line
		if len(row)!= 10:
			continue
		#append the second column into a list
		token = row[1]
		tag = row[3]
		#check if the token is previousl encountered
		if row[1] not in m: 
			m[token]={}
		#check if the POS tag is previousl encountered
		if row[3] not in m:
			m[token][tag]=0
		if tag in m[token]:
			m[token][tag] +=1
		if tag not in POS:
			#add the tag into the POS
			POS[tag]= 0
		POS[tag]+=1

Startingline = '# P\tcount\ttag\tform'
print(Startingline)
for tag in POS:
	print("%.2f\t%d\t%s\t_" % (POS[tag]/sum(POS.values()),POS[tag],tag))
for token in m:
	for tag in m[token]:
		print("%.2f\t%d\t%s\t%s" % (m[token][tag]/sum(m[token].values()),m[token][tag],tag,token))
