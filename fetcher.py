try:
    import urllib2
except:
    print "urllib2 is not installed"
try:
    from bs4 import BeautifulSoup as BS
except:
    print "BeautifulSoup4 is not installed"

import os
from subprocess import call


head_link="http://www.kissanime.com/"
anime='Anime/'
anime_name="One-Piece"
tot_link=head_link+anime+anime_name


soup = BS(urllib2.urlopen(tot_link).read())

table = soup.find('table', {'class': 'listing'})

rows=[]
for r in table.findAll("tr")[1:]:
    link = r.find('a')
    rows.append(link)
  
rows=rows[::-1][:-1]



def download(link,name=None):
    try:
        f=open('.tmp.txt','w')
        f.write(link)
        f.write('\n')
        if name !=None:
            f.write(' out=')
            f.write(name)
            f.write('\n')
        f.close()
        call(["aria2c",'-c','true','-x','16','-j','10','-i','.tmp.txt'])
        os.rmdir('.tmp.txt')
        return 1
    except:
        return 0

#print len(rows)
for i in rows:
    #print "#########"
    #print i['href']
    #print i['title']
    #print i.contents[0].strip()
    link= head_link+i['href']
    data=soup = BS(urllib2.urlopen(link).read())
    dlinks=data.find('div',{'id':'divDownload'})
    #print dlinks
    link=dlinks.find('a')
    #print link.contents[0]
    #print link['href']
    file_name=i.contents[0].strip()+'_'+link.contents[0]
    #print file_name
    print "downloading ... %s " % file_name 
    #print link['href']
    download(link['href'],file_name)