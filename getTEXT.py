from bs4 import BeautifulSoup
import urllib.request
import ssl

def getContent(url) :
    ssl._create_default_https_context = ssl._create_unverified_context
    content = urllib.request.urlopen(url)
    read_content = content.read()
    soup = BeautifulSoup(read_content,'html.parser')

    h1All = soup.find_all('h1')
    AllSpecdiv = soup.find_all('div', class_="idocBlock")
    #title
    print(h1All[1].text)
    f.write(h1All[1].text + "\n")
    #content
    contentText = ""
    for n in AllSpecdiv :
        #print(n.text)
        f.write(n.text + "\n")

ssl._create_default_https_context = ssl._create_unverified_context
content = urllib.request.urlopen("https://www.iletaitunehistoire.com/genres/contes-et-legendes")
read_content = content.read()
soup = BeautifulSoup(read_content,'html.parser')
f = open("ComteLegendesDatasets.txt", "a")
i = 0
txt = ""
for i in range(91) :
    getContent("url_page"+ str(i) +"#histoire")
    #print("https://www.iletaitunehistoire.com/genres/contes-et-legendes/lire/biblidcon_0"+ str(i) +"#histoire")

f.close()


