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

	playlist = Playlist(get_artists, get_songs)
	create_playlist()
	add_songs()
	delete_old_playlist()

	new_songs = get_new_songs()
	play_count = get_play_count(new_songs())
	create_graph(play_count)


def get_artists():
	pass

def get_songs():
	pass

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