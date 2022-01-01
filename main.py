import pandas as pd
import requests
import csv
from scrap import scrap
rows = []
result_1 =""
result_2 = ""
fields = ['URL_1 ', 'URL_2 ' , 'TITLE MATCH RESULT' , 'DESCRIPTION MATCH RESULT'] 
filename = "result_file.csv"
data = pd.read_csv("urls.csv")
web_data = {(data_row["URL_1"], data_row["URL_2"]): data_row for (index, data_row) in data.iterrows()}
filename = "web_result.csv"  
for i in web_data:
        first_url = i[0]
        first_data = scrap(first_url)
        snd_url = i[1]
        second_data = scrap(snd_url)
        if first_data[0] == second_data[0]:
                result_1 = 'Matched'
        else:
                result_1 = "Unmatched"
        if first_data[1] == second_data[1]:
                result_2 = 'Matched'
        else:
                result_2 = "Unmatched"
        result_list = [first_url,snd_url, result_1,result_2]
        rows.append(result_list)


with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)

                

        
