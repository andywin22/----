########################## Google新聞  ##########################
import requests
url = 'https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'

resp = requests.get(url)
ouput = resp.content.decode()
print(ouput)

########################## Gmail登入 + 找關鍵字 ##########################
import requests

url = 'https://mail.google.com/mail/u/0/#inbox'

headers={ "User-Agent": ''
        ,"Cookie":''
    }
req = requests.get(url, headers = headers)
resp = req.content.decode()
print('Helal Uddin' in resp)

##########################學校系統##########################
import requests
from bs4 import BeautifulSoup

url = "https://student.cyut.edu.tw/ST0000"

headers ={"User-Agent": ''
      ,"Cookie": ''
}
resp = requests.get(url, headers=headers)
content = resp.content.decode()
soup = BeautifulSoup(content,'html.parser')
output = soup.find_all('div', class_='col-md-2 col-xs-6')
print(output)


########################## 學校系統 + 找關鍵字 ##########################
import requests
from bs4 import BeautifulSoup

url = 'https://student.cyut.edu.tw/ST0000/'

headers={ "User-Agent": ''
      ,"Cookie": ''
    }

resp = requests.get(url, headers=headers)
content = resp.content.decode()
soup = BeautifulSoup(content,'html.parser')
output = soup.find_all('div', class_='col-md-2 col-xs-6')

word = '學期課表'

found_keyword = any(word in str(item) for item in output)

print(found_keyword)