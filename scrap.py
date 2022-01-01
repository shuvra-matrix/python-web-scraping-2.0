from bs4 import BeautifulSoup
import requests
import lxml

def scrap(urls):
    list=[]
    PRODUCT_URL = urls
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",'Accept-Language':"en-US,en;q=0.9"}

    request = requests.get(PRODUCT_URL,headers=header)
    supe = BeautifulSoup(request.content,'lxml')
    title = supe.find('title')
    desc = supe.find('meta' , property="og:description")
    title = title.get_text().lower()
    list.append(title)
    if desc :
        desc = desc['content'].lower()
        list.append(desc)
    else :
        list.append("No meta url given")
    return list

