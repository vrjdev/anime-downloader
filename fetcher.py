try:
    import urllib2
except:
    print "urllib2 is not installed"
try:
    from bs4 import BeautifulSoup as BS
except:
    print "BeautifulSoup4 is not installed , try sudo pip install BeautifulSoup4"

import os
import sys
from subprocess import call




com_link="http://www.kissanime.com/Anime/One-Piece"
com_link="http://kissanime.com/Anime/Hunter-x-Hunter-2011"

if com_link.endswith('/'):
    com_link=com_link[:-1]
folder_name=com_link.split('/')[-1:][0]


complete=False

latest=False

last_x=True
last_num=10


from urlparse import urlparse
parsed_uri = urlparse( com_link )
domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

head_link=domain



tot_link=com_link

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
            f.write(folder_name+'/'+name)
            f.write('\n')
        f.close()
        try:
            call(["aria2c",'-c','true','-x','16','-j','10','-i','.tmp.txt'])
        except:
            print "aria2c is not installed , try sudo apt-get install aria2"
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
elif latest==True:
    episode=rows[-1:][0]
    link= head_link+episode['href']
    data=soup = BS(urllib2.urlopen(link).read())
    dlinks=data.find('div',{'id':'divDownload'})
    link=dlinks.find('a')
    file_name=episode.contents[0].strip()+'_'+link.contents[0]
    print "downloading ... %s " % file_name 
    download(link['href'],file_name)
elif last_x==True:
    episodes=rows[-last_num:]
    for i in episodes:
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