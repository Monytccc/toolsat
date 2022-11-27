
from time import sleep
import requests,os
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
thanh_xau= do+"["+luc+"●"+do+"] "+trang+"=> ";
thanh_dep=  do+"["+luc+"●"+do+"] "+trang+"=> ";
def logo():
    logo = """\033[1;92m     Thương Hiệu: \033[1;33mLMK-TOOL   🔥  \033[1;92m Coppyright:\033[1;33m Lê Mạnh Kiên
\033[1;33m •╔═════════════════════════☩══♛══☩═════════════════════════╗•
\033[1;33m  Zalo:\033[1;32m 0843081105              \033[1;31m██╗░░██╗██╗███████╗███╗░░██╗
\033[1;33m  Youtube:\033[1;32m Kiên 205 Official    \033[1;32m██║░██╔╝██║██╔════╝████╗░██║
\033[1;33m  Bản Tool:\033[1;32m Tool Gộp            \033[1;33m█████═╝░██║█████╗░░██╔██╗██║
\033[1;33m  Update:\033[1;32m V7.0                  \033[1;34m██╔═██╗░██║██╔══╝░░██║╚████║
\033[1;33m  Thương Hiệu:\033[1;32m LMK-TOOL         \033[1;35m██║░╚██╗██║███████╗██║░╚███║                                    \033[1;39m╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚══╝  
 \033[1;33m•╚═════════════════════════☩══✦══☩═════════════════════════╝•
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    print(logo)
    print("\033[1;33m"+"------------------------------------------------------------")

    get_qdc = {
        'Level':'Tool Vipig Tym',
        'update':'V2.0',
        'end':'Thanks',
    }
    print("\033[1;32m╔═════════════════════╗"); 
    print("\033[1;32m║ \033[1;33mThông Tin Tool\033[1;32m      ║"); 
    print("\033[1;32m╚═════════════════════╝"); 
    print(thanh_xau+luc+"Bản Tool: "+vang+get_qdc['Level']); #người mua
    print(thanh_xau+luc+"Update: "+vang+get_qdc['update']); #ngày mua
    print(thanh_xau+luc+"LMK: "+vang+get_qdc['end']); #ngày hết hạn

    print("\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"); 
logo()
lmkvip="\033[1;31m[\033[1;33mLMK-TOOL\033[1;31m]\033[1;35m❯\033[1;36m❯\033[1;37m❯\033[1;32m "
lmkdz="\033[1;31m[\033[1;33mLMK-TOOL\033[1;31m]\033[1;35m❯\033[1;36m❯\033[1;37m❯ \033[1;31m "
useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36";
while True:
    luu = str(input("\033[1;32m Nhập\033[1;33m Enter\033[1;32m Để Vào Tool\033[1;32m Nhập\033[1;31m no\033[1;32m Để Đăng Nhập Lại: "))
    if luu=='no':
        tokenvipig = str(input(lmkvip+"Token VIPIG: \033[1;33m "))
        
        with open('TOKENVIPIG.txt',mode='w') as file:
            file.write(tokenvipig)
            file.close()
        break
    if luu=='':
        try:
            dataacc = open('TOKENVIPIG.txt',mode='r').read()
            tokenvipig = dataacc
            break
        except:
            print("\033[1;96mBạn Chưa Lưu Tài Khoản Hoặc Chạy Lần Đầu\n")
            continue
get = requests.post('https://vipig.net/logintoken.php',headers={'Content-type': 'application/x-www-form-urlencoded'},data={'access_token': tokenvipig})
cookievipig = str(get.headers['set-cookie'])
if get.json()['status']=='success':
    print("\033[1;96mĐăng Nhập Thành Công vipig\n")
else:
    print("\033[1;96mKiểm Tra Lại Cookie vipig\n")
    exit()
soluong = int(input(lmkvip+"Nhập Số Lượng Acc Instagram Muốn Chạy: \033[1;33m "))
datacookie = []
for a in range(1,soluong+1):
    cookieins = str(input(f"\033[1;32mNhập Cookie Thứ {a}:\033[1;33m "))
    headers = {
    'authority': 'www.instagram.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': cookieins,
    'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
    'referer': 'https://www.instagram.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'viewport-width': '1366',
    }

    getdatains = requests.get('https://www.instagram.com/', headers=headers)
    try:
        idins =  getdatains.text.split('\\"viewerId\\":\\"')[1].split('\\"')[0]
        userins =  getdatains.text.split('\\"userLevel\\":\\"')[1].split('\\"')[0]
        datacookie.append(f'{idins}|{userins}|{cookieins}')
    except:
        print("\033[1;96mKiểm Tra Lại Cookie instagram\n")
delayy = int(input(f"\033[1;32mNhập Delay:\033[1;33m "))
os.system('clear')
logo()
def tym(idtym, csrftoken, cookieins):
    headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': cookieins,
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'viewport-width': '811',
    'x-asbd-id': '198387',
    'x-csrftoken': csrftoken,
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR2USZZ6eJeXKuiG76MzxHVV1Qr2svdlQPqs7SJc3Fkgc-7c',
    'x-instagram-ajax': '1005751561',
    'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.post(f'https://www.instagram.com/web/likes/{idtym}/like/', headers=headers)
    if response.json()['status']=='ok':
        return "Thành Công"
    else:
        return "Thất Bại"
def getxu(cookievipig):
    headers = {
    'authority': 'vipig.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'vi,en;q=0.9',
    'cache-control': 'max-age=0',
    
    'cookie': cookievipig,
    'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    response = requests.get('https://vipig.net/home.php', headers=headers)
    xu = response.text.split('id="soduchinh">')[1].split('</strong>')[0]
    return xu
stt = 1
for i in range(len(datacookie)):
    data = datacookie[i].split('|')
    idins =  data[0]
    userins =  data[1]
    cookieins = data[2]
    xu = getxu(cookievipig=cookievipig)
    print(f'\033[1;32mInstagram: {userins}| Xu: {xu}')
    #cấu hình
    headers = {
    'authority': 'vipig.net',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookievipig,
    'origin': 'https://vipig.net',
    'referer': 'https://vipig.net/cauhinh/index.php',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'iddat[]': idins,
    }

    cauhinh = requests.post('https://vipig.net/cauhinh/datnick.php', headers=headers, data=data)
    headers = {
    'authority': 'vipig.net',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'vi,en;q=0.9',
    'cookie': cookievipig,
    'referer': 'https://vipig.net/kiemtien/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    getlink = requests.get('https://vipig.net/kiemtien/getpost.php', headers=headers)
    for data in getlink.json():
        idpost = data['idpost']
        link = data['link']
        headerget = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookieins,
        'pragma': 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
        'referer': 'https://vipig.net/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'viewport-width': '1366',
        }
        response = requests.get(f'{link}/', headers=headerget)
        idtym = response.text.split('"media_id":"')[1].split('"')[0]
        csrftoken = response.text.split('"csrf_token":"')[1].split('"')[0]
        don = tym(idtym, csrftoken, cookieins)
        if don == "Thành Công":
            xu = getxu(cookievipig=cookievipig)
            headers = {
            'authority': 'vipig.net',
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': cookievipig,
            'origin': 'https://vipig.net',
            'referer': 'https://vipig.net/kiemtien/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'id': idpost,
            }

            nhanxu = requests.post('https://vipig.net/kiemtien/nhantien.php', headers=headers, data=data)
            if 'Thành công' in nhanxu.text:
                print(lmkvip+f"[{stt}] Tym Cho Bài Viết \033[1;31m✇ {idpost} \033[1;96m Thành Công| +300 | Tổng: {xu}")
            else:
                print(lmkvip+f"[{stt}] Tym Cho Bài Viết \033[1;31m✇ {idpost} \033[1;96m Thành Công| Tổng: {xu}")
            stt= stt+1
        else:
            print(f"\033[1;31m[{stt}] Tim Thất Bại")
        for i in range(delayy, 0, -1):
            print("\033[1;33mLMK-TOOL Vui Lòng Chờ "+str(i)+" Giây",end='\r');
            sleep(0.2);
            print("\033[1;32mLMK-TOOL Vui Lòng Chờ "+str(i)+" Giây",end='\r');
            sleep(0.2);
            print("\033[1;35mLMK-TOOL Vui Lòng Chờ "+str(i)+" Giây",end='\r');
            sleep(0.2);
            print("\033[1;36mLMK-TOOL Vui Lòng Chờ "+str(i)+" Giây",end='\r')
            sleep(0.2);
            print("\033[1;96mLMK-TOOL Vui Lòng Chờ "+str(i)+" Giây",end='\r');
            sleep(0.2);
