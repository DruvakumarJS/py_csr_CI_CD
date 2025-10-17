import xlrd

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter=True

path = r'C:\Users\druva\Downloads\demowebshop_locators (1).xlsx'


#####################################################################################
## LOGIN

login_workbook = xlrd.open_workbook(path)                           ## book object
login_worksheet = login_workbook.sheet_by_name("Sheet2")     ## sheet object
login_rows = login_worksheet.get_rows()                             ## generator object
login_header = next(login_rows)


def login_locators():
    login_data = {}
    for item in login_rows:
        login_data[item[0].value] = (item[1].value, item[2].value)

    return login_data

#NGO

ngo_worksheet = login_workbook.sheet_by_name("ngo")     ## sheet object
ngo_rows = ngo_worksheet.get_rows()                             ## generator object
ngo_header = next(ngo_rows)

def ngo_locators():
    ngo_data = {}
    for item in ngo_rows:
        ngo_data[item[0].value] = (item[1].value, item[2].value)

    return ngo_data

project_worksheet = login_workbook.sheet_by_name("project")     ## sheet object
project_rows = project_worksheet.get_rows()                             ## generator object
project_header = next(project_rows)
def project_locators():
    project_data = {}
    for item in project_rows:
        project_data[item[0].value] = (item[1].value, item[2].value ,item[3].value)

    return project_data

