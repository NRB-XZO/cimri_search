import requests
from os import system
from bs4 import BeautifulSoup
while True:
    try:
        system("clear")
        system("figlet cimri")
        x = str(input("Arama:"))
        url = "https://www.cimri.com/arama?q={}".format(x)
        responce = requests.get(url)
        html_icerigi = responce.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        for i in soup.find_all("h3", {"class": "product-title"}):
            print(i.text)
            print("********************************")

        asd = input("\033[93;1m[+]\033 Devam etmek icin herhangi bir tusa basiniz.")
    except:
        print("Devam")