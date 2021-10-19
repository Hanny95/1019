# webdriver > 이종간의 소프트웨어 드라이버(중간에서 연결하는) 역할
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#01 - chrome 검색 자동화
browser = webdriver.Chrome()   #()안에 chromedriver 경로지정
url = 'https://www.google.co.kr/'
browser.get(url)  # step01 : 사이트 접속

# gLFyf           # step02 : element 찾기
inputs = browser.find_elements(By.CLASS_NAME, 'gLFyf')  # By import 해야함
print(f'inputs : {inputs}')      # 결과 : 1개

# step03 : input search word
inputs[0].send_keys('python')

# step04 : click on enter  > ** Keys import
inputs[0].send_keys(Keys.ENTER)











