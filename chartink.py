import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from google_sheet import clean_up, update_cell, update_google_sheet
from nse_data import updatenseIndex,maketStatus,marketAdvacneDecline
from back_end_chart_ink import chartinkLogicBankend




def trasferDataToGoogleSheet():

    URL = 'https://chartink.com/screener/process'

    # Initialize prev_data as None before the loop
    print("started")
   
    while True:

        market = maketStatus()
       
        updatenseIndex()
        marketAdvacneDecline()
 
        try:
            title = "Compounding Funda"
            sub_title = "©SnT Solution - 8080105062"
            update_cell(cell='A3',data=title,sheetname='DashBoard')
            update_cell(cell='A28',data=sub_title,sheetname='DashBoard')
            # Condtion 1
            conditionName = "MUST TRY" # change name Here
            conditionNameLocation = "B4"
            # Put condition here
            CONDITION1 = {"scan_clause": "( {cash} ( ( {cash} ( latest macd line( 13 , 8 , 5 ) > latest macd signal( 13 , 8 , 5 ) and 1 day ago  macd line( 13 , 8 , 5 ) <= 1 day ago  macd signal( 13 , 8 , 5 ) and 1 day ago macd line( 13 , 8 , 5 ) < 1 day ago macd signal( 13 , 8 , 5 ) and latest rsi( 14 ) >= 40 and latest volume >= latest sma( latest volume , 20 ) and market cap >= 500 ) ) ) ) "}
            row_to_start ='A3'
            row_to_clean = 'A3:D'
            chartinkLogicBankend(condition=CONDITION1,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 2
        try:
            # Condtion 2
            conditionName = "GROWING" # change name Here
            CONDITION2 = {"scan_clause": "( {cash} ( ( {cash} ( quarterly close >= 1 quarter ago close * 1.07 and 1 quarter ago close >= 2 quarter ago close * 1.07 and 2 quarter ago close > 3 quarter ago close * 1.07 and 3 quarter ago close > 4 quarters ago close * 1.07 and market cap >= 750 and market cap <= 5000 and latest close > latest open and latest volume > 1 day ago volume ) ) ) ) "} 
            row_to_start ='F3'
            row_to_clean = "F3:I"
            conditionNameLocation = "F4"
            chartinkLogicBankend(condition=CONDITION2,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 3        
        try:
            # condition 3
            conditionName = "B/O TRADE"
            CONDITION3 = {"scan_clause": "( {cash} ( ( {cash} ( ( {cash} ( abs( latest high - latest low ) > abs( 1 day ago high - 1 day ago low ) and abs( latest high - latest low ) > abs( 2 days ago high - 2 days ago low ) and abs( latest high - latest low ) > abs( 3 days ago high - 3 days ago low ) and abs( latest high - latest low ) > abs( 4 days ago high - 4 days ago low ) and latest close > latest open and latest close > weekly open and latest close > monthly open and latest low > 1 day ago close - abs( 1 day ago close / 222 ) and latest adx( 14 ) >= 15 and latest adx di positive( 14 ) > latest adx di negative( 14 ) and 1 day ago  adx di positive( 14 ) <= 1 day ago  adx di negative( 14 ) ) ) ) ) ) )"}
            row_to_start ='k3'
            row_to_clean = "k3:N"
            conditionNameLocation = "J4"
            chartinkLogicBankend(condition=CONDITION3,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 4    
        try:
            # condition 4
            conditionName = "STRONG UPTREND"
            CONDITION4 = {"scan_clause": "( {cash} ( ( {cash} ( weekly rsi( 14 ) >= 60 and monthly rsi( 14 ) >= 60 and latest rsi( 14 ) >= 40 and latest rsi( 14 ) < 60 and latest rsi( 14 ) > 1 day ago rsi( 14 ) and 1 day ago rsi( 14 ) < 2 days ago rsi( 14 ) and 2 days ago rsi( 14 ) < 3 days ago rsi( 14 ) and latest volume >= 1 day ago volume and market cap >= 500 ) ) ) )" }
            row_to_start ='P3'
            row_to_clean = "P3:S"
            conditionNameLocation = "N4"
            chartinkLogicBankend(condition=CONDITION4,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e) 
        # Condtion 5    
        try:
            # condition 5
            conditionName = "BLaster"
            CONDITION5 = {"scan_clause": "( {cash} ( ( {cash} ( latest volume > 1 day ago max( 255 , latest volume ) and latest close >= latest open ) ) ) )" }
            row_to_start ='U3'
            row_to_clean = "U3:X"
            conditionNameLocation = "B16"
            chartinkLogicBankend(condition=CONDITION4,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 6    
        try:
            # condition 6
            conditionName = "MOMENTUM BUY"
            CONDITION6 = {"scan_clause": "( {cash} ( ( {57960} ( ( {cash} ( latest avg true range( 14 ) > 1 day ago avg true range( 14 ) and 1 day ago avg true range( 14 ) <= 2 days ago avg true range( 14 ) and 2 days ago avg true range( 14 ) <= 3 days ago avg true range( 14 ) and 3 days ago avg true range( 14 ) <= 4 days ago avg true range( 14 ) and 4 days ago avg true range( 14 ) <= 5 days ago avg true range( 14 ) and 5 days ago avg true range( 14 ) <= 6 days ago avg true range( 14 ) and 6 days ago avg true range( 14 ) <= 7 weeks ago avg true range( 14 ) and latest volume >= 1 day ago volume and latest volume >= latest sma( latest volume , 20 ) and latest volume >= 25000 and latest close > latest open and market cap > 500 ) ) ) ) ) )"}
            row_to_start ='Z3'
            row_to_clean = "Z3:AC"
            conditionNameLocation = "F16"
            chartinkLogicBankend(condition=CONDITION6,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 7    
        try:
            # condition 
            conditionName = "FUTURE WINNER"
            CONDITION7 = {"scan_clause": "( {cash} ( ( {cash} ( latest close >= latest ema( latest close , 20 ) and latest ema( latest close , 20 ) < latest ema( latest close , 50 ) and latest ema( latest close , 20 ) > 1 day ago ema( latest close , 20 ) and market cap >= 20 and latest volume > 1 day ago volume and latest volume > 2 days ago volume and latest close >= 20 and latest close >= 1 day ago close and latest volume >= 50000 and latest close / weekly max( 52 , weekly high ) * 100 > 75 ) ) ) ) "}
            row_to_start ='AE3'
            row_to_clean = "AE3:AH"
            conditionNameLocation = "J16"
            chartinkLogicBankend(condition=CONDITION7,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 8    
        try:
            # condition 8
            conditionName = "SURPRISE MOVE"
            CONDITION8 = {"scan_clause": "( {cash} ( ( {cash} ( latest open > 1 day ago close * 1.03 and latest volume > 1 day ago volume ) ) ) )"}
            row_to_start ='AJ3'
            row_to_clean = "AJ3:AM"
            conditionNameLocation = "N16"
            chartinkLogicBankend(condition=CONDITION8,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # print(market)    
        if(market == 'Closed' or market == "Close"):
            print(f"Market is {market}")
            return {"Market Status" : "hello"}
    # Sleep for 5 minutes``
        
    time.sleep(100) # 300 seconds = 5 minutes
