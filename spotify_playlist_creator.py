import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime

def main():

	driver = webdriver.Chrome(r'C:\Users\Sam Lewittes\Downloads\chromedriver\chromedriver.exe')

	artists = get_artists(driver)
	songs = get_songs(driver,artists)
	delete_old_playlist(driver)
	create_playlist(driver)
	add_songs(driver,songs)

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

def get_songs(driver, artists):

	songs = []
	
	for artist in artists:
		artist.replace(" ", "+")
		driver.get('https://www.google.com/search?safe=strict&hl=en&source=hp&ei=B6uAXIiyFsqEtQXr7YiQBQ&q=new+' + artist + '+songs&btnK=Google+Search&oq=new+' + artist + '+songs&gs_l=psy-ab.3..0l2j0i22i30l8.5153.8057..8240...0.0..1.229.2246.15j5j2......0....1..gws-wiz.....0..0i131j0i3.eR4WOjQ7FQU')
		sleep(.5)
		list_of_dates = driver.find_elements_by_xpath("//*[@class='jbzYp']")
		list_of_titles = driver.find_elements_by_xpath("//*[@class='title']")
		for index in range(len(list_of_dates)):
			if "2019" in list_of_dates[index].text:
				songs.append(list_of_titles[index].text)

	return list(set(songs))


def create_playlist(driver):
	
	driver.get("https://open.spotify.com/collection/playlists")
	sleep(.5)

	driver.find_element_by_class_name("asideButton").click()
	sleep(.1)
	driver.find_element_by_class_name("inputBox-input").send_keys("New Songs - " + str(datetime.datetime.today().strftime('%m-%d-%Y')))
	sleep(.5)
	driver.find_elements_by_xpath("//*[@class='button-group__item']")[1].click()

	sleep(.5)

def add_songs(driver, songs):
	
	for song in songs:
		driver.get("https://open.spotify.com/search/recent")
		sleep(.5)
		driver.find_element_by_class_name("SearchInputBox__input").send_keys(song)
		sleep(2)

		action = ActionChains(driver)
		action.move_to_element((driver.find_elements_by_xpath("//*[@class='tracklist-name ellipsis-one-line']"))[0]).perform();
		action.context_click().perform()
		sleep(.3)
		driver.find_elements_by_xpath("//*[@class='react-contextmenu-item']")[3].click()
		sleep(.3)


		possibilities = driver.find_elements_by_xpath("//*[@class='mo-info-name']")
		for index in range(len(possibilities)):
			try:
				if "New Songs - " in possibilities[index].get_attribute("title"):
					possibilities[index].click()
					sleep(.3)
					driver.find_elements_by_xpath("//*[@class='mo-coverArt-hover']")[0].click()
					sleep(.3)
			except:
				pass

		

def delete_old_playlist(driver):

	driver.get("https://open.spotify.com/collection/playlists")
	sleep(.5)

	list_of_playlists = driver.find_elements_by_xpath("//*[@class='mo-info-name']")

	for i in range(len(list_of_playlists)):

		try:
			if ("New Songs - ") in list_of_playlists[i].get_attribute("title"):
				driver.get(list_of_playlists[i].get_attribute("href"))
				sleep(.5)

				#deletes playlist
				driver.find_elements_by_xpath("//*[@class='btn btn-transparent btn--narrow']")[0].click()
				sleep(.5)
				driver.find_elements_by_xpath("//*[@class='react-contextmenu-item']")[7].click()
				sleep(.1)
				driver.find_elements_by_xpath("//*[@class='button-group__item']")[1].click()
				sleep(.5)
		except:
			pass


def get_new_songs():
	pass

def get_play_count():
	pass

def create_graph():
	pass

def add_to_csv():
	pass

main()