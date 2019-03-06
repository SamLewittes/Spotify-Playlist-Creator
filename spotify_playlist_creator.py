import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime

class Playlist:
	def __init__(self,artists,songs):
		self.artists = artists
		self.songs = songs


def main():

	driver = webdriver.Chrome(r'C:\Users\Sam Lewittes\Downloads\chromedriver\chromedriver.exe')

	#playlist = Playlist(get_artists(driver), get_songs(driver))
	#print(playlist.artists)

	spotify_login(driver)
	#create_playlist(driver)
	delete_old_playlist(driver)



	#create_playlist()
	#add_songs()
	#delete_old_playlist()

	#new_songs = get_new_songs()
	#play_count = get_play_count(new_songs())
	#create_graph(play_count)


def get_artists(driver):

	spotify_login(driver)

	driver.get("https://open.spotify.com/collection/artists")

	sleep(.5)

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

def get_songs(driver):
	return[]

def create_playlist(driver):
	
	driver.get("https://open.spotify.com/collection/playlists")
	sleep(.5)

	driver.find_element_by_class_name("asideButton").click()
	sleep(.1)
	driver.find_element_by_class_name("inputBox-input").send_keys("New Songs - " + str(datetime.datetime.today().strftime('%m-%d-%Y')))
	sleep(.5)
	driver.find_elements_by_xpath("//*[@class='button-group__item']")[1].click()

	sleep(.5)

def add_songs():
	pass

def delete_old_playlist(driver):

	driver.get("https://open.spotify.com/collection/playlists")
	sleep(.5)

	list_of_playlists = driver.find_elements_by_xpath("//*[@class='mo-info-name']")

	for i in range(len(list_of_playlists)):

		if ("New Songs - ") in list_of_playlists[i].get_attribute("title"):
			driver.get(list_of_playlists[i].get_attribute("href"))
			sleep(.5)

			driver.find_element_by_xpath("//*[@class='btn btn-transparent btn--narrow']").click()
			sleep(.5)
			driver.find_elements_by_xpath("//*[@class='react-contextmenu-item']")[7].click()
			sleep(.1)
			driver.find_elements_by_xpath("//*[@class='button-group__item']")[1].click()
			sleep(.5)



def get_new_songs():
	pass

def get_play_count():
	pass

def create_graph():
	pass

main()