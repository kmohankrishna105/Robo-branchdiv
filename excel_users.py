import xlrd
import xlwt

def extract_users():
    # Give the location of the file
    loc = ("C:\\Users\\mkottak\\Downloads\\FireShot\\newusers.xls")

    # To open Workbook

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    for i in range (0,2):
        # For row 0 and column 0
        email=sheet.cell_value(i, 0)
        firname=sheet.cell_value(i, 1)
        lasname=sheet.cell_value(i, 2)
        address1=sheet.cell_value(i, 3)
        city = sheet.cell_value(i, 4)
        code= sheet.cell_value(i, 5)
        print(email)


