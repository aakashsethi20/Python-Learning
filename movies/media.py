#!usr/bin/python

import webbrowser

class Movie():
	def __init__(self, movie_title, movie_story, movie_poster, trailer_youtube_url) :
		self.title = movie_title
		self.story = movie_story
		self.poster = movie_poster
		self.trailer = trailer_youtube_url

	def show_trailer(self) :
		webbrowser.open(self.trailer)