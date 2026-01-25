from urllib.request import urlopen
from bs4 import BeautifulSoup

def recursive_path(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, features="html.parser")
    for tag in soup.find_all('a'):
        if tag.contents[0] != "../":
            next_url = url + tag.contents[0]
            if next_url[-1] == '/':
                recursive_path(next_url)
            else:
                flag = urlopen(next_url).read().decode("utf-8")
                if flag.find("flag") != -1:
                    print(next_url)
                    print(flag)
                    exit()

print("Which site web are we crawling today ?")
url = input()
print("Please wait here")
recursive_path(url)
