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
complete=False
latest=True

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
        try:
            call(["aria2c",'-c','true','-x','16','-j','10','-i','.tmp.txt'])
        except:
            print "aria2c is not installed"
        os.rmdir('.tmp.txt')
        return 1
    except:
        return 0

if complete==True:
    for i in rows:
        #print i['href']
        #print i['title']
        #print i.contents[0].strip()
        link= head_link+i['href']
        data=soup = BS(urllib2.urlopen(link).read())
        dlinks=data.find('div',{'id':'divDownload'})
        link=dlinks.find('a')
        file_name=i.contents[0].strip()+'_'+link.contents[0]
        print "downloading ... %s " % file_name 
        download(link['href'],file_name)

if latest==True:
    episode=rows[-1:][0]
    link= head_link+episode['href']
    data=soup = BS(urllib2.urlopen(link).read())
    dlinks=data.find('div',{'id':'divDownload'})
    link=dlinks.find('a')
    file_name=episode.contents[0].strip()+'_'+link.contents[0]
    print "downloading ... %s " % file_name 
    download(link['href'],file_name)