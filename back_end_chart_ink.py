
import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import pytz
from pprint import pprint
from google_sheet import clean_up, update_google_sheet,update_cell

URL = 'https://chartink.com/screener/process'
async def  chartinkLogicBankend(condition,row_to_start,row_to_clean,sheetname,conditionName,conditionNameLocation):
    # print(conditionName)
    # print(conditionNameLocation)
    try:
        with requests.session() as s:
            rawData = s.get(URL)
            soup = bs(rawData.content,"lxml")
            meta = soup.find('meta', {"name":"csrf-token"})['content']
            header = {"X-Csrf-Token": meta}
            responseData_scan1 = await s.post(url=URL , headers= header , data=condition, timeout=10000)
            if responseData_scan1.content:
                data = responseData_scan1.json()
                stock = data['data']
                stock_list = pd.DataFrame(stock)
                if stock_list.empty:
                     clean_up(range_to_clear=row_to_clean,sheetname=sheetname)
                     return
              
                stock_list_sorted = stock_list.sort_values(by='per_chg', ascending=False)
                update_cell(conditionNameLocation,conditionName,sheetname="DashBoard")   
                update_google_sheet(row_to_start,stock_list_sorted[['nsecode','per_chg','close','volume']],range_to_clear=row_to_clean,sheetname=sheetname)
                
    except Exception as e:
            clean_up(range_to_clear=row_to_clean)
            print(e)

            
