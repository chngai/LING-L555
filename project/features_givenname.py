import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import epitran as ep
import re
import math
import seaborn as sns
epi = ep.Epitran('cmn-Hans', cedict_file='cedict_1_0_ts_utf-8_mdbg.txt')
df = pd.read_csv('givenname.csv', delimiter =',')

#convert characters to ipa
#create new column and convert character column into ipa
ipa =[]
for i  in df['character']:
	ipa.append(epi.transliterate(i))
df['ipa'] = ipa



#--------------------------------this is a line----------------------
#converting tone features
tones =[]
heights =[]
contours =[]
levels =[]
risings =[]
fallings =[]
melodies =[]

for i in df['pinyin']:
	if '1' in i:
		#tone 1 is a high level tone
		tones.append(1)
		heights.append('high')
		contours.append('level')
		levels.append(1)
		risings.append(0)
		fallings.append(0)
		melodies.append('high')
	elif '2' in i:
		#tone 2 is mid rising tone
		tones.append(2)
		heights.append('mid')
		contours.append('rising')
		levels.append(0)
		risings.append(1)
		fallings.append(0)
		melodies.append('high')
	elif '3' in i:
		#tone 3 is low falling-rising tone
		tones.append(3)
		heights.append('low')
		contours.append('falling-rising')
		levels.append(0)
		risings.append(1)
		fallings.append(1)
		melodies.append('low')
	elif '4' in i:
		#tone 4 is high falling tone
		tones.append(4)
		heights.append('high')
		contours.append('falling')
		levels.append(0)
		risings.append(0)
		fallings.append(1)
		melodies.append('low')
	elif re.findall(r'[^1234]', i):
		tones.append('missing')
		heights.append('missing')
		contours.append('missing')
		levels.append('missing')
		risings.append('missing')
		fallings.append('missing')
		melodies.append('missing')

df['tone'] =tones
df['tone_height'] =heights
df['tone_contour'] =contours
df['tone_level'] =levels
df['tone_rising'] =risings
df['tone_falling'] =fallings
df['tone_melody'] = melodies


#Tone Update
registers =[]
pitches = []
melodies = []

for i in df ['pinyin']:
	if '1' in i:
		registers.append('+upper')
		pitches.append ('raised_H')
		melodies.append('high')
	elif '2' in i:
		registers.append('+upper')
		pitches.append ('raised_L')
		melodies.append('high')
	elif '3' in i:
		registers.append('-upper')
		pitches.append ('raised_H')
		melodies.append('low')
	elif '4' in i:
		registers.append('-upper')
		pitches.append ('raised_L')
		melodies.append('low')
	elif re.findall(r'[^1234]', i):
		registers.append('missing')
		pitches.append ('missing')
		melodies.append('missing')

df['tone_register'] = registers
df['tone_pitch'] = pitches
df['tone_melody'] = melodies

#---------------------------------this is a line-----------------------------------------
#converting vowels features to numerics

# converto to numeric
backednesses = []
heights =[]
roundednesses =[]

#backedness feature for monophthong
for i in df['ipa']:
	if re.findall (r'[^aəiyɤuoe]*[iye][^aəiyɤuoe]*', i):    #i, e, and y
		backednesses.append('front')
	elif re.findall (r'[^aəiyɤuoe]*[əa][^aəiyɤuoe]*', i):  #ə and a(isn't a front?)
		backednesses.append('center') 
	elif re.findall (r'[^aəiyɤuoe]*[uoɤ][^aəiyɤuoe]*', i):   # u, o, and ɤ
		backednesses.append('back')
	elif re.findall (r'[^aəiyɤuoe]*[iye][aəiyɤuoe][^aəiyɤuoe]*', i):  #diphtong i, e, and y
		backednesses.append('front')
	elif re.findall (r'[^aəiyɤuoe]*[əa][aəiyɤuoe][^aəiyɤuoe]*', i):  #diphthong ə and a(isn't a front?)
		backednesses.append('center') 
	elif re.findall (r'[^aəiyɤuoe]*[uoɤ][aəiyɤuoe][^aəiyɤuoe]*', i):   #diphthong u, o, and ɤ
		backednesses.append('back')
	elif re.findall (r'[^aəiyɤuoe]*[iye][aəiyɤuoe][aəiyɤuoe][^aəiyɤuoe]*', i):  #triphtong i, e, and y
		backednesses.append('front')
	elif re.findall (r'[^aəiyɤuoe]*[əa][aəiyɤuoe][aəiyɤuoe][^aəiyɤuoe]*', i):  #triphthong ə and a(isn't a front?)
		backednesses.append('center') 
	elif re.findall (r'[^aəiyɤuoe]*[uoɤ][aəiyɤuoe][aəiyɤuoe][^aəiyɤuoe]*', i):   #triphthong u, o, and ɤ
		backednesses.append('back')
	else: 
		backednesses.append('missing')

#height feature for monophthong
for i in df['ipa']:
	if re.findall (r'[^aəiyɤuoe]*[iyuɤ][^aəiyɤuoe]*', i):  #i, y, u, and ɤ
		heights.append('high')
	elif re.findall (r'[^aəiyɤuoe]*[əeo][^aəiyɤuoe]*', i):    #ə,o, and e
		heights.append('middle') 
	elif re.findall (r'[^aəiyɤuoe]*[a][^aəiyɤuoe]*', i):    #a
		heights.append('low')
	elif re.findall (r'[^aəiyɤuoe]*[iyuɤ][aəiyɤuoe][^aəiyɤuoe]*', i):  # diphthong i, y, u, and ɤ
		heights.append('high')
	elif re.findall (r'[^aəiyɤuoe]*[əeo][aəiyɤuoe][^aəiyɤuoe]*', i):    #diphthong ə,o, and e
		heights.append('middle') 
	elif re.findall (r'[^aəiyɤuoe]*[a][aəiyɤuoe][^aəiyɤuoe]*', i):    #diphthong a
		heights.append('low')
	elif re.findall (r'[^aəiyɤuoe]*[iyuɤ][aəiyɤuoe][aəiyɤuoe][^aəiyɤuoe]*', i):  # triphthong i, y, u, and ɤ
		heights.append('high')
	elif re.findall (r'[^aəiyɤuoe]*[əeo][aəiyɤuoe][aəiyɤuoe][^aəiyɤuoe]*', i):    #triphthong ə,o, and e
		heights.append('middle') 
	elif re.findall (r'[^aəiyɤuoe]*[a][aəiyɤuoe][aəiyɤuoe][^aəiyɤuoe]*', i):    #triphthong a
		heights.append('low')
	else: #fail safe for missing vowel for height feature
		heights.append('missing')


#rounded feature for monophthong
for i in df['ipa']:
	if re.findall (r'[^aəiyɤuoe]*[uoy][^aəiyɤuoe]*', i):      #u, o, and y
		roundednesses.append('rounded')
	elif re.findall (r'[^aəiyɤuoe]*[iɤəae][^aəiyɤuoe]*', i):   #i, ɤ, ə, e, and a
		roundednesses.append('unround')
	elif re.findall (r'[^aəiyɤuoe]*[uoy][aəiyɤuoe][^aəiyɤuoe]*', i):      #diphthong u, o, and y
		roundednesses.append('rounded')
	elif re.findall (r'[^aəiyɤuoe]*[iɤəae][aəiyɤuoe][^aəiyɤuoe]*', i):   #diphthong i, ɤ, ə, e, and a
		roundednesses.append('unround')
	elif re.findall (r'[^aəiyɤuoe]*[uoy][aəiyɤuoe][aəiyɤuoe][^aəiyɤuoe]*', i):      #triphthong u, o, and y
		roundednesses.append('rounded')
	elif re.findall (r'[^aəiyɤuoe]*[iɤəae][aəiyɤuoe][aəiyɤuoe][^aəiyɤuoe]*', i):   #triphthong i, ɤ, ə, e, and a
		roundednesses.append('unround')
	else:            #fail safe for missing vowel for height feature
		roundednesses.append('missing')
		
df['vowel_backedness'] = backednesses
df['vowel_height'] = heights
df['vowel_roundedness'] = roundednesses


#---------------------size correspondence--------------------------------------
#tagging size
sizes = []

for i in df['ipa']:
	if re.findall (r'[^aəiyɤuoe]*[i][^aəiyɤuoe]*', i):    #i, e, and y
		sizes.append('small')
	elif re.findall (r'[^aəiyɤuoe]*[a][^aəiyɤuoe]*', i):  #ə and a(isn't a front?)
		sizes.append('large')
	else: 
		sizes.append('missing')

df ['size'] = sizes



#------------this is a line-----------------
#counting diphthongs & triphthongs

diphthongs_counter = 0
triphthongs_counter = 0
for i in df['ipa']:
	if re.findall ('(ai|ia|ua|ua|ya|ao)', i):
		diphthongs_counter +=1
	if re.findall ('(uai|iao)', i):
		triphthongs_counter +=1
diph_percentage = (diphthongs_counter/2614)
tri_percentage = (triphthongs_counter/2614)
print ('number of diphthongs = %d'%diphthongs_counter)
print ('percentage of diphthongs =%.2f'%diph_percentage)
print ('number of triphthongs = %d'%triphthongs_counter)
print ('percentage of triphthongs =%.2f'%tri_percentage)


#----------------------------------masculine and feminie---------------------
#transforming variable
df['masculine'] = (df['n.male'] / (df['n.male'] + df['n.female']))
df['feminine'] = (df['n.female'] / (df['n.male'] + df['n.female']))
df.to_csv (r'givename_16052022.csv', index = False, header=True)
