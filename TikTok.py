try:
    import requests
except:
    print('[-] pip install requests')
    exit(0)
try:
    import colorama
    from colorama import Fore
    colorama.init(autoreset=True)
except:
    print('[-] pip install colorama')
    exit(0)
Bb = Fore.LIGHTYELLOW_EX
print(Bb + """
           __  __ ____   _____  ____  _   _ 
          |  \/  |___ \ / ____|/ __ \| \ | |
          | \  / | __) | |  __| |  | |  \| |
          | |\/| ||__ <| | |_ | |  | | . ` |
          | |  | |___) | |__| | |__| | |\  |
          |_|  |_|____/ \_____|\____/|_| \_|

""", Fore.LIGHTGREEN_EX + "\n                  ( @_m3gon )", Fore.LIGHTBLUE_EX + "\n",Fore.LIGHTYELLOW_EX + f"( Turbo TikTok {Fore.RESET}& {Fore.LIGHTYELLOW_EX}Checker Swap TikTok {Fore.RESET}& {Fore.LIGHTYELLOW_EX}Checker TikTok )\n\n"+Fore.RESET)
print(f'[+] {Fore.LIGHTYELLOW_EX}1 {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Checker TikTok'+Fore.RESET)
print(f'[+] {Fore.LIGHTYELLOW_EX}2 {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Checker Swap TikTok'+Fore.RESET)
print(f'[+] {Fore.LIGHTYELLOW_EX}3 {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Turbo TikTok'+Fore.RESET)
number1 = input('[?] Enter Number : ')
if number1 == '2':
    print('======================================')
    def check_sessionid_true_or_error():
        sessionid = input('[?] Enter Sessionid : ')
        url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
        headers = {
            'Host': 'api16-normal-c-alisg.tiktokv.com',
            'Content-Length': '25',
            'Connection': 'close',
            'Cookie': f'sessionid={sessionid}',
            'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
            "x-tt-passport-csrf-token": f"{sessionid}",
            'Content-Type': 'application/x-www-form-urlencoded',
            'passport-sdk-version': '5.12.1',
            'sdk-version': '2'
        }
        data = {
            'login_name': ''
        }
        req_check_sessionid = requests.post(url, headers=headers, data=data).text
        if ('"error_code":1') in req_check_sessionid:
            print(f'[-] {Fore.LIGHTRED_EX}Sessionid Is Error {Fore.RESET}: {Fore.LIGHTRED_EX}{sessionid}' + Fore.RESET)
            exit(0)
        elif ('"error_code":3') in req_check_sessionid:
            print(f'[+] {Fore.LIGHTGREEN_EX}Sessionid Is True' + Fore.RESET)
            def check_username():
                try:
                    namefile = input('[?] Enter Name File Userlist : ')
                    fileopen = open(namefile, "r").read().splitlines()
                except:
                    print(f'[-] {Fore.LIGHTRED_EX} Not Found File To Name : {namefile}')
                    exit(0)
                for file in fileopen:
                    url_check_username = f'https://www.tiktok.com/@{file}'
                    headers_check_username = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'no-cache',
                        'cookie': f'sessionid={sessionid}',
                        'pragma': 'no-cache',
                        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
                    }
                    req_check_username = requests.get(url_check_username, headers=headers_check_username).status_code
                    def swap():
                        if req_check_username == 404:
                            print('=======================================')
                            print(f'[+] {Fore.LIGHTGREEN_EX}Username Available {Fore.RESET}: {Fore.LIGHTGREEN_EX}{file}')
                            url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
                            headers = {
                                'Host': 'api16-normal-c-alisg.tiktokv.com',
                                'Content-Length': '25',
                                'Connection': 'close',
                                'Cookie': f'sessionid={sessionid}',
                                'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                                "x-tt-passport-csrf-token": f"{sessionid}",
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'passport-sdk-version': '5.12.1',
                                'sdk-version': '2'
                            }
                            data = {
                                'login_name': f'{file}'
                            }
                            req_swap_username = requests.post(url, data=data, headers=headers).text
                            if ('"error_code":1024') in req_swap_username:
                                print(f'[-] {Fore.LIGHTRED_EX}Error Swap')
                                exit(0)
                            elif ('"message":"success"') in req_swap_username:
                                print(
                                    f'[+] {Fore.LIGHTGREEN_EX}Done Swap The Username {Fore.RESET}: {Fore.LIGHTGREEN_EX}{file}')
                                print('=======================================')
                                input('[#] Enter To Exit ..')
                                exit(0)
                            elif (
                                    '"description":"login name can only be updated once within one month."') in req_swap_username:
                                print(f'[-] {Fore.LIGHTYELLOW_EX}You Can Change Username To Account After {Fore.LIGHTRED_EX}30 Day {Fore.RESET}..')
                                exit(0)
                        elif req_check_username == 200:
                            print(f'[-] {Fore.LIGHTRED_EX}Username Taken {Fore.RESET}: {Fore.LIGHTRED_EX}{file}')
                    swap()
            check_username()
    check_sessionid_true_or_error()
if number1 == '1':
    print('======================================')
    print(f'[+] {Fore.LIGHTYELLOW_EX}1 {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Checker TikTok {Fore.RESET}- {Fore.LIGHTGREEN_EX}Using {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Sessionid')
    print(f'[+] {Fore.LIGHTYELLOW_EX}2 {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Checker TikTok {Fore.RESET}- {Fore.LIGHTRED_EX}No {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Sessionid')
    numbersessionid = input('[?] Enter Number : ')
    if numbersessionid == '2':
        def check_sessionid_true_or_error():
            def check_username():
                try:
                    namefile = input('[?] Enter Name File Userlist : ')
                    fileopen = open(namefile, "r").read().splitlines()
                except:
                    print(f'[-] {Fore.LIGHTRED_EX} Not Found File To Name : {namefile}')
                    exit(0)
                for file in fileopen:
                    url_check_username = f'https://www.tiktok.com/@{file}'
                    headers_check_username = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'no-cache',
                        'cookie': 'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; ttwid=1%7Cbza8rvLOfNRPRwC43Zn3utwgngykYIkkhCtiFchZVMA%7C1616005073%7C1dd5efed4a61e4b1654f08f10a6ff7b85e3d57622a4d6011f6642b1bbf785fcb; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; store-country-code=sa; webapp_tiktok_lang=ar; tta_attr_id=0.1616499265.6942811476331593729; store-idc=alisg; s_v_web_id=verify_kmxb0dd5_U5SMVNWR_g0Au_4r8J_9Qe3_NJxpQO88j1Pw; bm_sz=B7BA96C29038DE027C1D8F44A20C1A03~YAAQj14zVtaDAax4AQAA51hurAue29s91EML4n7y7cpyXNp/mZ3eFOkU6xBp3cKVVKQNAV9Go3KVylbpRTbqwM/gjIjZHSsoKSbTlu+/SDXrUtMvoxCySp51X0y6+hV2CMGlP4UYfMBaaOHdvgYkEuBqb7jvvsNsQ3WxMLHSSBmzWy4V4jdLhT+lIHmJyECf; R6kq3TV7=ACWpbqx4AQAAtUda3I_0CRPGGXLYLm2dJqAVLy1VpSjtyyr0FvPj2jB9JGt-|1|0|0bab3523b256c3857d3044d70777cfc59db5a0a4; sid_guard=8a278ba86e41e4c666d87f182f5b4271%7C1617800905%7C5184000%7CSun%2C+06-Jun-2021+13%3A08%3A25+GMT; uid_tt=8948fc10fd88d839a5aa3fd2b8f32306a672d59add77b7a74e4cf9de5aae91cf; uid_tt_ss=8948fc10fd88d839a5aa3fd2b8f32306a672d59add77b7a74e4cf9de5aae91cf; sid_tt=8a278ba86e41e4c666d87f182f5b4271; sessionid=8a278ba86e41e4c666d87f182f5b4271; sessionid_ss=8a278ba86e41e4c666d87f182f5b4271; MONITOR_WEB_ID=6940688826462406145; odin_tt=16b47a9d890633da0212dcb61ecc74bad891f304e8c86da0a347c884185159246e0932d6fdbcf1dd76a150885370131e15897483a96a29f50a117268ee6a3d4fd158ff6034e5fe341156825b4b9ea0a7; tt_csrf_token=jFzXWBTVtdIJmz30aL5rDcCC; ak_bmsc=2BFA9FBE889292D9A8ACE1688F0441DC56335E84F35A0000A8D16D60A230CB0A~pl9YsfnUUFxSScJyCVjDbIy6xc9HNUT8NZt5/jV+pSBPI+tfkxCBs3saHsfIH7o0fPyhRp2X6L/ST9y2NkRyAvHJgIjuMJ0vDItFhZfBhvqgaqKlDecn++VZxnIf0ENPjyb/JGMhtBdYbROsBA3sF9cvsVb9KOK0OnqCXeLaAk1kh0fNvZB7UdLgfqeLh6Q1KeTSu9XiSxwY2bj1IoKR4QTQPvYPV8F1nQ9fG13MXvFy749gPtkrq/qg9lzNVgjTo3dfGs8KSqObvkL9eWOOWxuts2XhY60wz2AOjo8yI1azSt4O5Fqrc0u5FuwvwgUR5zcR3zsm4nIbsiq5geGYVbsg==; csrf_session_id=7d92d02da92e45d3b38480113ec3e2b5; bm_mi=7A2D33586E1C3E465AD8DA3FDF492AF3~apo0P2TMSSxBvHoDz19xRJmxeJLbWCYCrYxIn8X/aMemntN18RhH8r8OyGPf5QT9CqwtBm9e77kkzLLoXvgAK7AetmNqa2cDc/vffFeXx3/ClA+bFLnHNmUCZ0xfOCsV8ABDD6p0ejkZcZtgnDTNsBt4zsz4yBz2aD/kgO6USsaY6NOc6OidNEUhP66EqbtLn9M1gF4Udest87E0EL8Q37ewfWGOgw0jJnSdHCWvNkY=; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQhF4zVtA/46x4AQAAqGr7rAXcf3Xg4fDEZyGhvFncu1lzRdE2ZvhkswlA6k+8ROBAHVH3COWwrL747JfsaEAyV+cwyxzwmAE8+zYsUVgBmBmAwgOEpMhWprb+d/ADq7Ek6G5g6wudlWw7vF0aOep/WXLIff6m2ynybkAnd0+1Cx1M281mnfHgI7RbYzowU0umCo3WHyu9B5EYXS/WDGR577FZcfl+bv+V9zGkFuwno9tnhbYSA0b9uTJ3x/GHf6iy1SGsGSYZr5YPKHjeMUxxtxdY6of2i4N4ApDDWfj8rt0n60V3xUfxfWUvo4Z9yDQpB3/yGJLhSQQ+mZSZKlE8S5EX5J9dA4V2wzhmecIxYnHq5ZluCB4OZXe8r6PkRrHTpZT9pK5MGaUOGfgHl9JDdYufl+sv9A==~-1~-1~-1; bm_sv=31C9EC826FD5B2BB015298CD740D2C26~DevuhoUbWEDMuQUWBWa2O+picPk0NNHClYDH6hB3k0hWbjGieDWNPEDBi+MXpJDxHlmdgdpNrSLctT3SaIQ4wnzjekaKWAgAmh1BN6faL3XurDb1OY1HEyo11KzW4df/qiphj7PIDzImKUwPqIEF5w3R0fGamWUuHZQik6pGFTg=',
                        'pragma': 'no-cache',
                        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
                    }
                    req_check_username = requests.get(url_check_username, headers=headers_check_username).status_code
                    if req_check_username == 404:
                        print(f'[+] {Fore.LIGHTGREEN_EX}Username Available {Fore.RESET}: {Fore.LIGHTGREEN_EX}{file}')
                        with open('Available_tiktok.txt', 'a') as xx:
                            xx.write(file + '\n')
                    elif req_check_username == 200:
                        print(f'[-] {Fore.LIGHTRED_EX}Username Taken {Fore.RESET}: {Fore.LIGHTRED_EX}{file}')
            check_username()
        check_sessionid_true_or_error()
    if numbersessionid == '1':
        def checker_tiktok():
            available = 0
            Taken = 0
            sess = input('[+] Enter Sessionid : ')
            namefile = input('[+] Enter NameFile Userlist : ')
            openfile = open(namefile).read().splitlines()
            for checkerusers in openfile:
                url_checker_tiktok = f'https://www.tiktok.com/api/uniqueid/check/?aid=1233&unique_id={checkerusers}&app_language=ar&fromWeb=1&cookie_enabled=true&screen_width=810&screen_height=692&browser_language=en-US&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F89.0.4389.90%20Safari%2F537.36&browser_online=true&timezone_name=America%2FLos_Angeles&device_platform=web_pc&region=SA&_signature=_02B4Z6wo00101r8OLdQAAIDD2vtO9XDzECq.DilAAM-dfa'
                headers_checker_tiktok = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'referer': 'https://www.tiktok.com/signup/create-username?lang=ar',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                    'x-mssdk-info': 'LRRVAlZCQ08zzICjyuDuPxrY6FeG2qKm4zqRVPS5Jn5bhK8ZCTcHP0rJCMMzGgMWU.YtbXXFBr.ZeI4cqaEbcGN3SMPRY3j0c1rzbhJ8mm4Tj8uhAbza0ulz.7zOJwCOZ3x6A.HUGgx2UtuXc3KnHqJ9jgsVcCkIaO8lXhTg50DVybeyCsUUUdvyBuDZwjcKpP7rc1nv1-.Qi-oesXItZnV1CnSH7kLTnn75NG3kZQXGz5rOW9npFIj7w1vXmyYrkA.Son6M7p7DNB9fArgR2eFHHvx29XzWrdTU1QYq7rCSNCGxQAFGaCNfZ5FUB46NEzv1ghDqXd99HhJeWL-x9ku9QKEWeJtM1zBcVvW75eASPcQfaxytt0.tylv6EyQiZcOBOEYS3p04MBVzKA-OSkVSwfgxqU1Bh3Or2X34gPpOzWL92ih.KeptGICK6vijHukr5jfCIBSXhxvG7Dmrf.MbeT1XpZKcv1nZJvNZd.mU9vFBJe77DPfbGpbQbSa7lJ1jE3J1vQZQjr9B1oJBJKIi3F-ZVUSAUQBz9gWi2jWZURsQAF9Typ1gPLKEWgrYqXfNv9zs4vsGV35H7oJjqG9UN0FqdEgKg9RTUleKkwGGrXVQUm4YVpTvbTUiOVpKEXz220XDgHd32wnFx1iOuEXl68ttHly0KLchuQsxunG3l9EAOSjNdCEupwDy7s4f1Gng8MbY2OSbmxdTN5TIsVX6PiE9LIDyJ1AGcYyuevGWGreLztxW7h-uFGzzEKRKfYpfHnI8T5yoEiHRqY.SkU7N7E480mCzMC8Uf6iiMayvuQJpNxlxoZYq8FxPNrUc1hK3Psd43zG8-9XKQGM7v3u95M1lzGFPtwl7prCkiPecAyx8xiaMuMDHmXbLtxzsUGtM.tzJ8brBfqizkyFyF2-NxR3kS.Q6D8yj6CenMsukxifZXXTU1iLo.n3DO-CkgPUxdNQXHEIrfmpKJwFNKtqu0IR.cD-HkRGFj92iuWdvsdXO3MlFMXKeRFM6s3pqsyzKqOrsPlcpj.eDD1WXk6qyUkFMXOukWHdXkjbYUiqMQBSra2Y9W2t0qbXUCPD75ut1TW.UIuqnZVvrr.hQODbGpQlWBwj2LducqoduCgGYmvjB1qg0PfQiIlAn.mhfRQKDej-aImeKb1VSOjHIMCgimIf9DspemoPOt0Dd89vTMc4SPOYg7j7L-Uql5lP-ka5xsYKxHKmMxhPmqi7rL0LNjBzDBhxGJ7MrdSns7-4jc-io7iOFViWIzYtGSl9jLjq4QSx8K24AXS-ECHDPuwzcuJ5NCPejUY41lkk5z8i4ytxtmy9.56AVpNEhK23TaM72beyvbHPrk3bo3OiEe-rM44nPFK.IKLT0BjEeoZP5YHGGP963lIQ1BfKy.XCB7.KXXtBIY5wAZx-BTMjdWNCnVB7WNyupz89NMjpRInXsO4gy3WYbFrQ05mCfPiPq5.Kjl6sYLWjGi3n2Msklz0Nd08EmaQjpapQMGw7jXNS7gQa9h0u4wyKfCXNJNpWKue-jcRDdL.miiaR49LadGrW62bKDiBQ9ZGPO.dlWwpb7nS3HoeFUs4Bk1XzrwgXg7JU0FJWaRAL7YGWl6WnGErvvSQ50pQfBfAY9ukGcZoRVDq5tcfrkfKBhvagi.6-02u0u1-jzRU3phLXbeM1smEjJjLmO6VBXZMCoEBZF4Jy9KnubDe11JRFEusthrVMLnQ-4kxzr1Uyp1QiAUOPMCRWxDsObe5BPf71MLFL3.tWjwJ5n3LwUD.IpWD4uf4eDmqdAFqtxXCmXnRi7PZD9Di7lJZo8nSNczcGvl8YiItU-KwQTJzm4c9VYQkRtE0cv-lBSoHi9hdJxCdj4NUWh1mVZJF4CLd619w-giEygAt-sVBUhEiH6HHzCnJtUPnt5x-l5mQGxd-U1ObQNzhmzer1ObK7mHFTsYqFLnQIPwAnzjSG5V7dAaWwQb.nv8rYDdrcU.h33U7O6T...1SFIkAF5aImI5EVcE0eHxEa4l4AfJoN1BMp-6UB5pLPJVWPpwd18.In0J3kC5sn2RL6zxtozjT-4c2YrPAY5gsakwafGPGA885U6IiM4bVpiieC7jAjuvU1FS-QxYsUwG8ZOzyWoTYKB0h.VtjKxN.1vig5CEEh-oFejdTAtHX5Zi6YEEnnGbk-NfwxaXyXQCCaGkPqo15s64MpWo7N.jttqySeRO-rh35eQ9iWFZmnoD5kjRkXvvwxsFprZrHG7LTDFbnlZomAIosfOTYhfjyyrYBCnLguGXNuS2kVrLGYtKPMI4btYlYnuIowf4S9Gl.B.K2rafgaIRanDCI0d3Bd0TNSr1vL0648E9WLexejILZJp6w6RSKmvO.9zXFlMyn.2c9dLIoh57XSzE6qqLUee0Ht02GMAQqkxD3Kpwrncex6UjgHZdHS9vmGZhHwmaLb0zIuo2gShzp4wiZLzg4oNkKUS9k51iNGyAO45GH7riIs4r64e30T5sVmEx0pRrko6BJzE4o0TSySE8Leg6qaJqJ38RE9VrjEhJYOOxtIPvAohbIbfHQq3AyzOjpgemuLfkVshSBIhlkHKzcr3OX8SmxCX8OjLMUxhHuPg8D44g6oprrVRWQJFvsLPxq4yGSWTbqeauoGG8zNsARb-wc4CLpzjrBzMCorGWJZRIILtfbH2xYUYNHx21W4HKPWGw8eAYp2Kvz0xMpY0Zd3X8Kwpn69H1ltqoiVxXlVNUFH83B99iXo2lMfjLvbnyZ2xsQflpP08m9gDvaNmIJ81aY7on7nca0-8CWbk4EMWrkxxX70mNnn3Xk4eMysj7qjRe3N6gYEuThu3RvCCYHaHRG9-kgO.B6hVUHXkN74h3WXgW7OpSY69T7Zt4XNocQ2lNsM0NJx0EsdPsTfDQ9JWFe0SPX0Sq2AUP7ZPbY2fW3XgXcZ3D97M8NQeki0eBd3lf4p5LJlUJZXrrzaT2anLQkINShVFuEPLWfXJFTM3YVU7o2p8SWELSUw6Z08UEPf9bgPv63p1gJiuPGDuAwNmLsy09nKKbF5QTif1cJLCCo1C8jZwTsgHVjM7uGWQyW6EoZK50UOGJhhsa1k='
                }
                cookies = {'sessionid': sess}
                req = requests.get(url_checker_tiktok, headers=headers_checker_tiktok, cookies=cookies).text
                if '"status_msg":""' in req:
                    available += 1
                    print(f'[{available}] {Fore.LIGHTGREEN_EX}Available {Fore.RESET}: {Fore.LIGHTGREEN_EX}{checkerusers}')
                    with open('Available_tiktok.txt', 'a') as x:
                        x.write(checkerusers + '\n')
                else:
                    Taken += 1
                    print(f'[{Taken}] {Fore.LIGHTRED_EX}Taken {Fore.RESET}: {Fore.LIGHTRED_EX}{checkerusers}')
        checker_tiktok()
if number1 == '3':
    print('======================================')
    print(f'[+] {Fore.LIGHTYELLOW_EX}1 {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Turbo TikTok {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Userlist'+Fore.RESET)
    print(f'[+] {Fore.LIGHTYELLOW_EX}2 {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Turbo TikTok {Fore.RESET}- {Fore.LIGHTYELLOW_EX}Suggestions'+Fore.RESET)
    numberwhat = input('[?] Enter Number : ')
    if numberwhat == '2':
        def check_sessionid_true_or_error():
            sessionid = input('[?] Enter Sessionid : ')
            url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
            headers = {
                'Host': 'api16-normal-c-alisg.tiktokv.com',
                'Content-Length': '25',
                'Connection': 'close',
                'Cookie': f'sessionid={sessionid}',
                'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                "x-tt-passport-csrf-token": f"{sessionid}",
                'Content-Type': 'application/x-www-form-urlencoded',
                'passport-sdk-version': '5.12.1',
                'sdk-version': '2'
            }
            data = {
                'login_name': ''
            }
            req_check_sessionid = requests.post(url, headers=headers, data=data).text
            if ('"error_code":1') in req_check_sessionid:
                print(f'[-] {Fore.LIGHTRED_EX}Sessionid Is Error {Fore.RESET}: {Fore.LIGHTRED_EX}{sessionid}'+Fore.RESET)
                exit(0)
            elif ('"error_code":3') in req_check_sessionid:
                print(f'[+] {Fore.LIGHTGREEN_EX}Sessionid Is True'+Fore.RESET)
            def check_username():
                username = input('[?] Enter Username Target : ')
                url_check_username = f'https://www.tiktok.com/@{username}'
                headers_check_username = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'cookie': f'sessionid={sessionid}',
                'pragma': 'no-cache',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
                }
                while True:
                    req_check_username = requests.get(url_check_username, headers=headers_check_username).status_code
                    def swap():
                        if req_check_username == 404:
                            url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
                            headers = {
                                'Host': 'api16-normal-c-alisg.tiktokv.com',
                                'Content-Length': '25',
                                'Connection': 'close',
                                'Cookie': f'sessionid={sessionid}',
                                'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                                "x-tt-passport-csrf-token": f"{sessionid}",
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'passport-sdk-version': '5.12.1',
                                'sdk-version': '2'
                            }
                            data = {
                                'login_name': f'{username}'
                            }
                            req_swap_username = requests.post(url, data=data, headers=headers).text
                            if ('"error_code":1024') in req_swap_username:
                                print(f'[-] {Fore.LIGHTRED_EX}Error Swap')
                                exit(0)
                            elif ('"message":"success"') in req_swap_username:
                                print(f'[+] {Fore.LIGHTGREEN_EX}Done Swap')
                                input('[#]] Enter To Exit ..')
                                exit(0)
                            elif ('"description":"login name can only be updated once within one month."') in req_swap_username:
                                print(f'[-] {Fore.LIGHTYELLOW_EX}You Can Change Username To Account After {Fore.LIGHTRED_EX}30 Day {Fore.RESET}..')
                                exit(0)
                        elif req_check_username == 200:
                            print(f'[-] {Fore.LIGHTRED_EX}Username Taken {Fore.RESET}: {Fore.LIGHTRED_EX}{username}')
                    swap()
            check_username()
        check_sessionid_true_or_error()
    if numberwhat == '1':
        print('======================================')
        def check_sessionid_true_or_error():
            sessionid = input('[?] Enter Sessionid : ')
            url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
            headers = {
                'Host': 'api16-normal-c-alisg.tiktokv.com',
                'Content-Length': '25',
                'Connection': 'close',
                'Cookie': f'sessionid={sessionid}',
                'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                "x-tt-passport-csrf-token": f"{sessionid}",
                'Content-Type': 'application/x-www-form-urlencoded',
                'passport-sdk-version': '5.12.1',
                'sdk-version': '2'
            }
            data = {
                'login_name': ''
            }
            req_check_sessionid = requests.post(url, headers=headers, data=data).text
            if ('"error_code":1') in req_check_sessionid:
                print(f'[-] {Fore.LIGHTRED_EX}Sessionid Is Error {Fore.RESET}: {Fore.LIGHTRED_EX}{sessionid}'+Fore.RESET)
                exit(0)
            elif ('"error_code":3') in req_check_sessionid:
                print(f'[+] {Fore.LIGHTGREEN_EX}Sessionid Is True'+Fore.RESET)
                def check_username():
                    try:
                        namefile = input('[?] Enter Name File Userlist : ')
                        fileopen = open(namefile, "r").read().splitlines()
                    except:
                        print(f'[-] {Fore.LIGHTRED_EX} Not Found File To Name : {namefile}')
                        exit(0)
                    while True:
                        for file in fileopen:
                            url_check_username = f'https://www.tiktok.com/@{file}'
                            headers_check_username = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'en-US,en;q=0.9',
                            'cache-control': 'no-cache',
                            'cookie': f'sessionid={sessionid}',
                            'pragma': 'no-cache',
                            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
                            }
                            req_check_username = requests.get(url_check_username, headers=headers_check_username).status_code
                            def swap():
                                if req_check_username == 404:
                                    print('=======================================')
                                    print(
                                        f'[+] {Fore.LIGHTGREEN_EX}Username Available {Fore.RESET}: {Fore.LIGHTGREEN_EX}{file}')
                                    url = 'https://api16-normal-c-alisg.tiktokv.com/passport/login_name/update/?residence=SA&device_id=6870709334024848901&os_version=13.6.1&app_id=1233&iid=6924902298624624385&app_name=musical_ly'
                                    headers = {
                                        'Host': 'api16-normal-c-alisg.tiktokv.com',
                                        'Content-Length': '25',
                                        'Connection': 'close',
                                        'Cookie': f'sessionid={sessionid}',
                                        'x-Tt-Token': '2c593820065f9a47b9bf51281eda9604-1.0.0-1.0.0',
                                        "x-tt-passport-csrf-token": f"{sessionid}",
                                        'Content-Type': 'application/x-www-form-urlencoded',
                                        'passport-sdk-version': '5.12.1',
                                        'sdk-version': '2'
                                    }
                                    data = {
                                        'login_name': f'{file}'
                                    }
                                    req_swap_username = requests.post(url, data=data, headers=headers).text
                                    if ('"error_code":1024') in req_swap_username:
                                        print(f'[-] {Fore.LIGHTRED_EX}Error Swap')
                                        exit(0)
                                    elif ('"message":"success"') in req_swap_username:
                                        print(
                                            f'[+] {Fore.LIGHTGREEN_EX}Done Swap The Username {Fore.RESET}: {Fore.LIGHTGREEN_EX}{file}')
                                        print('=======================================')
                                        input('[#] Enter To Exit ..')
                                        exit(0)
                                    elif (
                                    '"description":"login name can only be updated once within one month."') in req_swap_username:
                                        print(
                                            f'[-] {Fore.LIGHTYELLOW_EX}You Can Change Username To Account After {Fore.LIGHTRED_EX}30 Day {Fore.RESET}..')
                                        exit(0)
                                elif req_check_username == 200:
                                    print(f'[-] {Fore.LIGHTRED_EX}Username Taken {Fore.RESET}: {Fore.LIGHTRED_EX}{file}')
                            swap()
                check_username()
        check_sessionid_true_or_error()
