from omdblib import OMDB

def get_ratings(movie_titles):
    omdb = OMDB("b87452b6")

    ratings = []
    for title in movie_titles:
        movie = omdb.title_search(title)
        ratings.append(movie.rotten_tomatoes_score)
    return ratings


if __name__ == '__main__':
    from nfrtitles import get_nfr_title_list
    movies = get_nfr_title_list()
    # movies = ["Star Wars", "Return of the Jedi", "The Empire Strikes Back"]
    ratings = get_ratings(movies)
    print(f"ratings: {ratings}")

