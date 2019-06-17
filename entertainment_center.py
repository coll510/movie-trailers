import media
import fresh_tomatoes

love_and_basketball = media.Movie("Love & Basketball", 
								"Monica and Quincy love and play basketball together through many life challenges from childhood to adulthood.", 
								"/home/lurial/src/build_programs/movies/movie-posters/2000-poster-love_and_basketball-1.jpg", 
								"https://www.youtube.com/watch?v=Ur83i6_BjbE",
								"https://en.wikipedia.org/wiki/Love_%26_Basketball")

water_boy = media.Movie("The Waterboy", 
						"A waterboy for a college football team discovers he has a unique tackling ability and becomes a member of the team.",
						"/home/lurial/src/build_programs/movies/movie-posters/1998-poster-waterboy-2.jpg",
						"https://www.youtube.com/watch?v=1HYpS-KF_pg", 
						"https://en.wikipedia.org/wiki/The_Waterboy")

black_panther = media.Movie("Black Panther", 
							"After the death of his father, T'Challa returns home to the African nation of Wakanda to take his rightful place as king.", 
							"/home/lurial/src/build_programs/movies/movie-posters/Black-Panther-poster-main-xl.jpg",
							"https://www.youtube.com/watch?v=xjDjIWPwcPU",
							"https://en.wikipedia.org/wiki/Black_Panther_(film)")

fast_five = media.Movie("Fast Five", 
						"Dominic Toretto and his crew of street racers plan a massive heist to buy their freedom while in the sights of a powerful Brazilian drug lord and a dangerous federal agent.",
						"/home/lurial/src/build_programs/movies/movie-posters/fast-five-final-poster.jpg", 
						"https://www.youtube.com/watch?v=mw2AqdB5EVA",
						"https://en.wikipedia.org/wiki/Fast_Five")

avatar = media.Movie("Avatar", 
					"A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.", 
					"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					"https://www.youtube.com/watch?v=6ziBFh3V1aM",
					"https://en.wikipedia.org/wiki/Avatar")




creed = media.Movie("Creed II", 
							"Under the tutelage of Rocky Balboa, newly crowned heavyweight champion Adonis Creed faces off against Viktor Drago, the son of Ivan Drago.",
							"/home/lurial/src/build_programs/movies/movie-posters/creed21200poster.jpg", 
							"https://www.youtube.com/watch?v=cPNVNqn4T9I", 
							"https://en.wikipedia.org/wiki/Creed_II")


movies = [love_and_basketball, water_boy, black_panther, fast_five, avatar, creed]
fresh_tomatoes.open_movies_page(movies)
#print(avatar.title, ":", avatar.storyline)
#avatar.show_trailer()
#love_and_basketball.show_trailer()
				