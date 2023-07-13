import numpy as np
import pandas as pd
import boto3
#Data Source
import yfinance as yf
from datetime import datetime

import plotly.graph_objs as go
equity_details = pd.read_csv('EQUITY_L.csv')
for name in equity_details.SYMBOL:
    try:
        data = yf.download(f'{name}.NS',period='1d')
        data.to_csv(f'./Incremental data/{name}.csv') # Data will be stored in data folder
    except Exception as e:
        print(f'{name} ===> {e}')
# current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

 
# # convert datetime obj to string
# str_current_datetime = str(current_datetime)
 
# # create a file object along with extension
# file_name = str_current_datetime+".csv"

# s3_client = boto3.client('s3')
# s3_client.upload_file(r'F:\Software\danish\Alapex\Incremental Data\\'+file_name,"landing-bucket-alapex",file_name)
