import openpyxl,os
from openpyxl.drawing.image import Image
import glob
import pandas as pd

wb = openpyxl.Workbook()
ws = wb.worksheets[-1]

path=input("Enter the path : ")
os.chdir(path)
main_df=pd.read_excel(path+"\OMS_E2E_Scenarios_Rula_Review.xlsx",sheet_name=-1)
req_df=main_df[["IMX","Order"]]
#req_df.dropna(axis=0,inplace=True)
req_df=req_df.head(5)
req_df.fillna('0',inplace=True)
print(req_df)

for file in glob.glob("*.png"):
    name=file[:-4]
    print(name)
    print(type(name))
    print(type(req_df['Order'][0]))
    print(req_df.loc[req_df['Order']==name,'IMX'])
    #print("new: "+str(new_name))
#C:\Users\mkottak\Pictures\sample
