import requests
from bs4 import BeautifulSoup
from time import sleep

file1 = open("output.csv","w")  

for x in range(1,2064): 
    print(x)
    try:
        url = 'https://nlcbresults.com/LottoPlus?DrawNo='+str(x) 
        data = requests.get(url)
        html = BeautifulSoup(data.text, 'html.parser') 
        whiteBalls = html.select('div.Ball60White')
        file1.write(str(x)+","+whiteBalls[0].get_text()+","+whiteBalls[1].get_text()+","+whiteBalls[2].get_text()+","+whiteBalls[3].get_text()+","+whiteBalls[4].get_text()+","+html.select('div.Ball60Yellow')[0].get_text()+",\n")  
    except Exception as e:
        print(e) 

    if(x % 10 == 0):
        sleep(60)

file1.close() 