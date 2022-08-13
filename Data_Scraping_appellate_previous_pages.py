import sys
import bs4 as bs
import urllib.request

from cv2 import split
test_url='http://www.supremecourt.gov.bd/web/index.php?page=cause_list.php&menu=00&div_id=1&court_id=1&date1='+'31/2/2022'
sauce=urllib.request.urlopen(test_url)
soup=bs.BeautifulSoup(sauce,'lxml')

td=soup.find_all("td",{"class":"font_e_14"})
count=0
for x in td:
    count=count+1
TD=soup.find_all("td",{"class":"font_e_14"})
TD5=soup.find_all("td",{"class":"font_u_14"})
print(count)



#table_rows=table.find_all('tr')
i=0
c=0
for x in range(0,int(count/4)):
    
   
    
    print(TD[i].string.strip()) 
    i=i+1
    print('------------------------------------------------------')
    col2=TD[i].prettify().split('>')[1].split('<')[0]+TD[i].prettify().split('>')[2].split('<')[0]
    print(col2) 
    i=i+1
    
    print('------------------------------------------------------')
    col3=TD[i].prettify().split('>')[1].split('<')[0]+" vs "+TD[i].prettify().split('>')[3].split('<')[0]
    print(col3) 
    i=i+1
    
    print('------------------------------------------------------')
    col4=TD[i].prettify().split('>')[1].split('<')[0]+" and "+TD[i].prettify().split('>')[3].split('<')[0]
    print(col4) 
    i=i+1
    
    print('------------------------------------------------------')
    print(TD5[c].find_all('td')[1].string) 
    c=c+1
    
    print('------------------------------------------------------')
    
  