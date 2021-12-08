# Givenname Project
## Brief Overview:

  The aim of my current project is to investigate the correspondence between sound and meaning in Mandarin Chinese first names. With the ever-growing body of studies on the naming of fictional characters, the investigation of sound symbolism on first names has been limited thus far. The vast majority of these studies have focused on personal names in English (Cassidy et al., 1999; Cutler et al., 2017; Pitcher et al., 2013a; Sidhu & Pexman, 2015; Slater & Feinman, 1985; Sutton, 2016; Wright et al., 2005). Namely, these studies have reported vowels associated with smallness were more commonly found in female names (e.g. front vowels like /i/, /e/, and /aɪ/). On the contrary, male names were likely to contain vowels that are associated with largess (e.g. back vowels like/ æ/, /o/, and /eɪ/). These preferences have been proposed to reflect biological dimorphism where body-size preference guides gender-name assignment (Pitcher et al., 2013b; Sidhu & Pexman, 2015; Slater & Feinman, 1985). Although some studies have gone beyond Indo-European languages, the interaction between tones and segmental information remains unexplored (Urdu: Moshin & Kang, 2018, Mandarin: van de Weijer et al., 2020, and Cantonese: Wong & Kang, 2019). Of interest is whether these generalizations applied to Mandarin Chinese single vowels and how sound-gender associations interact with suprasegmental features (tones).
Name-gender association is evaluated using linear regression. The givenname database used in the current study is Chinese Name Database 1930-2008. This database covers the frequency of 1.2 billion Han Chinese population starting from 1930 to 2008. To my knowledge, forming the most comprehensive and extensive database of names to date to date. Gender biases are defined as the difference in the proportion of males and females consisting of a given character. All characters were subsequently converted to IPA transcription using an online translation tool from GitHub (https://github.com/Connum/npm-pinyin2ipa#readme). All translations were then verified by a native Mandarin Chinese speaker with linguistic background. All names were coded for their phonetic features, including vowel and tonal features, and their gender adaptation (maleness: 0-1/ femaleness: 0-1).

## References
Cassidy, K. W., Kelly, M. H., & Sharoni, L. J. (1999). Inferring gender from name phonology. Journal of Experimental Psychology: General, 128(3), 362–381. https://doi.org/10.1037//0096-3445.128.3.362  
Cutler, A., Mcqueen, J., & Robinson, K. E. N. (2017). Sound Patterns of Men ’ s and Women ’ s Names. 26(2), 471–482.  
Moshin, N., & Kang, Y. (2018). Gender Phonology of Urdu First names. SPF2018.  
Pitcher, B. J., Mesoudi, A., & McElligott, A. G. (2013). Sex-Biased Sound Symbolism in English-Language First Names. PLoS ONE, 8(6), 1–6. https://doi.org/10.1371/journal.pone.0064825  
Sidhu, D. M., & Pexman, P. M. (2015). What’s in a name? Sound symbolism and gender in first names. PLoS ONE, 10(5), 1–22. https://doi.org/10.1371/journal.pone.0126809  
Slater, A. S., & Feinman, S. (1985). Gender and the phonology of north American first names. Sex Roles, 13(7–8), 429–440. https://doi.org/10.1007/BF00287953  
Sutton, L. (2016). Aliens Are Just Like Us: Personal Names in The Legion of Super-Heroes. Names, 64(2), 109–119. https://doi.org/10.1080/00277738.2016.1159446  
van de Weijer, J., Ren, G., van de Weijer, J., Wei, W., & Wang, Y. (2020). Gender identification in Chinese names. Lingua, 234. https://doi.org/10.1016/j.lingua.2019.102759  
Wong, K. W. Y., & Kang, Y. (2019). Sound symbolism of gender in Cantonese First names. 2129–2133.  
Wright, S., Hay, J., & Bent, T. (2005). Ladies ﬁrst? Phonology, frequency, and the naming conspiracy. https://doi.org/10.1515/ling.2005.43.3.531  


## Coding:
  The following files are uploaded (refer to pdf file for details):

- givenname_01122021_mono.csv  
- stats_givenname.py  
- feature_givenname.py  

  For file 1, it is the csv file for the program to run.  
  For file 2, it generates the plots and statistical model  
  For file 3, it generates the phonetic features, necessary for running analysis.  
