# webdriver > 이종간의 소프트웨어 드라이버(중간에서 연결하는) 역할
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
url = 'https://www.naver.com/'
driver.get(url)

inputs = driver.find_element(By.ID, 'query')

searchWord = input('검색어 입력 : ')

inputs[0].send_keys('python')

inputs[0].send_keys(Keys.ENTER)