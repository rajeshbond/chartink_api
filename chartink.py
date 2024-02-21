import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from google_sheet import clean_up, update_google_sheet
from nse_data import updatenseIndex,maketStatus,marketAdvacneDecline
from back_end_chart_ink import chartinkLogicBankend

def trasferDataToGoogleSheet():

    URL = 'https://chartink.com/screener/process'

    # Initialize prev_data as None before the loop
    print("started")
    while True:

        marketStatus = maketStatus()
        updatenseIndex()
        marketAdvacneDecline()
        with requests.session() as s:
            rawData = s.get(URL)
            soup = bs(rawData.content,"lxml")
            meta = soup.find('meta', {"name":"csrf-token"})['content']
            header = {"X-Csrf-Token": meta}
            
            # Scan name and condition to pass 
            # Condtion 1
            try:
                # Condtion 1
                conditionName = "Previous Day"
                conditionNameLocation = "B4"
                CONDITION1 = {"scan_clause": "( {cash} ( 1 day ago close > 1 day ago sma( 1 day ago high , 56 ) and [-1] 15 minute close > [-1] 15 minute sma( [-1] 15 minute high , 56 ) and 1 day ago low <= 1 day ago sma( 1 day ago high , 56 ) and latest close > 1 day ago high and latest close > latest supertrend( 18 , 1.5 ) and 1 day ago volume > 100000 and 1 day ago volume > 2 days ago volume and latest adx di positive( 14 ) > latest adx di negative( 14 ) and latest adx di positive( 14 ) > latest adx( 14 ) and latest adx( 14 ) > 20 ) ) "} # need to be dynamic
                row_to_start ='A3'
                row_to_clean = 'A3:D'
                chartinkLogicBankend(condition=CONDITION1,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            except Exception as e:
                print(e)
            # Condtion 2
            try:
                # Condtion 2
                conditionName = "Flash Sale"
                CONDITION2 = {"scan_clause": "( {cash} ( latest sma( latest high , 56 ) > 1 day ago sma( 1 day ago high , 56 ) and latest close > latest sma( latest high , 56 ) and latest low <= latest sma( latest high , 56 ) and latest rsi( 9 ) > latest ema( latest rsi( 9 ) , 3 ) and latest wma( latest rsi( 9 ) , 21 ) < latest ema( latest rsi( 9 ) , 3 ) and 1 day ago volume > 200000 and latest close > latest supertrend( 21 , 1.5 ) and latest close > 1 day ago high ) )"} 
                row_to_start ='F3'
                row_to_clean = "F3:I"
                conditionNameLocation = "F4"
                chartinkLogicBankend(condition=CONDITION2,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            except Exception as e:
                print(e)
            # Condtion 3        
            try:
                # condition 3
                conditionName = "Fast Movers"
                CONDITION3 = {"scan_clause": "( {cash} ( latest wma( latest rsi( 9 ) , 21 ) > 51 and latest rsi( 9 ) > latest ema( latest rsi( 9 ) , 5 ) and 1 day ago  rsi( 9 ) <= 1 day ago  ema( latest rsi( 9 ) , 5 ) and 1 day ago volume > 200000 and latest close > 20 and yearly debt equity ratio < 0.25 ) ) "}
                row_to_start ='k3'
                row_to_clean = "k3:N"
                conditionNameLocation = "J4"
                chartinkLogicBankend(condition=CONDITION3,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            except Exception as e:
                print(e)
            # Condtion 4    
            try:
                # condition 4
                conditionName = "Must Try"
                CONDITION4 = {"scan_clause": "( {cash} ( latest close > latest sma( latest high , 56 ) and 1 day ago  close <= 1 day ago  sma( latest high , 56 ) and yearly debt equity ratio < 0.4 and yearly return on capital employed percentage > 15 and latest wma( latest rsi( 9 ) , 21 ) > 1 day ago wma( latest rsi( 9 ) , 21 ) ) ) "}
                row_to_start ='P3'
                row_to_clean = "P3:S"
                conditionNameLocation = "N4"
                chartinkLogicBankend(condition=CONDITION4,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            except Exception as e:
                print(e) 
            # Condtion 5    
            try:
                # condition 5
                conditionName = "RSI_Blast"
                CONDITION5 = {"scan_clause": "( {cash} ( latest close > latest supertrend( 18 , 1.5 ) and latest rsi( 9 ) > latest wma( latest rsi( 9 ) , 21 ) and latest rsi( 9 ) > 65 and 1 day ago  rsi( 9 ) <= 65 and latest low <= latest sma( latest high , 56 ) and latest close > latest sma( latest high , 56 ) and 1 day ago volume > 100000 and yearly debt equity ratio < 0.4 and yearly return on capital employed percentage > 12 ) ) "}
                row_to_start ='U3'
                row_to_clean = "U3:X"
                conditionNameLocation = "B16"
                chartinkLogicBankend(condition=CONDITION4,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            except Exception as e:
                print(e)
            # Condtion 6    
            try:
                # condition 6
                conditionName = "New Trade"
                CONDITION6 = {"scan_clause": "( {cash} ( ( latest high - latest low ) > ( 1 day ago high - 1 day ago low ) and( latest high - latest low ) > ( 2 days ago high - 2 days ago low ) and( latest high - latest low ) > ( 3 days ago high - 3 days ago low ) and( latest high - latest low ) > ( 4 days ago high - 4 days ago low ) and( latest high - latest low ) > ( 5 days ago high - 5 days ago low ) and latest close > latest open and latest close > 1 day ago close and weekly close > weekly open and monthly close > monthly open and 1 day ago volume > 10000 and latest sma( close,20 ) > latest sma( close,50 ) and latest sma( close,50 ) > latest sma( close,200 ) and latest close > 200 ) )"}
                row_to_start ='Z3'
                row_to_clean = "Z3:AC"
                conditionNameLocation = "F16"
                chartinkLogicBankend(condition=CONDITION6,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            except Exception as e:
                print(e)
            # Condtion 7    
            try:
                # condition 
                conditionName = "Best Trade"
                CONDITION7 = {"scan_clause": "( {cash} ( latest low < latest ema( latest high , 56 ) and latest close > latest ema( latest high , 56 ) and 1 day ago  close <= 1 day ago  ema( latest high , 56 ) and 1 day ago volume > latest ema( latest close , 20 ) * 2 and latest volume > 100000 and 1 day ago close < latest close and latest rsi( 9 ) > latest ema( latest rsi( 9 ) , 3 ) and latest ema( latest rsi( 9 ) , 3 ) > latest wma( latest rsi( 9 ) , 21 ) and weekly ema( weekly rsi( 9 ) , 3 ) > weekly wma( weekly rsi( 9 ) , 21 ) and latest close > 1 day ago high and latest rsi( 9 ) > 1 day ago rsi( 9 ) * 1.25 and latest ema( latest close , 56 ) > latest sma( latest close , 200 ) ) ) "}
                row_to_start ='AE3'
                row_to_clean = "AE3:AH"
                conditionNameLocation = "J16"
                chartinkLogicBankend(condition=CONDITION7,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            except Exception as e:
                print(e)
            # Condtion 8    
            try:
                # condition 8
                conditionName = "Important"
                CONDITION8 = {"scan_clause": "( {cash} ( latest close > latest sma( latest close , 20 ) and 1 day ago  close <= 1 day ago  sma( latest close , 20 ) and latest close > latest sma( latest close , 50 ) and 1 day ago  close <= 1 day ago  sma( latest close , 50 ) and latest close > latest ema( latest high , 9 ) and 1 day ago  close <= 1 day ago  ema( latest high , 9 ) and latest volume > 100000 and latest volume > latest sma( latest volume , 20 ) * 1.25 and latest ema( latest rsi( 9 ) , 3 ) > latest wma( latest rsi( 9 ) , 21 ) and 1 day ago  ema( latest rsi( 9 ) , 3 )<= 1 day ago  wma( latest rsi( 9 ) , 21 ) ) ) "}
                row_to_start ='AJ3'
                row_to_clean = "AJ3:AM"
                conditionNameLocation = "N16"
                chartinkLogicBankend(condition=CONDITION8,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
            except Exception as e:
                print(e)
            print(marketStatus)    
            if(marketStatus == 'Closed'):
                print("Market is Cloased")
                break
        # Sleep for 5 minutes``
        time.sleep(10)  # 300 seconds = 5 minutes