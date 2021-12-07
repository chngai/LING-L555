import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import epitran as ep
import statsmodels.api as sm
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


#--------plotting out the data-------
#------------masculine-----
options =['low','mid','high']
plot_df = df[df['tone_height'].isin(options)]
plt.figure(0)
plt.title('Discribution of Tone Height in Male Names')
plt.ylabel('Percentage of Male Names')
ax =sns.boxplot (x = 'tone_height', y ='masculine', data = plot_df)
plt.savefig('tone_height~masculine.png')
options =[]

plt.figure(1)
options =['1','2','3','4']
plot_df = df[df['tone'].isin(options)]
plt.title('Discribution of Tones in Male Names')
plt.ylabel('Percentage of Male Names')
bx = sns.boxplot(x= "tone", y= "masculine", data = plot_df)
plt.savefig('tone~masculine.png')
option =[]

plt.figure(2)
options =['level','rising','failling-rising','falling']
plot_df = df[df['tone_contour'].isin(options)]
plt.title('Discribution of Tonal Contour in Male Names')
plt.ylabel('Percentage of Male Names')
cx = sns.boxplot(x= "tone_contour", y= "masculine", data = plot_df)
plt.savefig('tone_contour~masculine.png')
options =[]

plt.figure(3)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel in Male Names')
plt.ylabel('Percentage of Male Names')
dx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df)
plt.savefig('vowel_backedness~masculine.png')
options =[]

plt.figure(4)
options =['high','middle','low']
plot_df = df[df['vowel_height'].isin(options)]
plt.title('Discribution of Vowal Heights in Male Names')
plt.ylabel('Percentage of Male Names')
ex = sns.boxplot (x= "vowel_height", y= "masculine", data = plot_df)
plt.savefig('vowel_height~masculine.png')
options =[]


plt.figure(5)
options =['rounded','unround']
plot_df = df[df['vowel_roundedness'].isin(options)]
plt.title('Discribution of Vowal Roundedness in Male Names')
plt.ylabel('Percentage of Male Names')
fx = sns.boxplot (x= "vowel_roundedness", y= "masculine", data = plot_df)
plt.savefig('vowel_roundedness~masculine.png')
options =[]

#-------------------------feminie----------------------
plt.figure(6)
options =['low','mid','high']
plot_df = df[df['tone_height'].isin(options)]
plt.title('Discribution of Tone Height in Female Names')
plt.ylabel('Percentage of Female Names')
gx =sns.boxplot (x = 'tone_height', y ='feminine', data = plot_df, hue="tone_height")
plt.savefig('tone_height~feminity.png')
options =[]
plt.savefig('tone_height~feminine.png')

plt.figure(7)
options =['1','2','3','4']
plot_df = df[df['tone'].isin(options)]
plt.title('Discribution of Tones in Female Names')
plt.ylabel('Percentage of Female Names')
hx = sns.boxplot(x= "tone", y= "feminine", data = plot_df , hue="tone")
plt.savefig('tone~feminine.png')
option =[]

plt.figure(8)
options =['level','rising','failling-rising','falling']
plot_df = df[df['tone_contour'].isin(options)]
plt.title('Discribution of Tonal Contour in Female Names')
plt.ylabel('Percentage of Female Names')
ix = sns.boxplot(x= "tone_contour", y= "feminine", data = plot_df, hue = "tone_contour")
plt.savefig('tone_contour~feminine.png')

plt.figure(9)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel in Female Names')
plt.ylabel('Percentage of Female Names')
jx = sns.boxplot(x= "vowel_backedness", y= "feminine", data = plot_df, hue = "vowel_backedness")
options =[]
plt.savefig('vowel_backedness~feminine.png')

plt.figure(10)
options =['high','middle','low']
plot_df = df[df['vowel_height'].isin(options)]
plt.title('Discribution of Vowal Heights in Female Names')
plt.ylabel('Percentage of Female Names')
kx = sns.boxplot (x= "vowel_height", y= "feminine", data = plot_df, hue ="vowel_height")
plt.savefig('vowel_height~feminine.png')
options =[]


plt.figure(11)
options =['rounded','unround']
plot_df = df[df['vowel_roundedness'].isin(options)]
plt.title('Discribution of Vowal Roundedness in Female Names')
plt.ylabel('Percentage of Female Names')
lx = sns.boxplot (x= "vowel_roundedness", y= "feminine", data = plot_df, hue = "vowel_roundedness")
plt.savefig('vowel_roundedness~feminine.png')
options =[]

#--------plotting out the data-------
#------------plotting the distribution of vowel when considering the effect of tone-----------------
plt.figure(12)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel by Tone Height in Males Names')
plt.ylabel('Percentage of Male Names')
jx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df, hue = "tone_height")
options =[]
plt.savefig('vowel_backedness+tone_height~masculine.png')

plt.figure(13)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel by Tone Height in Males Names')
plt.ylabel('Percentage of Male Names')
jx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df, hue = "tone")
options =[]
plt.savefig('vowel_backedness+tone~masculine.png')


#-------------------this is a line-------------------------
#---statistical test---
"""converting column into dummy column variable"""
df2 = df.copy()

df2 = pd.get_dummies(df2, columns =['vowel_roundedness','vowel_height','vowel_roundedness', 'tone_height', 'tone_contour'])

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import epitran as ep
import statsmodels.api as sm
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

#--------plotting out the data-------
#------------masculine-----
options =['low','mid','high']
plot_df = df[df['tone_height'].isin(options)]
plt.figure(0)
plt.title('Discribution of Tone Height in Male Names')
plt.ylabel('Percentage of Male Names')
ax =sns.boxplot (x = 'tone_height', y ='masculine', data = plot_df)
plt.savefig('tone_height~masculine.png')
options =[]

plt.figure(1)
options =['1','2','3','4']
plot_df = df[df['tone'].isin(options)]
plt.title('Discribution of Tones in Male Names')
plt.ylabel('Percentage of Male Names')
bx = sns.boxplot(x= "tone", y= "masculine", data = plot_df)
plt.savefig('tone~masculine.png')
option =[]

plt.figure(2)
options =['level','rising','failling-rising','falling']
plot_df = df[df['tone_contour'].isin(options)]
plt.title('Discribution of Tonal Contour in Male Names')
plt.ylabel('Percentage of Male Names')
cx = sns.boxplot(x= "tone_contour", y= "masculine", data = plot_df)
plt.savefig('tone_contour~masculine.png')
options =[]

plt.figure(3)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel in Male Names')
plt.ylabel('Percentage of Male Names')
dx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df)
plt.savefig('vowel_backedness~masculine.png')
options =[]

plt.figure(4)
options =['high','middle','low']
plot_df = df[df['vowel_height'].isin(options)]
plt.title('Discribution of Vowal Heights in Male Names')
plt.ylabel('Percentage of Male Names')
ex = sns.boxplot (x= "vowel_height", y= "masculine", data = plot_df)
plt.savefig('vowel_height~masculine.png')
options =[]

plt.figure(5)
options =['rounded','unround']
plot_df = df[df['vowel_roundedness'].isin(options)]
plt.title('Discribution of Vowal Roundedness in Male Names')
plt.ylabel('Percentage of Male Names')
fx = sns.boxplot (x= "vowel_roundedness", y= "masculine", data = plot_df)
plt.savefig('vowel_roundedness~masculine.png')
options =[]

#-------------------------feminie----------------------
plt.figure(6)
options =['low','mid','high']
plot_df = df[df['tone_height'].isin(options)]
plt.title('Discribution of Tone Height in Female Names')
plt.ylabel('Percentage of Female Names')
gx =sns.boxplot (x = 'tone_height', y ='feminine', data = plot_df, hue="tone_height")
plt.savefig('tone_height~feminity.png')
options =[]
plt.savefig('tone_height~feminine.png')

plt.figure(7)
options =['1','2','3','4']
plot_df = df[df['tone'].isin(options)]
plt.title('Discribution of Tones in Female Names')
plt.ylabel('Percentage of Female Names')
hx = sns.boxplot(x= "tone", y= "feminine", data = plot_df , hue="tone")
plt.savefig('tone~feminine.png')
option =[]

plt.figure(8)
options =['level','rising','failling-rising','falling']
plot_df = df[df['tone_contour'].isin(options)]
plt.title('Discribution of Tonal Contour in Female Names')
plt.ylabel('Percentage of Female Names')
ix = sns.boxplot(x= "tone_contour", y= "feminine", data = plot_df, hue = "tone_contour")
plt.savefig('tone_contour~feminine.png')

plt.figure(9)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel in Female Names')
plt.ylabel('Percentage of Female Names')
jx = sns.boxplot(x= "vowel_backedness", y= "feminine", data = plot_df, hue = "vowel_backedness")
options =[]
plt.savefig('vowel_backedness~feminine.png')

plt.figure(10)
options =['high','middle','low']
plot_df = df[df['vowel_height'].isin(options)]
plt.title('Discribution of Vowal Heights in Female Names')
plt.ylabel('Percentage of Female Names')
kx = sns.boxplot (x= "vowel_height", y= "feminine", data = plot_df, hue ="vowel_height")
plt.savefig('vowel_height~feminine.png')
options =[]

plt.figure(11)
options =['rounded','unround']
plot_df = df[df['vowel_roundedness'].isin(options)]
plt.title('Discribution of Vowal Roundedness in Female Names')
plt.ylabel('Percentage of Female Names')
lx = sns.boxplot (x= "vowel_roundedness", y= "feminine", data = plot_df, hue = "vowel_roundedness")
plt.savefig('vowel_roundedness~feminine.png')
options =[]

#--------plotting out the data-------
#------------plotting the distribution of vowel when considering the effect of tone-----------------
plt.figure(12)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel by Tone Height in Males Names')
plt.ylabel('Percentage of Male Names')
jx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df, hue = "tone_height")
options =[]
plt.savefig('vowel_backedness+tone_height~masculine.png')

plt.figure(13)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel by Tone Height in Males Names')
plt.ylabel('Percentage of Male Names')
jx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df, hue = "tone")
options =[]
plt.savefig('vowel_backedness+tone~masculine.png')

#-------------------this is a line-------------------------
#---statistical test---

df2 = df.copy()
df2 = pd.get_dummies(df2, columns =['vowel_roundedness','vowel_height','vowel_roundedness', 'tone_height', 'tone_contour'])

df2.to_csv('edited_givenname_07_12_21.csv', delimiter=',', encoding='utf-8')

df2['tone_height_high'] = df2['tone_height_high'].astype('category')
df2['tone_height_mid'] = df2['tone_height_mid'].astype('category')
df2['tone_height_low'] = df2['tone_height_low'].astype('category')
df2['tone_contour_level'] = df2['tone_contour_level'].astype('category')
df2['tone_contour_rising'] = df2['tone_contour_rising'].astype('category')
df2['tone_contour_falling-rising'] = df2['tone_contour_falling_rising'].astype('category')
df2['tone_contour_falling'] = df2['tone_contour_falling'].astype('category')
df2['vowel_backedness_front'] = df2['vowel_backedness_front'].astype('category')
df2['vowel_backedness_back'] = df2['vowel_backedness_back'].astype('category')
df2['vowel_backedness_center'] = df2['vowel_backedness_center'].astype('category')
df2['vowel_height_high'] = df2['vowel_height'].astype('category')
df2['vowel_height_middle'] = df2['vowel_height'].astype('category')
df2['vowel_height_low'] = df2['vowel_height'].astype('category')
df2['vowel_roundedness_rouneded'] = df2['vowel_roundedness_rounded'].astype('category')
df2['vowel_roundedness_unround'] = df2['vowel_roundedness_unround'].astype('category')

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
'vowel_roundedness_rouneded',
'vowel_roundedness_unround']]
X = sm.add_constant(X)

#lines for regression
ks = sm.OLS(Y, X).fit()
ks_res =ks.fit()
ks_res.summary()
```

for c in df2.columns: 
	print(c)

print (df2.head(3))

