from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.giniemusic_rank

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
data = requests.get('https://www.genie.co.kr/chart/top200', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# 아래 빈 칸('')을 채워보세요
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#파이썬에서 .lstrip() .rstrip() strip()은 문자열에서 공백은 제거하는 함수!
#text를 슬라이싱하는데 하필 0,1사이에있는 문자열을 가져오도록 [0:2]하는 이유는 십의자리까지 가져오도록 하기위해서, 한자리수인건 공백으로 표시됨
#title은 왼쪽에만 공백이 있어서 현재 lstrip()이나 strip()이나 사용상 차이는 없음. 아티스트명은 공백없어서 그냥 text로 가져오면 됨.
for tr in trs:
    rank = tr.select_one('td.number').text[0:2].lstrip()
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    # print(rank, title, artist)
    oneday={
    'rank': rank,
    'title': title,
    'artist': artist,
    }
    db.ginie_homework.insert_one(oneday)