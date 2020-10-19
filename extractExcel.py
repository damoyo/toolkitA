import  xlrd
# encoding if it contains non ascii coding we need chinese
# on demand if the databse is too big dont load all
def read_excel(file_name):
    # open workbook
    workbook = xlrd.open_workbook(file_name, encoding='cp1252', on_demand = True)

    # open worksheet by name
    worksheet = workbook.sheet_by_name('My_Sheet_Name')

    # open worksheet by index(n)
    worksheet = workbook.sheet_by_index(0)

    # count number of workbooks
def number_of_sheets(workbook):
    no_sheets = workbook.nsheets

    # list of the names of the sheets present in the file
def names_of_sheets(workbook):
    sheet_names = workbook.sheet_names()

    # Value of 1st row and 1st column needs to be iterated
def get_data_cell(sheet):
    """
    if sheet.cell(0, 0).value == xlrd.empty_cell.value:
    # Do something
    :param sheet:
    :return:
    """

    sheet.cell(0, 0).value
