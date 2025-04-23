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
    
    return {
                "title": title,
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

# from collections import Counter

def get_most_watched_genre(user_data):

    # if not user_data["watched"]:
    #     return None
    # genre_counter_list = [movie["genre"] for movie in user_data["watched"]]
    # genre_counter = Counter(genre_counter_list)
    # most_watched_genre = genre_counter.most_common(1)[0][0]
    # return most_watched_genre


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
    # seen_titles = set()
    for firend in user_data["friends"]:
        for friend_movies in firend["watched"]:
            if friend_movies["title"] in movie_title \
                 and friend_movies not in friends_unique_movie:

            # friend_movies["title"] not in seen_titles:
                friends_unique_movie.append(friend_movies)
                # seen_titles.add(friend_movies["title"])
    
    return friends_unique_movie

    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    get_recs = []
    friends_unique_movie = get_friends_unique_watched(user_data) 
    for movie in friends_unique_movie:
        if movie["host"] in user_data.get("subscriptions",[]):
            get_recs.append(movie)

    return get_recs



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    recomm_movies = get_available_recs(user_data)
    
    # to check the edge cases of the genre not in user list 
    # or user with indifferent genre

    recomm_by_genre = []
    for movie in recomm_movies:
        if movie["genre"] == most_watched_genre:
            recomm_by_genre.append(movie)

    return recomm_by_genre


def get_rec_from_favorites(user_data):

    friends_watched_title = set()
    for each_friend in user_data["friends"]:
        for friend_movies in each_friend["watched"]:
            friends_watched_title.add(friend_movies["title"])

    rec_from_favorite_list = []
    if not user_data["favorites"]:
        return []
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_watched_title:
            rec_from_favorite_list.append(movie)
    
    return rec_from_favorite_list
    
