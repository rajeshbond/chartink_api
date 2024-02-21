import gspread 
from google.oauth2.service_account import Credentials
import json

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
    ]

cred = Credentials.from_service_account_file('keys.json',scopes = scopes)

client = gspread.authorize(cred)

sheet_id = '1ZGk_XUTN-AyyJ6jjXKbG_OWWrZUVPcj26zlHWfH6m_c' 
workBook = client.open_by_key(sheet_id)
# sheets = map(lambda x:x.title, workBook.worksheets())  to display the sheet name 
# sheet = workBook.worksheet('Hello World')
# sheet.update_title('Hello World')
# sheet.update_acell('A1',"Hello Rajesh ") # acell with cell name 
# sheet.update_cell(1,1, 'Rajesh Bondgilwar') # cell with index 
# sheet.format('A1',{'textFormat':{'bold':True}})
# print(list(sheets))
# values_list = sheet.sheet1.row_values(1)
# print(values_list)



worksheet_list = map(lambda x:x.title , workBook.worksheets())

# # new_worksheets_name = 'Values'

# if new_worksheets_name in worksheet_list:
#     sheet = workBook.worksheet(new_worksheets_name)
# else:
#     sheet = workBook.add_worksheet(new_worksheets_name, rows=10, cols=10)

# sheet.clear() 
# sheet.update(f'A1:C{len(values)}', values)

def update_google_sheet (row,data,range_to_clear,sheetname = 'Hello World'):
    sheet = workBook.worksheet(sheetname)
    values = data.values.tolist()
    # sheet.clear()
    # range_to_clear = 'F3:I24'
    # Clear the content of the range
    sheet.batch_clear([range_to_clear])

    # sheet.update(row, [['Symbol', 'Percentage Change', 'Close', 'Volume']] + values)
    sheet.update(row, values)
def update_cell(cell,data,sheetname):
    sheet = workBook.worksheet(sheetname)
    sheet.update(cell,[[data]])

def clean_up (range_to_clear,sheetname = 'Hello World'):
    sheet = workBook.worksheet(sheetname)    
    sheet.batch_clear([range_to_clear])



