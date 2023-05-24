import requests
from bs4 import BeautifulSoup
from time import sleep

output = open("cash_pot_output.csv","a")  

run_no_file = open("NEXT_RUN_NUMBERS.txt","r+") 
CURRENT_RUN_NUMBER = int(run_no_file.read()) 
run_no_file.close()

if CURRENT_RUN_NUMBER == 1:
    output.write("DRAW_ID,DAY,MONTH,DATE,YEAR,BALL1,BALL2,BALL3,BALL4,BALL5,Multiplier\n")  
 
for x in range(CURRENT_RUN_NUMBER,10000000000000000000000):  
    try:   
        url = 'https://nlcbresults.com/CashPot?DrawNo='+str(x)  
        data = requests.get(url)
        html = BeautifulSoup(data.text, 'html.parser') 
        whiteBalls = html.select('div.Ball60White')
        multiplier = html.select("div.Ball60Green")
        date = html.select('strong')[39].get_text().replace(" ",",") 
        
        output.write(str(x)+","+date+","+whiteBalls[0].get_text()+","+whiteBalls[1].get_text()+","+whiteBalls[2].get_text()+","+whiteBalls[3].get_text()+","+whiteBalls[4].get_text()+","+multiplier[0].get_text()+",\n")  
        CURRENT_RUN_NUMBER = CURRENT_RUN_NUMBER + 1
        print(x)

    except Exception as e: 
        print(x)
        print(str(e)) 
        exit()

    if(x % 10 == 0):
        sleep(60)

run_no_file = open("NEXT_RUN_NUMBERS.txt","w") 
run_no_file.write(str(CURRENT_RUN_NUMBER)) 
run_no_file.close()

output.close() 

 