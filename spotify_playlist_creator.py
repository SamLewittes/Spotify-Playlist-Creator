import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Playlist:
	def __init__(self,artists,songs):
		self.artists = artists
		self.songs = songs


def main():

	driver = webdriver.Chrome(r'C:\Users\Sam Lewittes\Downloads\chromedriver\chromedriver.exe')

	playlist = Playlist(get_artists(driver), get_songs(driver))
	print(playlist.artists)
	#create_playlist()
	#add_songs()
	#delete_old_playlist()

	#new_songs = get_new_songs()
	#play_count = get_play_count(new_songs())
	#create_graph(play_count)


def get_artists(driver):

	spotify_login(driver)

	artist_list = driver.find_elements_by_xpath("//*[@class='mo-info-name']")

	for i in range(len(artist_list)):
		artist_list[i] = artist_list[i].get_attribute("title")

	return(artist_list)

def spotify_login(driver):
	username_request = input("Please enter your spotify username/email: ")
	password_request = input("Please enter your spotify password: ")

	driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fbrowse%2Ffeatured")

	username = driver.find_element_by_id('login-username')
	username.send_keys(username_request)

	password = driver.find_element_by_id('login-password')
	password.send_keys(password_request)
	sleep(.5)

	driver.find_element_by_id('login-button').click()
	sleep(.5)

	driver.get("https://open.spotify.com/collection/artists")




def get_songs(driver):
	return[]

def create_playlist():
	pass

def add_songs():
	pass

def delete_old_playlist():
	pass


def get_new_songs():
	pass

def get_play_count():
	pass

def create_graph():
	pass

main()