# webdriver > 이종간의 소프트웨어 드라이버(중간에서 연결하는) 역할
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#02 - naver.com login 자동화
browser = webdriver.Chrome()
browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

# id, pw  > 아이디 & 비밀번호
idForInput = browser.find_element(By.ID, 'id')
idForInput.send_keys('gildong')

pwForInput = browser.find_element(By.ID, 'pw')
pwForInput.send_keys('1234')

# log.login > 버튼 id
loginBtn = browser.find_element(By.ID, 'log.login')
loginBtn.click()

