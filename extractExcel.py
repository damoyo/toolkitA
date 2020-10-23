import xlrd


# encoding if it contains non ascii coding we need chinese
# on demand if the databse is too big dont load all


def read_excel(file_name):
    """
    Create the excel Object to work on
    :param file_name:
    :return: WorkBook Object
    """
    # open the workbook
    workbook = xlrd.open_workbook(file_name, on_demand=True)
    return workbook

def getnames():
    a = read_excel("testdata.xlsx")
    sheet = a.sheet_by_index(0)
    collen = sheet.get_rows()
    collen = sheet.get_rows()
    count = 0
    for value in collen:
        print(value[1])

def getid():
    a = read_excel("testdata.xlsx")
    sheet = a.sheet_by_index(0)
    collen = sheet.get_rows()
    collen = sheet.get_rows()
    count = 0
    for value in collen:
        print (value[0])

def insert_to_database():
    a = read_excel("testdata.xlsx")
    sheet = a.sheet_by_index(0)
    collen = sheet.get_rows()
    ln = len(list(collen))
    rowlen = sheet.row_len(0)
    collen = sheet.get_rows()
    count = 0
    for value in collen:
        sql = "INSERT INTO users(id, name, ID) VALUES(01, %s[0], value[1])" %value
        print(sql)


insert_to_database()
getnames()
getid()