# coding=utf-8

"""
Module that uses the content of media.py to define class movie
"""

import media
import fresh_tomatoes

# Make movie instances
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avtar = media.Movie(
    "Avtar",
    "A marine on a alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie(
    "School of Rock",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie(
    "Ratatouille",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie(
    "Hunger Games",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")

hindi_medium = media.Movie(
    "Hindi Medium",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Hindi_Medium_Poster.jpg",
    "https://www.youtube.com/watch?v=GjkFr48jk68")

logan = media.Movie(
    "Logan",
    "Storyline",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

# Collect all the movie instances in list
movies = [toy_story, avtar,
          school_of_rock,
          ratatouille,
          midnight_in_paris,
          hunger_games,
          hindi_medium,
          logan]

# Pass the movies list to open movie catalogue
fresh_tomatoes.open_movies_page(movies)
