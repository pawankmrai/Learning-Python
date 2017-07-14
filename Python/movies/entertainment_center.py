import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.storyline)

avtar = media.Movie("Avtar", "A marine on a alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print (avtar.storyline)
#avtar.show_trailer()

school_of_rock = media.Movie("School of Rock", "Storyline", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


ratatouille = media.Movie("Ratatouille", "Storyline", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")


midnight_in_paris = media.Movie("Midnight in Paris", "Storyline", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=BYRWfS2s2v4")


hunger_games = media.Movie("Hunger Games", "Storyline", "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF8")


# open webbrowser
movies = [toy_story, avtar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

#fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)

print media.Movie.__module__
