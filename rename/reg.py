#!/usr/bin/python
'''
change names.csv for replacements, but don't change the first line(old new headers)
'''
import csv
import re
rep={}
#####READ CSV FILE ###########
with open('names.csv') as csvfile: 
    reader = csv.DictReader(csvfile)
    for row in reader:
        rep[row['old']]=row['new']
##########################
      

# use these three lines to do the replacement
rep = dict((re.escape(k), v) for k, v in rep.iteritems())

pattern = [r'\b'+key+r'\b' for key in rep.keys()]
pattern = re.compile("|".join(pattern))

f=open('mml.txt','r') #OPEN ORIGINAL MML SCRIPT
text=f.read()
f.close()

text=pattern.sub(lambda m: rep[re.escape(m.group(0))], text) #SUBSTITUTE


final=open('mml_edited.txt','w') #FINAL GENERATED FILE
final.write(text)
final.close()

