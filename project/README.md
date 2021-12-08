# Givenname Project
## Brief Overview:

  The aim of my current project is to investigate the correspondence between sound and meaning in Mandarin Chinese first names. With the ever-growing body of studies on the naming of fictional characters, the investigation of sound symbolism on first names has been limited thus far. The vast majority of these studies have focused on personal names in English (Cassidy et al., 1999; Cutler et al., 2017; Pitcher et al., 2013a; Sidhu & Pexman, 2015; Slater & Feinman, 1985; Sutton, 2016; Wright et al., 2005). Namely, these studies have reported vowels associated with smallness were more commonly found in female names (e.g. front vowels like /i/, /e/, and /aɪ/). On the contrary, male names were likely to contain vowels that are associated with largess (e.g. back vowels like/ æ/, /o/, and /eɪ/). These preferences have been proposed to reflect biological dimorphism where body-size preference guides gender-name assignment (Pitcher et al., 2013b; Sidhu & Pexman, 2015; Slater & Feinman, 1985). Although some studies have gone beyond Indo-European languages, the interaction between tones and segmental information remains unexplored (Urdu: Moshin & Kang, 2018, Mandarin: van de Weijer et al., 2020, and Cantonese: Wong & Kang, 2019). Of interest is whether these generalizations applied to Mandarin Chinese single vowels and how sound-gender associations interact with suprasegmental features (tones).
Name-gender association is evaluated using linear regression. The givenname database used in the current study is Chinese Name Database 1930-2008. This database covers the frequency of 1.2 billion Han Chinese population starting from 1930 to 2008. To my knowledge, forming the most comprehensive and extensive database of names to date to date. Gender biases are defined as the difference in the proportion of males and females consisting of a given character. All characters were subsequently converted to IPA transcription using an online translation tool from GitHub (https://github.com/Connum/npm-pinyin2ipa#readme). All translations were then verified by a native Mandarin Chinese speaker with linguistic background. All names were coded for their phonetic features, including vowel and tonal features, and their gender adaptation (maleness: 0-1/ femaleness: 0-1).


## Coding:
  The following files are uploaded (refer to pdf file for details):

-1)givenname_01122021_mono.csv
-2)stats_givenname.py
-3)feature_givenname.py

  For file 1, it is the csv file for the program to run.
  For file 2, it generates the plots and statistical model
  For file 3, it generates the phonetic features, necessary for running analysis.
