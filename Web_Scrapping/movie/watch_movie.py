import requests
from bs4 import BeautifulSoup
import pandas as pd

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content=(response.text)
soup = BeautifulSoup(content,"html.parser")
title=soup.find_all(name="h3", class_="title")
print(title)
movie=[item.getText() for item in title]
# for n in range(len(movie)-1,-1,-1):
#     print(movie[n])
movies=movie[::-1]
file=pd.DataFrame(movies)
file1=file.to_csv("movie_name.csv",index=False)



