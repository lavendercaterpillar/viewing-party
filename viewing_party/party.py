# ------------- WAVE 1 --------------------
#  User_data dictionary is the main data structure working with here.
# Clarifying questions:

def create_movie(title, genre, rating):
    '''
    input title and genre as strings, ratign as number
        MOVIE_TITLE_1 = "It Came from the Stack Trace"
        GENRE_1 = "Horror"
        RATING_1 = 3.5
    output is a dictionary which has 3 key/value pairs; returns None if no title or genre or rating
    '''

    #  invalid or missing input handling
    if not "title" or not "rating" or not "genre":
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
    pass



def add_to_watchlist(user_data, movie):
    '''
    input: 2 dicts
    output: is a dict with key as "watchlist" and value as a list; the list contains dictionaries of movies (3 key/value)
    '''
    pass



def watch_movie(user_data, movie):
    '''
    output: if the movie is in the data, we move the movie from the "watchlist" to the "watched" list in user_data 
    '''
    pass



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def clean_wave_2_data():
    '''
    Seems to create a clean data set similar to user_data in wave_1. 
    '''
    pass


def get_watched_avg_rating():
    pass


def get_most_watched_genre():
    pass




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

