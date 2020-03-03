"""
Case study:
-----------
A scenario where we receive files with order numbers but we need to provide Test ID as suffix/prefix/new name for the files to be uploaded for client validation.

Note: If this is a daily task for 3-4 resources and continued for more than 4 months.It should be work for automating the above scenario
"""

import openpyxl,os
import glob
import pandas as pd

wb = openpyxl.Workbook()
ws = wb.worksheets[-1]

path=input("Enter the path : ")
os.chdir(path)
main_df=pd.read_excel(path+"\sheet1.xlsx",sheet_name=-1)
req_df=main_df[["IMX","Order"]]
#req_df.dropna(axis=0,inplace=True)
#req_df=req_df.head(5)
req_df.fillna('0',inplace=True)
print(req_df)
#

for file in glob.glob("*.png"):
    name=file[:-4]
    print(name)
    #print(type(name))
    print(type(req_df['Order'][0]))
    try:
        new_name=req_df.loc[req_df['Order'] == int(name),'IMX'].iloc[0]
        #new_name=req_df.loc[req_df['Order'] == name,'IMX'].iloc[0]
        import shutil

        shutil.move(name+'.png', new_name+'.png')
    except:
        print(name+"Not available ")



