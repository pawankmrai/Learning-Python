import webbrowser
import random

class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # init
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = random.choice(self.VALID_RATINGS) # take a random rating from VALID_RATINGS

    # show trailer function
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
