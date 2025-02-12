import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import re

# CURRENTLY UNUSED

lm = LinearRegression()

df = pd.read_csv('givenname_01122021_mono.csv', delimiter =',')

np.random.seed(42)

# convert characters to ipa
# #create new column and convert character column into ipa
# ipa =[]
# for i  in df['character']:
# 	ipa.append(epi.transliterate(i))
# df['ipa'] = ipa

#filtering out cells with 'missing'
for c in df.columns: 
	df[c] != "missing"
    
#-------this is a line-------------------------
#Updating columns on masculine and feminie

df['masculine'] = (df['n.male'] / (df['n.male'] + df['n.female']))
df['feminine'] = (df['n.female'] / (df['n.male'] + df['n.female']))

print(df['masculine'],df['feminine'] )
#------------------------plotting out the data-----------------
#------------masculine-----
options =["+upper", "-upper"]
plot_df = df[df['tone_register'].isin(options)]
sns.set(style="darkgrid")
plt.figure(0)
plt.title('Discribution of Tonal Height in Male Names')
plt.ylabel('Percentage of Male Names')
my_pal = {"+upper": "r", "-upper": "b"}
ax =sns.boxplot (x = 'tone_register', y ='masculine', data = plot_df, palette=my_pal)
plt.savefig('tone_register~masculine.png')
options =[]

plt.figure(1)
options =['1','2','3','4']
plot_df = df[df['tone'].isin(options)]
plt.title('Discribution of Tones in Male Names')
plt.ylabel('Percentage of Male Names')
my_pal = {"1": "r", "2": "b", "3":"g", "4":"yellow"}
sns.set(style="darkgrid")
bx = sns.boxplot(x= "tone", y= "masculine", data = plot_df, palette=my_pal)
plt.savefig('tone~masculine.png')
option =[]

plt.figure(2)
options =['raised_L', 'raised_H']
plot_df = df[df['tone_pitch'].isin(options)]
plt.title('Discribution of Tonal Pitch in Male Names')
plt.ylabel('Percentage of Male Names')
sns.set(style="darkgrid")
my_pal = {"raised_L":"indigo", "raised_H":"r"}
cx = sns.boxplot(x= "tone_pitch", y= "masculine", data = plot_df, palette=my_pal)
plt.savefig('tone_pitch~masculine.png')
options =[]

plt.figure(3)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel Backedness in Male Names')
plt.ylabel('Percentage of Male Names')
sns.set(style="darkgrid")
my_pal = {"front": "r", "center": "b", "back":"g"}
dx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df, palette=my_pal)
plt.savefig('vowel_backedness~masculine.png')
options =[]

plt.figure(4)
options =['high','middle','low']
plot_df = df[df['vowel_height'].isin(options)]
plt.title('Discribution of Vowal Heights in Male Names')
plt.ylabel('Percentage of Male Names')
sns.set(style="darkgrid")
ex = sns.boxplot (x= "vowel_height", y= "masculine", data = plot_df)
plt.savefig('vowel_height~masculine.png')
options =[]


plt.figure(5)
options =['rounded','unround']
plot_df = df[df['vowel_roundedness'].isin(options)]
plt.title('Discribution of Vowal Roundedness in Male Names')
plt.ylabel('Percentage of Male Names')
sns.set(style="darkgrid")
my_pal = {"rounded": "k", "unround": "lightgrey"}
fx = sns.boxplot (x= "vowel_roundedness", y= "masculine", data = plot_df, palette=my_pal)
plt.savefig('vowel_roundedness~masculine.png')
options =[]

#-------------------------feminie----------------------
options =["+upper", "-upper"]
plot_df = df[df['tone_register'].isin(options)]
sns.set(style="darkgrid")
plt.figure(14)
plt.title('Discribution of Tonal Height in Female Names')
plt.ylabel('Percentage of Female Names')
my_pal = {"+upper": "r", "-upper": "b"}
ax =sns.boxplot (x = 'tone_register', y ='feminine', data = plot_df, palette=my_pal)
plt.savefig('tone_register~feminine.png')
options =[]

plt.figure(15)
options =['raised_L', 'raised_H']
plot_df = df[df['tone_pitch'].isin(options)]
plt.title('Discribution of Tonal Pitch in Female Names')
plt.ylabel('Percentage of Female Names')
sns.set(style="darkgrid")
my_pal = {"raised_L":"indigo", "raised_H":"r"}
cx = sns.boxplot(x= "tone_pitch", y= "feminine", data = plot_df, palette=my_pal)
plt.savefig('tone_pitch~feminine.png')
options =[]

plt.figure(6)
options =['low','mid','high']
plot_df = df[df['tone_height'].isin(options)]
plt.title('Discribution of Tone Height in Female Names')
plt.ylabel('Percentage of Female Names')
my_pal = {"low": "r", "mid": "b", "high":"g"}
sns.set(style="darkgrid")
gx =sns.boxplot (x = 'tone_height', y ='feminine', data = plot_df, palette=my_pal)
options =[]
plt.savefig('tone_height~feminine.png')

plt.figure(7)
options =['1','2','3','4']
plot_df = df[df['tone'].isin(options)]
plt.title('Discribution of Tones in Female Names')
plt.ylabel('Percentage of Female Names')
sns.set(style="darkgrid")
my_pal = {"1": "r", "2": "b", "3":"g", "4":"yellow"}
hx = sns.boxplot(x= "tone", y= "feminine", data = plot_df, palette=my_pal)
plt.savefig('tone~feminine.png')
option =[]

plt.figure(8)
options =['level','rising','failling-rising','falling']
plot_df = df[df['tone_contour'].isin(options)]
plt.title('Discribution of Tonal Contour in Female Names')
plt.ylabel('Percentage of Female Names')
my_pal = {"level": "g", "rising": "b", "failling-rising":"m", "falling":"r"}
sns.set(style="darkgrid")
ix = sns.boxplot(x= "tone_contour", y= "feminine", data = plot_df, palette=my_pal)
plt.savefig('tone_contour~feminine.png')

plt.figure(9)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel Backedness in Female Names')
plt.ylabel('Percentage of Female Names')
sns.set(style="darkgrid")
my_pal = {"front": "r", "center": "b", "back":"g"}
jx = sns.boxplot(x= "vowel_backedness", y= "feminine", data = plot_df, palette=my_pal)
options =[]
plt.savefig('vowel_backedness~feminine.png')

plt.figure(10)
options =['high','middle','low']
plot_df = df[df['vowel_height'].isin(options)]
plt.title('Discribution of Vowal Heights in Female Names')
plt.ylabel('Percentage of Female Names')
sns.set(style="darkgrid")
kx = sns.boxplot (x= "vowel_height", y= "feminine", data = plot_df)
plt.savefig('vowel_height~feminine.png')
options =[]


plt.figure(11)
options =['rounded','unround']
plot_df = df[df['vowel_roundedness'].isin(options)]
plt.title('Discribution of Vowal Roundedness in Female Names')
plt.ylabel('Percentage of Female Names')
sns.set(style="darkgrid")
my_pal = {"rounded": "k", "unround": "lightgrey"}
lx = sns.boxplot (x= "vowel_roundedness", y= "feminine", data = plot_df, palette=my_pal)
plt.savefig('vowel_roundedness~feminine.png')
options =[]

#--------plotting out the data-------
#------------plotting the distribution of vowel when considering the effect of tone-----------------
plt.figure(12)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
options = ['high','middle','low']
plot_df = df[df['vowel_height'].isin(options)]
plt.title('Discribution of Vowel by Tone Height in Males Names')
plt.ylabel('Percentage of Male Names')
sns.set(style="darkgrid")
jx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df, hue = "tone_height")
options =[]
plt.savefig('vowel_backedness+tone_height~masculine.png')

plt.figure(13)
options =['front','center','back']
plot_df = df[df['vowel_backedness'].isin(options)]
plt.title('Discribution of Vowel by Tone Height in Males Names')
plt.ylabel('Percentage of Male Names')
sns.set(style="darkgrid")
jx = sns.boxplot(x= "vowel_backedness", y= "masculine", data = plot_df, hue = "tone")
options =[]
plt.savefig('vowel_backedness+tone~masculine.png')


# STATISTICAL TESTS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# Converting column into dummy column variable
df2 = df.copy()
df2 = pd.get_dummies(df2, columns =['tone_melody','tone','vowel_roundedness','vowel_height','vowel_backedness', 'tone_height', 'tone_contour', 'tone_pitch','tone_register'])


# Convert data to category datatype
for c in df2.columns: 
    df2[c] = df2[c].astype('category')
     
    

# Selecting data for statistical regession
Y1 = df2['masculine']
Y2 = df2['feminine']
#include everything model
X = df2[['tone_melody_high','tone_melody_low',
'vowel_backedness_front',
'vowel_backedness_back',
'vowel_backedness_center',
'vowel_height_high',
'vowel_height_middle',
'vowel_height_low',
'vowel_roundedness_rounded',
'vowel_roundedness_unround']]

#simplified model
Z= df2[['tone_melody_high','tone_melody_low',
'vowel_height_high',
'vowel_height_middle',
'vowel_height_low',
'vowel_roundedness_rounded',
'vowel_roundedness_unround']]


#----------------------this is a line---------------------------------------
#descriptive statistics
print (df.groupby('tone_melody').agg({'masculine': ['mean', 'std']}))
print (df.groupby('vowel_height').agg({'masculine': ['mean', 'std']}))
print (df.groupby('vowel_roundedness').agg({'masculine': ['mean', 'std']}))
 

X = sm.add_constant(X)
Z = sm.add_constant(Z)


# Lines for regression
#everything model
ks = sm.OLS(Y1, X)
ks_res =ks.fit()
print(ks_res.summary())

#simplified model
ks2 = sm.OLS(Y1, Z)
ks2_res =ks2.fit()
print(ks2_res.summary())

#testing masculine vs feminie as dv
ksf = sm.OLS(Y2, Z)
ksf_res =ksf.fit()
print(ksf_res.summary())

# - - - ---- - PROBLEM HERE - - - - -- - 


# R-like version of GLM
# This dones't work because GLM hates the categorical variables, only accepts numeric
# glm_model = smf.glm("masculine ~ C(tone)", data = df2, family= sm.families.Poisson())
# print (glm_model.summary())

# Now the other way 
"""class statsmodels.genmod.generalized_linear_model.GLM(endog, exog, family=None,
 offset=None, exposure=None, freq_weights=None, var_weights=None, missing='none', **kwargs)"""
data = sm.datasets.scotland.load() # Example code from sm documentation
data.exog = sm.add_constant(data.exog)
gamma_model = sm.GLM(data.endog, data.exog, family=sm.families.Poisson())


my_endogM = np.array(df2['masculine'])
my_endogF = np.array(df2['feminine'])
my_exog = np.array(X)

glm_model = sm.GLM(my_endogM, my_exog, family=sm.families.Poisson())
fitted_glm_model = glm_model.fit()
summary = fitted_glm_model.summary()
print(summary)


#-----------------------this is a line-----------------------
#discarded
"""
#dropping outlier
https://www.listendata.com/2018/01/linear-regression-in-python.html
lm = lm.fit(X, Y)
lm.coef_
coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(lm.coef_))], axis = 1)
lm.intercept_
Y_pred = lm.predict(X_test)
Y_error = Y_test - Y_pred

influence =lm2.get_influence()
resid_student = influence.resid_studentized_external
resid = pd.concat([X,pd.Series(resid_student,name = "Studentized Residuals")],axis = 1)
resid.loc[np.absolute(resid["Studentized Residuals"]) > 3,:]
ind = resid.loc[np.absolute(resid["Studentized Residuals"]) > 3,:].index
Y.drop(ind, axis = 0, inplace = True)
"""
#---------this is a line---------------
# for c in df2.columns: 
# 	print(c)

#print(df2.head(3))

