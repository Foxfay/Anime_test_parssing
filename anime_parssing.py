import requests
from bs4 import BeautifulSoup
from class_lib import *
anime_slk=[]
url=['http://www.world-art.ru/animation/animation.php?id=262','http://www.world-art.ru/animation/animation.php?id=803']
for link in url:
    full_page = requests.get(link)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    find_name = soup.find('td', class_='review', text='Название (ромадзи)')
    find_tip = soup.find('td', class_='review', text='Тип')
    find_rating = soup.find('a', class_='review', href='rating_top.php')
    f=find_rating.parent.parent
    find_ann=soup.find('p', attrs={'align':'justify'}, class_='review')
    name = (find_name.find_next_sibling().find_next_sibling()).text
    tip=(find_tip.find_next_sibling().find_next_sibling()).text
    rating=(f.find_next_sibling().find_next_sibling()).text


    anime.tip=tip
    anime.rating=rating
    anime.ann=find_ann.text
    anime_slk.append(anime)
print(anime_slk[0].ann)
