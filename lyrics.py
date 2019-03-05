'''
Author: Aman Sharma
Contributor : Devendra Kushwah
Python 3
get_lyrics() : This funciton takes name of artist and song as argument and prints lyrics
lyrics scrapped from : http://www.metrolyrics.com/
'''
import requests, bs4

def get_url_from_google(song,artist):
  try:
    page=requests.get("https://www.google.com/search?&q="+artist+"+"+song+"+lyrics+metrolyrics")
    soup=bs4.BeautifulSoup(page.text,'html.parser')
    data=str(((soup.find_all('div',{'class':'g'}))[0]).find_all('a')[0])
    http=data.index('http')
    html=data.index('html')
    return data[http:html+4]
  except:
    return ''
  
def get_lyrics(song,artist):
  link=get_url_from_google(song,artist)
  if(link==''):
    return ''
  page=requests.get(link)
  soup=bs4.BeautifulSoup(page.text,'html.parser')
  lyrics = soup.find_all('p', {'class':'verse'})
  for i in lyrics:
    for j in i.contents:
      if(str(j) != '<br/>'):
        print(j)

if __name__ == '__main__':
  artist=input('Artist : ')
  song=input('Song : ')
  get_lyrics(song,artist)
