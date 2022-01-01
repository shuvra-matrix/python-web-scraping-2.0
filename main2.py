import pandas as pd
import requests
import csv
rows = []

data = pd.read_csv("urls.csv")
web_data = {(data_row["URL_1"], data_row["URL_2"]): data_row for (index, data_row) in data.iterrows()}
fields = ['url', 'result'] 
filename = "web_result.csv"
           
for i in web_data:
    date = web_data[i]
    first_url = data['URL_1']
    snd_url = data['URL_2']
    