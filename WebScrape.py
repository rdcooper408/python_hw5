from bs4 import BeautifulSoup
import os  
import pdb
import re
from codecs import open
with open('name_date.txt', 'w', "utf-8") as ND:
    ND.write('Name\t')
    ND.write('Date\n')
    for file in os.listdir('.'):
         soup = BeautifulSoup(open(file))
         all_section = soup.find_all(class_='clear-fix right-wide-column')
         for li in all_section:
             div = li.find("div", class_="section")
             seminar_EEP = div.strong
             if seminar_EEP is None or seminar_EEP == 0 or seminar_EEP.string != "EcoEvoPub Series":
                 break
             else:
                 #this gets the name 
                 div = li.find("div", class_="section")
                 seminar_name = div.p
                 if seminar_name is None or seminar_name == 0:
                     name = "no speaker"
                 else:
                     pattern = r"<p>([A-Z]* [A-Z]*)<br/>"
                     name1 = re.search(pattern, str(all_section), re.I)
                     if name1 is None:
                         break
                     else:
                         name = name1.group(1)
                 #this gets the date 
                 div = li.find("div", class_="section")
                 seminar_date = div.h4
                 if seminar_date is None or seminar_date == 0:
                     date = "no speaker"
                 else:    
                     date = seminar_date.string.strip() 
             
                 ND.write(date)
                 ND.write('\t')
                 ND.write(name)
                 ND.write('\n')
    
print "Finished"
