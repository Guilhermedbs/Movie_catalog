from catalog import MovieCatalog

catalog = MovieCatalog()

catalog.add_movie(
    "Interstellar", 
    "Christopher Nolan", 
    "Science Fiction", 
    2014
)

catalog.add_movie(
    "Pulp Fiction", 
    "Quentin Tarantino", 
    "Crime", 
    1994
)

catalog.add_movie(
    "Black Panther", 
    "Ryan Coogler", 
    "Action", 
    2018
)

catalog.add_movie(
    "Parasite", 
    "Bong Joon-ho", 
    "Drama", 
    2019
)

catalog.add_movie(
    "Oppenheimer", 
    "Christopher Nolan", 
    "Historical Drama", 
    2023
)

catalog.add_movie(
    "Inglourious Basterds", 
    "Quentin Tarantino", 
    "War", 
    2009
)

user_1 = catalog.add_user("John Silva")
user_2 = catalog.add_user("Maria Oliveira")

catalog.review_movie(1, user_1['id'], 5)
catalog.review_movie(2, user_1['id'], 4)
catalog.review_movie(5, user_1['id'], 5)

catalog.review_movie(1, user_2['id'], 4)
catalog.review_movie(3, user_2['id'], 5)
catalog.review_movie(4, user_2['id'], 4)

print("Movie Catalog:")
print("\n".join(catalog.list_movies()))

drama_movies = catalog.filter_movies(lambda movie: movie['genre'] == 'Drama')
print("\nDrama Movies:")
for movie in drama_movies:
    print(f"{movie['title']} - {movie['director']} ({movie['year']})")

popular_movies = catalog.popular_movies()
print("\nTop Rated Movies:")
for movie, avg_rating, total in popular_movies:
    print(f"{movie['title']}: {avg_rating:.1f} stars ({total} ratings)")

recommendations = catalog.recommend_movies(user_1['id'])
print(f"\nRecommended Movies for {user_1['name']}:")
for movie in recommendations:
    print(f"{movie['title']} - {movie['genre']} ({movie['year']})")

similar_movies = catalog.similar_movies(1)  
print("\nMovies Similar to Interstellar:")
for movie in similar_movies:
    print(f"{movie['title']} - {movie['director']} ({movie['year']})")

movie_details = catalog.get_movie_details(1)
print(f"\nDetails of {movie_details['title']}:")
print(f"Director: {movie_details['director']}")
print(f"Genre: {movie_details['genre']}")
print(f"Year: {movie_details['year']}")
print(f"Average Rating: {movie_details['average_rating']:.1f} ({movie_details['total_reviews']} ratings)")
