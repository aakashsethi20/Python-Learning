import media
import webbrowser
import sys

film_300 = media.Movie(
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

catch_me = media.Movie(
	# Title
	"Catch Me If You Can",
	# Story
	"A true story(?) of a FBI chasing a con artist.",
	# Poster
	"https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Catch_"+
	"Me_If_You_Can_2002_movie.jpg/220px-Catch_Me_If_You_Can_2002_movie.jpg",
	# Trailer
	"https://www.youtube.com/watch?v=SosRcIMCr5g"
	)

pulp_fiction = media.Movie(
	# Title
	"Pulp Fiction",
	# Story
	"Pulp Fiction connects the intersecting storylines of Los Angeles mobsters,"+
	" fringe players, small-time criminals, and a mysterious briefcase.",
	#Poster
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Pulp_Fiction_cover"+
	".jpg/220px-Pulp_Fiction_cover.jpg",
	#Trailer
	"https://www.youtube.com/watch?v=s7EdQ4FqbhY"
	)

pulp_fiction.show_trailer()
#sys.exit("Trailer launched!")
