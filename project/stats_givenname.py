import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import epitran as ep
import re
import math
import seaborn as sns
df = pd.read_csv('givenname_01122021_mono.csv', delimiter =',')#--------plotting out the data-------

#-----------this is a line------
#plotting charts
plt.figure(0)
plt.title('Discribution of tone height in male percentage population')
plt.ylabel('percentage of males')
ax =sns.scatterplot (x = 'tone_height', y ='masculine', s =100, data = df)
plt.savefig('tone_height~masculine_scatterplot.png')

plt.figure(1)
plt.title('Discribution of tones in male percentage population')
plt.ylabel('percentage of males')
bx = sns.scatterplot (x= "tone", y= "masculine", data = df, color ='#99c2a2')
plt.savefig('tone~masculine.png')

plt.figure(2)
plt.title('Discribution of tone contour in male percentage population')
plt.ylabel('percentage of males')
cx = sns.scatterplot (x= "tone_contour", y= "masculine", data = df, color ='#99c2a2')
plt.savefig('tone_contour~masculine.png')

plt.figure(3)
plt.title('Discribution of vowel backedness in male percentage population')
plt.ylabel('percentage of males')
dx = sns.scatterplot (x= "vowel_backedness", y= "masculine", data = df, color ='#99c2a2')
plt.savefig('vowel_backedness~masculine.png')

plt.figure(4)
plt.title('Discribution of vowel height in male percentage population')
plt.ylabel('percentage of males')
ex = sns.scatterplot (x= "vowel_height", y= "masculine", data = df, color ='#99c2a2')
plt.savefig('vowel_height~masculine.png')

plt.figure(5)
plt.title('Discribution of vowel roundedness in male percentage population')
plt.ylabel('percentage of males')
fx = sns.scatterplot (x= "vowel_roundedness", y= "masculine", data = df, color ='#99c2a2')
plt.savefig('vowel_roundedness~masculine.png')

#----feminie--------------
plt.figure(6)
gx =sns.scatterplot  (x = 'tone_height', y ='feminine', data = df, color ='#99c2a2')
plt.savefig('tone_height~feminine.png')

plt.figure(7)
hx = sns.scatterplot (x= "tone", y= "feminine", data = df)
plt.savefig('tone~feminine.png')

plt.figure(8)
ix = sns.scatterplot (x= "tone_contour", y= "feminine", data = df)
plt.savefig('tone_contour~feminine.png')

plt.figure(9)
jx = sns.scatterplot (x= "vowel_backedness", y= "feminine", data = df)
plt.savefig('vowel_backedness~feminine.png')

plt.figure(10)
kx = sns.scatterplot (x= "vowel_height", y= "feminine", data = df)
plt.savefig('vowel_height~feminine.png')

plt.figure(11)
lx = sns.scatterplot (x= "vowel_roundedness", y= "feminine", data = df)
plt.savefig('vowel_roundedness~feminine.png')



# STATISTICAL TESTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Converting column into dummy column variable
df2 = df.copy()
df2 = pd.get_dummies(df2, columns =['vowel_roundedness','vowel_height','vowel_backedness', 'tone_height', 'tone_contour'])


# Convert data to category datatype
for c in df2.columns: 
    df2[c] = df2[c].astype('category')

# Selecting data for statistical regession
Y = df2['masculine']
X = df2[['tone_height_high',
'tone_height_mid',
'tone_height_low',
'tone_contour_level',
'tone_contour_rising',
'tone_contour_falling-rising',
'tone_contour_falling',
'vowel_backedness_front',
'vowel_backedness_back',
'vowel_backedness_center',
'vowel_height_high',
'vowel_height_middle',
'vowel_height_low',
'vowel_roundedness_rounded',
'vowel_roundedness_unround']]
X = sm.add_constant(X)


# Lines for regression
ks = sm.OLS(Y, X)
ks_res =ks.fit()
print(ks_res.summary())

# for c in df2.columns: 
# 	print(c)

#print(df2.head(3))
