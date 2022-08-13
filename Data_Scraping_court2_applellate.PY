
import sys
import bs4 as bs
import urllib.request

from cv2 import split
import time

from_date ='7/7/2022'
to_date='2/8/2022'
FD=from_date.split('/')[0]
FM=from_date.split('/')[1]
FY=from_date.split('/')[2]
TD=to_date.split('/')[0]
TM=to_date.split('/')[1]
TY=to_date.split('/')[2]




print(int(TY))
print(int(TM))
print(int(TD))
print(int(FY))
print(int(FM))
print(int(FD))
fd=int(FD)
day=32 
for z in range(int(FY),int(TY)+1):
    
    for y in range(int(FM),int(TM)+1):
     
       
        if(int(FM)==int(TM)):
            day=int(TD)
            print("here is the day__________________-----------------") 
            print(day)
            
           
        for x in range(fd,day+1):
            s=str(x)+'/'+str(y)+'/'+str(z)
            print(s)
            
            test_url='http://www.supremecourt.gov.bd/web/index.php?page=cause_list.php&menu=00&div_id=1&court_id=4&date1='+s
            sauce=urllib.request.urlopen(test_url)
            soup=bs.BeautifulSoup(sauce,'lxml')

            td=soup.find_all("td",{"class":"font_e_14"})
            count=0
            for x in td:
                count=count+1
            TD=soup.find_all("td",{"class":"font_e_14"})
            TD5=soup.find_all("td",{"class":"font_u_14"})
            print(count)



            
        fd=1   
        
    




   