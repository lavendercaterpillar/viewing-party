# ------------- WAVE 1 --------------------
#  User_data dictionary is the main data structure working with here.

# Clarifying questions:

# invalid or missing input handling
# what if user_data = {}

def create_movie(title, genre, rating):
    '''
    input title and genre as strings, rating as number
    output is a dictionary which has 3 key/value pairs; 
    returns None if no title or genre or rating
    '''

    if not title or not rating or not genre:
        return None
    else:
        return {"title": title,
                "genre": genre, 
                "rating" : rating
                }
        

def add_to_watched(user_data, movie):
    '''
    input: movie is a dictionary of 3 key/value pairs. User_data is a nested dict with 1 key ("watched") 
    and value as a list that has a dictionary of movie(s)
    output: function adds the movie dict information to the "watched" list of user
    '''
    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    '''
    input: 2 dicts
    output: is a dict with key as "watchlist" and value as a list; the list contains dictionaries of movies (3 key/value)
    '''    
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    '''
    output: if the movie's title is in the user_data watchlist movies, 
    function moves the movie from the "watchlist" to the "watched" in user_data 
    '''
    movies_to_remove = []
    for movies in user_data["watchlist"]:
        if movies["title"] == title:
            user_data["watched"].append(movies)
            movies_to_remove.append(movies)
    
    for movie in movies_to_remove:
        user_data["watchlist"].remove(movies)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies

# amandas_data = {
#         "watched": [
#             HORROR_1,
#             FANTASY_1,
#             INTRIGUE_1
#         ],
#         "friends": [
#             {
#                 "watched": [
#                     HORROR_1,
#                     FANTASY_1,
#                 ]
#             },
#             {
#                 "watched": []
#             }
#         ]
#     }

def get_unique_watched(user_data):
    user_watched = set()
    friends_watched = set()
    for movies in user_data["watched"]:
        user_watched.add(movies["title"])
    for each_firend in user_data["friends"]:
        for friend_movies in each_firend["watched"]:
            friends_watched.add(friend_movies["title"])
    movie_title = user_watched - friends_watched
    
    unique_movie =[]
    for movies in user_data["watched"]:
        if movies["title"] in movie_title :
            unique_movie.append(movies)
    
    return unique_movie



# 2. Create a function named `get_friends_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies

def get_friends_unique_watched(user_data):
    user_watched = set()
    friends_watched = set()
    for movies in user_data["watched"]:
        user_watched.add(movies["title"])
    for each_firend in user_data["friends"]:
        for friend_movies in each_firend["watched"]:
            friends_watched.add(friend_movies["title"])
    movie_title = friends_watched - user_watched

    friends_unique_movie = []
    seen_titles = set()
    for firend in user_data["friends"]:
        for friend_movies in firend["watched"]:
            if friend_movies["title"] in movie_title and friend_movies["title"] not in seen_titles:
                friends_unique_movie.append(friend_movies)
                seen_titles.add(friend_movies["title"])
    
    return friends_unique_movie

    

    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------













#------------ Wave 01 Print statement Tests -----------
# MOVIE_TITLE_1 = "It Came from the Stack Trace"
# GENRE_1 = ""
# # GENRE_1 = "Horror"
# RATING_1 = 3.5

# movie = {
#     "title": MOVIE_TITLE_1,
#     "genre": GENRE_1,
#     "rating": RATING_1
# }
# user_data = {
#     "watched": [],
#     "watchlist": []
# }

# user_data = {
#     "watchlist": []
# }

# user_data = {
#     "watched": [],
# }

# user_data = {
#     "watched": [{
#     "title": "The Lord of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# }],
#     "watchlist": []
# }

# janes_data = {
#         "watchlist": [{
#             "title": MOVIE_TITLE_1,
#             "genre": GENRE_1,
#             "rating": RATING_1
#         }],
#         "watched": []
#     }

# print(create_movie(MOVIE_TITLE_1, GENRE_1, RATING_1))
# print(add_to_watched(user_data, movie))
# print(add_to_watchlist(user_data, movie))
# print(watch_movie(user_data, MOVIE_TITLE_1))