from bs4 import BeautifulSoup
from collections import OrderedDict
import urllib3
import re


def Highest_Grossing_Movie(soup):
    content = []
    for item in soup.find("table", {"class" : "wikitable"}):
        content.append(item)
    highest_gross = re.findall(r"(?:</span>)(.*?)(?:\s.*)", str(content))
    movies = re.findall(r"(?:<i><a href=\"/wiki/)(.*?)(?:\".*)", str(content))
    movie_dict = OrderedDict(zip(movies,highest_gross))
    for movie in movie_dict:
        print(movie,":",movie_dict[movie],"crores")

if __name__ == "__main__":
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    r = http.request("GET","https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2018")
    data = r.data.decode('utf-8')
    soup = BeautifulSoup(data,features = 'lxml')
    Highest_Grossing_Movie(soup)
    
    
    











































    


