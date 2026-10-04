from http.client import RemoteDisconnected
import requests, time, os, cloudscraper, random, string, threading, easygui, ctypes, datetime
from requests.exceptions import Timeout
from colorama import init, Fore
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager
from ssl import PROTOCOL_TLSv1_2
from fake_useragent import UserAgent
from collections import OrderedDict
init(convert=True)

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

lock = threading.Lock()

url = "https://auth.riotgames.com/api/v1/authorization/"
count = 0

workingp = []

working_count = 0
timedout_count = 0
disconnected_count = 0
valid = 0
invalid = 0

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=PROTOCOL_TLSv1_2)


headers = OrderedDict({
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "application/json, text/plain, */*",
    'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
})

session = requests.Session()
session.headers = headers
session.mount('https://', TLSAdapter())
scraper = cloudscraper.create_scraper(sess=session)

def MakeRequest(url, proxy, rawProxy):
    global working_count, timedout_count, disconnected_count, valid, invalid
    ctypes.windll.kernel32.SetConsoleTitleW(f"FXCK V1.3.5 | Checked: {num}/{len(ProxyList)} | Working: {working_count} | Timed-out: {timedout_count} | Bad: {disconnected_count} | CPM: {cpm} ")
    try:
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
        r = scraper.post(url, json=data, proxies=proxy, headers=headers, timeout=8)


        lock.acquire()
        print(f'{red}[+]{reset} HIT: {rawProxy}')
        lock.release()

        save = open("results/workingprox.txt", "a+", encoding="utf-8")
        save.write(f"{rawProxy}" + "\n")

        working_count += 1
        valid += 1

    except Timeout:
        timedout_count += 1
        invalid += 1
        return
    except: 
        disconnected_count += 1
        invalid += 1
        return


cpm = 0
def cpmrunner():
    global cpm
    while True:
        oldchecked = valid + invalid
        time.sleep(1)
        newchecked = invalid + valid
        cpm = (newchecked - oldchecked) * 60


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

ProxyList = []

def getproxies():
    try:
        print(f'    [{red}>{reset}] Path to proxy file> ')
        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'valx - Select proxy', multiple= False)
        with open(path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                ProxyList.append(line)
    except Exception:
        print("Error has occurred")

num = 0
amount = 0

def start():
    global amount, num
    threads = 200
    os.system("cls")
    getproxies()
    time.sleep(0.5)
    os.system("cls")

    print(title)

    
    threading.Thread(target=cpmrunner).start()

    while True: 
        if threading.active_count() <= int(threads):
            amount = len(ProxyList) 

            if amount > num:
                try:
                    proxyIP = ProxyList[num]

                    UseProxy = f'http://{proxyIP}'

                    proxies = {
                    "https": UseProxy
                    }  
                    threading.Thread(target=MakeRequest, args=(url, proxies, proxyIP)).start()
                    # print(proxies)
                    num += 1
                except:
                    print(f'{red}[~]{reset} Checking finished...')