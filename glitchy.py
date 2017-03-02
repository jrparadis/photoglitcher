import random
#should use urllib2 for everything
import urllib
import urllib2
import sys
import traceback
import shutil
import string
import os
from bs4 import BeautifulSoup

def pickseed():
    seed = ''
    count = 1
    totallength = random.randrange(10,20)
    while count <= totallength:
        randomx = random.choice(string.ascii_letters.lower())
        seed += str(randomx)
        count += 1
    return str(seed)

def pickverylongseed():
    seed = ''
    count = 1
    totallength = random.randrange(5,50)
    while count <= totallength:
        randomx = random.choice(string.printable)
        seed += str(randomx)
        count += 1
    return str(seed)

keyword = 'help'
img_list = []

url = 'https://www.reddit.com/r/wallpaper+wallpapers/new'
def makealist(url, pages):
    request = urllib2.Request(url)
    opener = urllib2.build_opener()
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')
    feeddata = opener.open(request).read()
    soup = BeautifulSoup(feeddata)
    url1 = soup.findAll('a', {'rel':"nofollow next"})
    url2 = url1[0]['href']
    print url2
    for image in soup.findAll('a', {'data-event-action':"title"}):
        img_list.append(image['href'])

    print 'first page okay'
    for eachy in range(pages):
        request = urllib2.Request(url2)
        opener = urllib2.build_opener()
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')
        feeddata = opener.open(request).read()
        soup = BeautifulSoup(feeddata)
        url1 = soup.findAll('a', {'rel':"nofollow next"})
        url2 = url1[0]['href']
        print url2
        
        for image in soup.findAll('a', {'data-event-action':"title"}):
            img_list.append(image['href'])
        print 'page ' + str(eachy) + ' ok'
    print img_list
    return img_list




def gothing(fname, numofcopies):
    for each in range(numofcopies):
            shutil.copyfile(str(fname) + '.jpg', str(newName) + str(each) + '.jpg')
            newfoto = open(str(fname) + str(each) + '.jpg', 'r+')
            contents = newfoto.readlines()
            newcontents = []
            for each1 in range(random.randrange(10,500)):
                x = random.randrange(7,12)
                if x == 1:
                    newcontents.append(contents)
                elif x == 2:
                    newcontents.append(contents.reverse())
                elif x == 3:
                    newcontents.append(pickverylongseed())
                elif x == 4:
                    newcontents.append(contents.sort())
                elif x == 5:
                    newcontents.append(contents.sort(reverse=True))
                elif x == 6:
                    newcontents.append(contents.sort())
                    newcontents.append(contents.sort())
                    newcontents.append(contents.sort())
                    newcontents.append(contents.sort())
                    newcontents.append(contents.sort())
                    newcontents.append(contents.sort(reverse=True))
                    newcontents.append(contents.sort(reverse=True))
                    newcontents.append(contents.sort(reverse=True))
                    newcontents.append(contents.sort(reverse=True))
                    newcontents.append(contents.sort(reverse=True))
                elif x == 7:
                    bleh = ''
                    for each in contents:
                        bleh += each
                    newcontents.append(bleh)
                elif x == 8:
                    bleh = []
                    for each in contents:
                        bleh += each
                    newcontents.append(bleh.sort())                
                else:
                    pass
                
            contents.insert(random.randrange(1,len(contents) * 100000),newcontents)
            contents = ''.join(str(contents))
            newfoto.write(contents)
            newfoto.close()    
    

inc = 0

img_list = makealist(url, 10)
for num in img_list:
    print num

    try:
        newName = pickseed()
        f = open(str(newName) + '.jpg','wb')
        f.write(urllib.urlopen(img_list[inc]).read())
        f.close()
        shutil.copyfile(str(newName) + '.jpg', str(newName) + '-o.jpg')
        gothing(str(newName), 15)      
        print str(inc) + ' worked'   
        inc += 1
        os.remove(str(newName)+'.jpg')
    except:
        f.close()
        
        traceback.print_exc(file=sys.stdout)
        print str(inc) + ' failed   ----'
        inc += 1
        os.remove(str(newName)+'.jpg')
