import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import epitran as ep
import re
import math
import seaborn as sns
epi = ep.Epitran('cmn-Hans', cedict_file='cedict_1_0_ts_utf-8_mdbg.txt')
df = pd.read_csv('givenname_01122021_mono.csv', delimiter =',')

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
		heights.append(3)
		contours.append(1)
		levels.append(1)
		risings.append(0)
		fallings.append(0)
		melodies.append(2)
	elif '2' in i:
		#tone 2 is mid rising tone
		tones.append(2)
		heights.append(2)
		contours.append(2)
		levels.append(0)
		risings.append(1)
		fallings.append(0)
		melodies.append(2)
	elif '3' in i:
		#tone 3 is low falling-rising tone
		tones.append(3)
		heights.append(1)
		contours.append(3)
		levels.append(0)
		risings.append(1)
		fallings.append(1)
		melodies.append(1)
	elif '4' in i:
		#tone 4 is high falling tone
		tones.append(4)
		heights.append(3)
		contours.append(4)
		levels.append(0)
		risings.append(0)
		fallings.append(1)
		melodies.append(1)
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

#---------------------------------this is a line-----------------------------------------
#converting vowels features to numerics

# converto to numeric
backednesses = []
heights =[]
roundednesses =[]

#backedness feature for monophthong
for i in df['ipa']:
	if re.findall (r'[^aəiyɤuoe]*[iye][^aəiyɤuoe]*', i):    #i, e, and y
		backednesses.append(1)
	elif re.findall (r'[^aəiyɤuoe]*[əa][^aəiyɤuoe]*', i):  #ə and a(isn't a front?)
		backednesses.append(2) 
	elif re.findall (r'[^aəiyɤuoe]*[uoɤ][^aəiyɤuoe]*', i):   # u, o, and ɤ
		backednesses.append(3)
	else: 
		backednesses.append('missing')

#height feature for monophthong
for i in df['ipa']:
	if re.findall (r'[^aəiyɤuoe]*[iyuɤ][^aəiyɤuoe]*', i):  #i, y, u, and ɤ
		heights.append(3)
	elif re.findall (r'[^aəiyɤuoe]*[əeo][^aəiyɤuoe]*', i):    #ə,o, and e
		heights.append(2) 
	elif re.findall (r'[^aəiyɤuoe]*[a][^aəiyɤuoe]*', i):    #a
		heights.append(1)
	else: #fail safe for missing vowel for height feature
		heights.append('missing')


#rounded feature
for i in df['ipa']:
	if re.findall (r'[^aəiyɤuoe]*[uoy][^aəiyɤuoe]*', i):      #u, o, and y
		roundednesses.append(1)
	elif re.findall (r'[^aəiyɤuoe]*[iɤəae][^aəiyɤuoe]*', i):   #i, ɤ, ə, e, and a
		roundednesses.append(0)
	else:            #fail safe for missing vowel for height feature
		roundednesses.append('missing')
		
df['vowel_backedness'] = backednesses
df['vowel_height'] = heights
df['vowel_roundedness'] = roundednesses


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
mono_df['masculine'] = (mono_df['n.male'] / (mono_df['n.male'] + mono_df['n.female']))
mono_df['feminine'] = (mono_df['n.female'] / (mono_df['n.male'] + mono_df['n.female']))
"""

