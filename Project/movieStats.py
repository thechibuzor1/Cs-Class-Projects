# Import libraries

from matplotlib import pyplot as plt

import numpy as np
from tmdbv3api import TMDb, Movie
tmdb = TMDb()
tmdb.api_key = '056e8c6cdd9f7aae4cc11feadce7922c'


# Creating dataset

movies = []
popularity = []

movie = Movie()
popular = movie.popular()
for p in popular:
    movies.append(p.title)
    popularity.append(p.popularity)
    

fig = plt.figure(figsize=(10, 7))
plt.title("CURRENTLY TRENDING MOVIES AND THEIR POPULARITY RATING")
plt.pie(popularity, labels=movies)

# show plot
plt.show()
