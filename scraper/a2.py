import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup

url=('https://in.finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI')
r=requests.get(url)
web_content=BeautifulSoup(r.text,'lxml')
web_content=web_content.find('div',{"class": 'D(ib) Mend(20px)'})
web_content=web_content.find('span').text

for i in range(1,100):
    price=[]
    col=[]
    time_stamp=datetime.datetime.now()
    time_stamp=time_stamp.strftime("%Y-%m-%d %H:%M:%S")

    price.append(web_content)
  
    col=[time_stamp]
    col.extend(price)
    df=pd.DataFrame(col)
    df=df.T
    df.to_csv('real time stock data.csv',mode='a',header=False)

    print(col)

