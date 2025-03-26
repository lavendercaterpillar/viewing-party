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

def get_watched_avg_rating(user_date):
    '''
    receives user_data dict and returns average of all movies ratings in watched list
    '''
    counter = 0
    sum = 0
    for movie in user_date["watched"]:
        sum += movie["rating"]
        counter += 1
    
    if counter != 0:
        return sum/counter
    else:
        return 0


def get_most_watched_genre(user_data):
    
    genre_frequency = {}

    for movie in user_data["watched"]:
        if movie["genre"] not in genre_frequency:
            genre_frequency[movie["genre"]] = 1
        else:
            genre_frequency[movie["genre"]] += 1
    
    most_watched_genre = None
    most_watched_freq = 0

    for genre, frequency in genre_frequency.items():
        if frequency > most_watched_freq:
            most_watched_freq = frequency
            most_watched_genre = genre
    
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
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

#------------ Wave 01 Print statement Tests -----------
