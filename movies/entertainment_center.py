import media
import webbrowser
import sys

toy_story = media.Movie(
	# Title
	"300",
	# Story
	"King Leonidas goes to war with 300"+
	" Spartans against 300,000, "+
	"soldiers of Persian Lord Xerxes.",
	# Poster
	"https://upload.wikimedia.org/wikipedia/en/thumb"+
	"/5/5c/300poster.jpg/220px-300poster.jpg",
	# Trailer
	"https://www.youtube.com/watch?v=UrIbxk7idYA")
# Trailer launcher
webbrowser.open("https://www.youtube.com/watch?v=UrIbxk7idYA")

#sys.exit("Trailer launched!")
