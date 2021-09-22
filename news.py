from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])

for article in articles:
    title = article.select_one('div.news_area > a').text
    url = article.select_one('div.news_area > a')['href']
    comp = article.select_one('a.info.press').text.split(' ')[0].replace('언론사', '')
    # div.news_area > div > div.info_group > a > span

    ws1.append([title, url, comp])

driver.quit()
wb.save(filename='articles.xlsx')