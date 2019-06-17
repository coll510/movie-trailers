import webbrowser

class Movie():

	def __init__(self, movie_title, movie_storyline, poster_image, 
				trailer_youtube, movie_link):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.movie_link = movie_link


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url) # Use self to access this instance variable