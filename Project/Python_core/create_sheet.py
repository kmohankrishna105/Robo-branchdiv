import os,glob
import openpyxl


wb = openpyxl.Workbook()
path=input("Enter the path : ")
os.chdir(path)

for file in glob.glob("*.png"):
    name=file[:-4]
    wb.create_sheet(title=name)

wb.save(path+"/day.xlsx")



