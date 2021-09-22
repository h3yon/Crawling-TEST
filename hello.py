from bs4 import BeautifulSoup
from selenium import webdriver
import dload
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EC%84%9C%EA%B0%95%EC%A4%80")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select("#imgList > div > a > img")

i = 1
for thumbnail in thumbnails:
    src = thumbnail["src"]
    dload.save(src,f'img_homework/{i}.jpg')
    i += 1

driver.quit()