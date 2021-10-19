# webdriver > 이종간의 소프트웨어 드라이버(중간에서 연결하는) 역할
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import request as rq
from selenium.webdriver.common.keys import Keys
import time
import saveToExcel as xl
import util

browser = webdriver.Chrome()
url = 'https://www.gmarket.co.kr/'
browser.get(url)


# keyword
searchInput = browser.find_element(By.NAME, 'keyword')
searchInput.send_keys('나이키운동화')
# searchInput.send_keys(Keys.ENTER)

# class > image
searchBtn = browser.find_element(By.CLASS_NAME, 'image')
searchBtn.click()

# 위의 코드 실행 후 웨이팅 후 아래 데이터 로드됌
# browser.implicitly_wait(3)
time.sleep(3)  # import time


# 신발 이름들
shoesNameSelector = '#section__inner-content-body-container > div > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__item'
shoeNames = browser.find_elements(By.CSS_SELECTOR, shoesNameSelector)


for idx, shoeName in enumerate(shoeNames):
    print(idx, shoeName.text)

# 신발 가격들
shoesPriceSelector = '#section__inner-content-body-container > div > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-price > div.box__price-seller > strong'
shoePrices = browser.find_elements(By.CSS_SELECTOR, shoesPriceSelector)

for idx, shoePrice in enumerate(shoePrices):
    print(idx, shoePrice.text)

try:
    for i in range(len(shoeNames)):
        shoesName = list(shoeNames[i]).text
        shoesPrice = util.wonToInt(shoePrices[i].text)
        xl.write2Excel([shoesName, shoesPrice])

except Exception as e:
    print(e)
    print('fail!')

else:
    print('success!')

# move page
# 2페이지 이동
pageSelector = '#section__inner-content-body-container > div:nth-child(7) > div > a:nth-child(4)'
pageNavigator = browser.find_element(By.CSS_SELECTOR, pageSelector)
pageNavigator.click()

browser.implicitly_wait(2)
# time.sleep(2)

# 3페이지 이동
pageSelector = '#section__inner-content-body-container > div:nth-child(3) > div > a:nth-child(5)'
pageNavigator = browser.find_element(By.CSS_SELECTOR, pageSelector)
pageNavigator.click()

# 4페이지 이동

pageSelector = '#section__inner-content-body-container > div:nth-child(3) > div > a:nth-child(6)'
pageNavigator = browser.find_element(By.CSS_SELECTOR, pageSelector)
pageNavigator.click()

# 5페이지 이동

pageSelector = '#section__inner-content-body-container > div:nth-child(3) > div > a:nth-child(7)'
pageNavigator = browser.find_element(By.CSS_SELECTOR, pageSelector)
pageNavigator.click()


time.sleep(2)

browser.close()

# 5페이지까지 신발이름과 신발가격 엑셀에 저장하기





