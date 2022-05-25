import pandas as pd
from pandas import ExcelWriter
# def result(s):
# 	charSet = set()
# 	l = 0
# 	res = 0 
# 	for r in range(len(s)):
# 		while s[r] in charSet:
# 			charSet.remove(s[l])
# 			l += 1
# 		charSet.add(s[r])
# 		res = max(res,len(charSet))
# 	return res

# print(result("abcb"))

# mon_dic = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}


# print(mon_dic['Jan'])
import glob,os
pattern ='*.xlsx'
xllis=glob.glob(pattern)

a = list(map(os.path.basename, glob.glob(r'D:\Office\Reports\MOCK\Reports_with_Script\Selected Product Depot wise only sales value\data\**\*.csv', recursive=True)))

csv_files = glob.glob(r'D:\Office\Reports\MOCK\Reports_with_Script\Selected Product Depot wise only sales value\data\**\*.csv', recursive=True)

all_data = pd.DataFrame()
for x in csv_files:
	(_, f_name) = os.path.split(x)
	(f_short_name, _) = os.path.splitext(f_name)
	print(f_short_name)
	df = pd.read_csv(x)
	df = df.iloc[1: , :]
	df.insert(0, 'Month', f_short_name)



	all_data = all_data.append(df,ignore_index=True,sort=False)
df.columns =['Name', 'Code', 'Age', 'Weight']
writer = pd.ExcelWriter('mm.xlsx', engine='xlsxwriter') 
all_data.to_excel(writer, sheet_name='Sheet1',index=False,header=None)
writer.save()
