#################### 先載 selenium ####################
#這個(包括驚嘆號)     !pip install selenium

#################### PTT ####################

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--diable-dve-shm-uage')

driver = webdriver.Chrome(options = options)
url = "https://www.ptt.cc/bbs/Gossiping/index.html"

driver.get(url)

over18 = driver.find_element(By.XPATH,'/html/body/div[2]/form/div[1]/button')
over18.click()

def result_print():

  for content in driver.find_elements(By.XPATH, '//div[@class="title"]'):
      try:
        # 直接取得 <a> 元素的 href 屬性
          hrefValue = content.find_element(By.XPATH, './/a').get_attribute("href")
          postTime = content.find_element(By.XPATH, '//div[@class="date"]')
          print(postTime.text + "  " + content.text + "\t\t\t\t\t" + hrefValue)
      except:
        # 如果找不到 <a> 元素，則只印出文字內容
          postTime = content.find_element(By.XPATH, '//div[@class="date"]')
          print(postTime.text + "  " + content.text+"\t\t\t\t\t")

print("\npage 1")

result_print() #先跑第一頁
for i in range(2,6): #使用迴圈從第2頁跑到第5頁  (i=2 i<6 i++)
  next_page = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/a[2]')
  next_page.click()
  print("\npage "+str(i)+"")
  result_print()
driver.quit()