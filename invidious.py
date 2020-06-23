from requests import get
from bs4 import BeautifulSoup
import subprocess

instance = "https://invidio.us"

def search(search_query):
    url = instance+"/search?q="+search_query

    results_list = []
    page = BeautifulSoup(get(url).text, features="html5lib")
    i=1
    for link in page.find_all('a'):
        if link.get("href")[0:6] == "/watch":
            if link.string != None:
                video_link = instance+link.get("href")
                results_list.append(video_link)
    return results_list

def play(url):
    subprocess.call(["mpv", url+"&quality=dash"])

if __name__ == "__main__":
    while True:
        search_query = input("Search something > ")
        play(search(search_query)[0])
