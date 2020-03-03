import xlrd
import xlwt

loc = ("C:\\Users\\mkottak\\Downloads\\FireShot\\newusers.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(0, 21):
    # For row 0 and column 0
    email = sheet.cell_value(i, 0)
    firname = sheet.cell_value(i, 1)
    print(email,firname)

