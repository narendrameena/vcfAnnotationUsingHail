#@author narumeena
#@description extrating variants from a input file into vcf format

import pandas as pd
from itertools import chain



def getDataAsDataFrame(filePath):
    return pd.DataFrame.from_csv(filePath)


df = getDataAsDataFrame("data/mappedMutationTosORFs.csv")

df.index = range(4408)

df.reset_index(drop=True)

df['INFO'] = df.apply(lambda x: ';'.join(
    [unicode(y) for y in x if not pd.isnull(y)]), axis=1) # concating all columns 

print( df[:5])
print(df["ChrN'.1"])
print(df["Start'.1"])
print(df["WT_SEQ'"])
print(df["MUT_SEQ'"])
print(df["INFO"])
print(df.columns.values.tolist())

# vcf format CHROM POS REF ALT INFO

#writing in vcf format
vcf =pd.DataFrame({'CHROM': df["ChrN'.1"],
     'POS': df["Start'.1"],
     'REF': df["WT_SEQ'"],
     'ALT': df["MUT_SEQ'"],
     'INFO': df["INFO"]
    })

print(vcf[:5])

#vcf.to_csv(r'mapped.vcf', header=True, index=None, sep=' ', mode='a')

#print(df["ChrN'.1"])