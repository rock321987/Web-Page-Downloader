from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import codecs
import sys
import pdfkit

if sys.stdout.encoding != 'cp850':
  sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'xmlcharrefreplace')
if sys.stderr.encoding != 'cp850':
  sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'xmlcharrefreplace')

def construct_url(link):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(link, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    return respData
    
try:
    basic = "http://wcipeg.com/wiki/index.php?title="
    extract_url_from_this_page = "http://wcipeg.com/wiki/Special:AllPages"
    extract_url_from_this_page = BeautifulSoup(construct_url(extract_url_from_this_page))
    cnt = 0

    for link in extract_url_from_this_page.find_all('a'):
        x = link.get('title')
        if (x == None or cnt >= 232):
            continue
        else:
            x = x.strip()
            x = x.replace(' ', '_')
            cnt += 1
            basic = (basic + x + "&printable=yes")
            
            if (x.find('/') > 0):
              x = x.replace('/', '_')

            pdfkit.from_url(basic, x + ".pdf")
            basic = "http://wcipeg.com/wiki/index.php?title="
except Exception as e:
    print (e)
