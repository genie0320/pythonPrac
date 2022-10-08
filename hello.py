import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://genie:sparta@cluster0.blce7zu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20221007', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')
    title = ""
    grade = ""
    start = ""

    if a is not None:
        title = a.text
        grade = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text

        doc = {
            'title': title,
            'grade': grade,
            'star': star
        }

        db.movies.insert_one(doc)
        # print(grade, title, star)

    print(db.movies.find_one({'name': title}))
