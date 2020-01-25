import openpyxl,os
from openpyxl.drawing.image import Image
import glob

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

path=input("Enter the path : ")
os.chdir(path)

for file in glob.glob("*.png"):
    name=file[:-4]
    ws=wb.create_sheet(title=name)

    img = openpyxl.drawing.image.Image(name+".png")
    ws.add_image(img,'A1')

wb.save('out.xlsx')

