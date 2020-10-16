import  xlrd
# encoding if it contains non ascii coding
# on demand if the databse is too big dont load all
def read_excel(file_name):
    # open workbook
    workbook = xlrd.open_workbook(file_name, encoding='cp1252', on_demand = True)

    # open worksheet by name
    worksheet = workbook.sheet_by_name('My_Sheet_Name')

    # open worksheet by index(n)
    worksheet = workbook.sheet_by_index(0)

    # count number of
def number_of_sheets(workbook):
    no_sheets = workbook.nsheets

    # list of the names of the sheets present in the file
def names_of_sheets(workbook):
    sheet_names = workbook.sheet_names()
