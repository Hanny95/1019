from urllib import request as rq

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl'
browser = webdriver.Chrome()
browser.get(url)

# 검색창 class = gLFyf
searchInput = browser.find_element(By.CLASS_NAME, 'gLFyf')
searchInput.send_keys('BTS')
searchInput.send_keys(Keys.ENTER)

time.sleep(2)

# javascript 에 명령 : 스크롤 끝까지 내리기 !!
endHeight = browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)

    currentHeight = browser.execute_script('return document.body.scrollHeight')

    if currentHeight == endHeight:
        try:
            moreBtn = browser.find_element(By.CLASS_NAME, 'mye4qd') # 결과 더보기 : # mye4qd
            moreBtn.click()

        except Exception as e:
            print(e)
            break

    endHeight = currentHeight

# 이미지 class = rg_i Q4LuWd
thums = browser.find_elements(By.CLASS_NAME, 'Q4LuWd')
print(f'thunms length : {len(thums)}')

# 스크롤 위치 초기화
browser.execute_script('window.scrollTo(0, 0)')

for idx, thum in enumerate(thums):

    try:
        thum.click()

        time.sleep(2)

        oriImgURL = browser.find_element(By.CLASS_NAME, 'n3VNCb').get_attribute('src')
        rq.urlretrieve(oriImgURL, 'C:/chh_scraping/download/img/testImg' + str(idx) + '.jpg')

    except Exception as e:
        print(e)


browser.close()

# 오리지널 이미지 class = n3VNCb










