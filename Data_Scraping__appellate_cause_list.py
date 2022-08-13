from cgitb import strong
import mysql.connector
from bs4 import BeautifulSoup
from cv2 import split
from pyparsing import col
import requests
import re

from mysql.connector import Error


        
url = f'http://www.supremecourt.gov.bd/web/index.php?page=cause_list.php&menu=00&div_id=1&court_id=1&date1=26/07/2022'
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
#page_text1 = doc.find(class_="link_e10r").font.string
elements = doc.find_all(class_="font_e_14")
i=0
c=0
for TD in elements: c=c+1

for TD in elements:
    

    if(i>20):i=i-1

    Heading=doc.find_all(class_="font_e_14")[i]
    i=i+1 
    col1=doc.find_all(class_="font_e_14")[i].string
    col1=str(col1).strip()
    i=i+1
    col2=doc.find_all(class_="font_e_14")[i]
    col2=str(col2).split(">")[1] + str(col2).split(">")[2]
    col2=col2.split("<br")
    col2=col2[0].strip()+": "+col2[1]
    i=i+1
    col3=doc.find_all(class_="font_e_14")[i]
    col3=str(col3).split(">")[1].split("<")[0]+" VS " +str(col3).split(">")[3].split("<")[0]
    i=i+1
    col4=doc.find_all(class_="font_e_14")[i]
    col4=str(col4).split(">")[1].split("<")[0]+" and "+str(col4).split(">")[3].split("<")[0]
    i=i+1
    col5=doc.find_all(class_="font_e_14")[i]
    col5=str(col5).split(">")[6].split("<")[0]
    i=i+1
    col6=doc.find_all(class_="font_e_14")[i]
    i=i+1

    print(col1)
    print(col2)
    print(col3)
    print(col4)
    print(col5)
    print(i)

    if(i>c-1):break

  
   


