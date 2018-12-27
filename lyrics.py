'''
Author: Aman Sharma
Python 3
lyrics() : This funciton takes name of artist and song as argument and prints lyrics
lyrics scrapped from : http://www.metrolyrics.com/
'''

# import libraries
from bs4 import BeautifulSoup 
import requests

def lyrics(artist_name, song_name):
	
	# create url
	url = 'http://www.metrolyrics.com/'+song_name+"-lyrics-"+artist_name

	# get lyrics webpage 
	web_page = requests.get(url)

	# check for status code
	if web_page.status_code == 200:
		# parse the html using beautiful soup
		soup = BeautifulSoup(web_page.content, 'html.parser')

		# find lyrics in soup
		lyrics = soup.find_all('p', {'class':'verse'})

		# print the lyrics
		for i in lyrics:
			print(i.text)

# taking name of artist and song
artist_name = input('Artist: ').lower().replace(' ', '-')
song_name = input('Song: ').lower().replace(' ', '-')
lyrics(artist_name, song_name) 
