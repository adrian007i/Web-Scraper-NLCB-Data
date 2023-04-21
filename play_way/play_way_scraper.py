import requests
from bs4 import BeautifulSoup
from time import sleep

output = open("play_way_output.csv","a")  

run_no_file = open("NEXT_RUN_NUMBERS.txt","r+") 
CURRENT_RUN_NUMBER = int(run_no_file.read()) 
run_no_file.close()

if CURRENT_RUN_NUMBER == 1:
    output.write("DRAW_ID,DAY,MONTH,DATE,YEAR,NAME,BALL1,BALL2,BALL3,BALL4,\n")  
 
for x in range(CURRENT_RUN_NUMBER,5):  
    try:   
        url = 'https://nlcbresults.com/PlayWhe?DrawNo='+str(x) 
        print(url)
        data = requests.get(url)
        html = BeautifulSoup(data.text, 'html.parser') 
        whiteBalls = html.select('span.Ball40White') 
        
        date = html.select('strong')[39].get_text().replace(" ",",") 
        name = html.select('strong')[40].get_text()  
        output.write(str(x)+","+date+","+name+","+whiteBalls[0].get_text()+","+whiteBalls[1].get_text()+","+whiteBalls[2].get_text()+","+whiteBalls[3].get_text()+",\n")  
        CURRENT_RUN_NUMBER = CURRENT_RUN_NUMBER + 1
        

    except Exception as e: 
        print(str(e))
        exit()

    if(x % 10 == 0):
        sleep(60)

run_no_file = open("NEXT_RUN_NUMBERS.txt","w") 
run_no_file.write(str(CURRENT_RUN_NUMBER)) 
run_no_file.close()

output.close() 

 