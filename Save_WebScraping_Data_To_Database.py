import mysql.connector
from bs4 import BeautifulSoup
from cv2 import split
from pyparsing import col
import requests
import re

from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='db',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
                
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
            if(int(col1)>50):break
            i=i+1	
            mySql_insert_query = """INSERT INTO `cause_list_high_court_division`(`SI`, `Court_Name`, `Honorable_Judges'Name`, `Jurisdictions`)  
                                VALUES (%s, %s, %s, %s) """

            record = (col1, col2, col3, col4)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print("Record inserted successfully into Laptop table")

cursor.close()
connection.close()
print("MySQL connection is closed")
