from bs4 import BeautifulSoup as BS
import urllib2
import wget

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
    print "downloading ... %s" , file_name
    """
    call(["wget", link['href'],'-O',file_name])
    """
    
    """
    download_file = urllib2.urlopen(link['href'])
    output = open(file_name,'wb')
    output.write(download_file.read())
    output.close()
    
    """
    
    """
    url = link['href']
    
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)
    
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
    
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,
    
    f.close()
    """
    wget.download(link['href'],file_name)
    



