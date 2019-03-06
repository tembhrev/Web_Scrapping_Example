from bs4 import BeautifulSoup
from collections import OrderedDict
import urllib3
import re

url = "https://en.wikipedia.org/wiki/List_of_Bollywood_films_of_2018"


def format_decorator(func):    
    def inner(*args):
        print("*"*30)
        return func(*args)    
    return inner

        
@format_decorator
def highest_grossing_movies(top_10):
    """
    function to list the Highest worldwide gross of 2018 from Bollywood
    """
    highest_gross = re.findall(r"(?:</span>)(.*?)(?:\s.*)", top_10)
    movies = re.findall(r"(?:<i><a href=\"/wiki/)(.*?)(?:\".*)", top_10)
    movie_dict = OrderedDict(zip(movies,highest_gross))
    print("HIGHEST GROSSING MOVIES 2018")
    print("*"*30)
    for movie in movie_dict:
        print(movie,":",movie_dict[movie],"crores")

@format_decorator
def all_movies(movie_list):
    count = 0
    for i in range(1,len(movie_list)):
        data = []
        soup = BeautifulSoup(str(movie_list[i]),features = 'lxml')
        [data.append(node.findAll(text=True)) for node in soup.findAll('i')]
        [str(val) for item in data for val in item if not str(val).isdigit()]
        count += len([str(val) for item in data for val in item if not str(val).isdigit()])
    return(count)
        


if __name__ == "__main__":
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    data = r.data.decode('utf-8')
    soup = BeautifulSoup(data,features = 'lxml')
    movie_list = soup.findAll('table', {'class': 'wikitable'})
    highest_grossing_movies(str(movie_list[0]))
    print("Movies released in 2018 :",all_movies(movie_list))

    
