from bs4 import BeautifulSoup
from cv2 import split
from pyparsing import col
import requests
import re

url = f'http://www.supremecourt.gov.bd/web/?page=bench_list.php&menu=00&div_id=2&date1=24/07/2022'
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
#page_text1 = doc.find(class_="link_e10r").font.string
elements = doc.find_all(class_="font_e_14")
i=0
c=2
for x in elements:
	
	table_elements = str(doc.find_all(class_="font_e_14")[i].td.font)
	col1=table_elements.split("<")[3].strip("/font>").strip()
	i=i+1
	i=i+1
	col2 = doc.find_all(class_="link_e10ru")[c].a.string
	c=c+1
	pull3=doc.find_all(class_="font_e_14")[i]
	p1=str(pull3).split(">")[1].strip()
	p1=p1.strip()
	p2=str(pull3).split(">")[2]
	p2=p2.strip()
	p3=str(pull3).split(">")[3]
	col3=p1+p2+p3
	col3=col3.replace("<br/","  ")
	i=i+1
	col4=doc.find_all(class_="font_e_14")[i].div
	col4=str(col4).strip("</div>").split(">")[1].strip("<br/")
	cleantext = BeautifulSoup(page, "lxml").text
	#print(cleantext)

	print(col1)
	print("-----------------------------------------------------------------------------")
	print(col2) 
	print("-----------------------------------------------------------------------------")
	print(col3)
	print("-----------------------------------------------------------------------------")
	print(col4)
	
	
	if(int(col1)>50):break
	i=i+1	

 