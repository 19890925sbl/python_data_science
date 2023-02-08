dictionary={'a':1,'b':2,'c':3,'d':4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k:v**2 for (k,v) in dictionary.items()}

{k.upper():v for(k,v) in dictionary.items()}

{k.upper():v*2 for (k,v) in dictionary.items()}
#before
['total','speeding','alcohol','not_distracted','no_previous','ins_premium','ins_losses','abbrev']
#after
['TOTAL','SPEEDING','ALCOHOL','NOT_SISTRACTED','NO_PREVIOUS','INS_PREMIUM','INS_LOSSES','ABBREV']

import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A=[]
for col in df.columns:
    A.append(col.upper())

df.columns=A
df=sns.load_dataset("car_crashes")
df.columns=[col.upper() for col in df.columns]