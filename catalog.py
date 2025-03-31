from typing import List, Dict, Callable, Tuple
import functools

class MovieCatalog:
    def __init__(self):
        def generate_id():
            counter = 0
            def increment():
                nonlocal counter
                counter += 1
                return counter
            return increment
        
        self.generate_movie_id = generate_id()
        self.generate_user_id = generate_id()
        self.movies = []
        self.users = []
        self.reviews = []

    def process_operation(self, operation: Callable, *args):
        try:
            result = operation(*args)
            self.log_operation(operation.__name__)
            return result
        except Exception as e:
            print(f"Error in operation: {e}")
            return None

    def filter_movies(self, criterion: Callable[[Dict], bool]) -> List[Dict]:
        return list(filter(criterion, self.movies))

    def list_movies(self) -> List[str]:
        return [f"Movie: {movie['title']} ({movie['year']}) - Director: {movie['director']}" for movie in self.movies]

    def add_movie(self, title: str, director: str, genre: str, year: int):
        movie = {
            'id': self.generate_movie_id(),
            'title': title,
            'director': director,
            'genre': genre,
            'year': year,
        }
        self.movies.append(movie)
        return movie

    def add_user(self, name: str):
        user = {
            'id': self.generate_user_id(),
            'name': name
        }
        self.users.append(user)
        return user

    def review_movie(self, movie_id: int, user_id: int, rating: int):
        """Reviews a movie with a rating from 1 to 5 stars"""
        movie = next((m for m in self.movies if m['id'] == movie_id), None)
        user = next((u for u in self.users if u['id'] == user_id), None)
        
        if not movie or not user:
            return None
            
        if 1 <= rating <= 5:
            review = {
                'id': len(self.reviews) + 1,
                'movie_id': movie_id,
                'user_id': user_id,
                'rating': rating,
            }
            self.reviews.append(review)
            return review
        return None

    def get_movie_reviews(self, movie_id: int) -> List[Dict]:
        """Returns all reviews for a specific movie"""
        return [r for r in self.reviews if r['movie_id'] == movie_id]

    def get_user_reviews(self, user_id: int) -> List[Dict]:
        """Returns all reviews made by a specific user"""
        return [r for r in self.reviews if r['user_id'] == user_id]

    def average_rating(self, movie_id: int) -> float:
        """Calculates the average rating of a movie"""
        movie_reviews = self.get_movie_reviews(movie_id)
        if not movie_reviews:
            return 0.0
        
        total = functools.reduce(
            lambda acc, rev: acc + rev['rating'], 
            movie_reviews, 
            0
        )
        return total / len(movie_reviews)

    def recommend_movies(self, user_id: int, quantity: int = 5) -> List[Dict]:
        """Recommends movies to a user based on ratings above 3 for genre and director"""
        user = next((u for u in self.users if u['id'] == user_id), None)
        if not user:
            return []
        
        good_reviews = [r for r in self.get_user_reviews(user_id) if r['rating'] > 3]
        
        reviewed_movies = [r['movie_id'] for r in self.get_user_reviews(user_id)]

        approved_genres = set()
        approved_directors = set()
        
        for review in good_reviews:
            movie = next((m for m in self.movies if m['id'] == review['movie_id']), None)
            if movie:
                approved_genres.add(movie['genre'])
                approved_directors.add(movie['director'])
        
        def recommendation_score(movie):
            score = 0
            if movie['genre'] in approved_genres:
                score += 2
            if movie['director'] in approved_directors:
                score += 3
            return score
        
        unseen_movies = self.filter_movies(
            lambda m: m['id'] not in reviewed_movies
        )
        
        recommendations = sorted(
            unseen_movies,
            key=recommendation_score,
            reverse=True
        )
        
        return recommendations[:quantity]

    def similar_movies(self, movie_id: int, quantity: int = 3) -> List[Dict]:
        """Finds similar movies based on genre and director"""
        movie = next((m for m in self.movies if m['id'] == movie_id), None)
        
        if not movie:
            return []

        similar = self.filter_movies(
            lambda m: m['id'] != movie_id and (m['genre'] == movie['genre'] or m['director'] == movie['director'])
         )

        def calculate_similarity(m):
            points = 0
            if m['genre'] == movie['genre']:
                points += 3
            if m['director'] == movie['director']:
                points += 4
            return points

        return sorted(similar, key=calculate_similarity, reverse=True)[:quantity]

    def popular_movies(self, min_reviews: int = 1) -> List[Tuple[Dict, float]]:
        """Returns the most highly rated movies, with a minimum number of reviews"""
        result = []
        
        for movie in self.movies:
            reviews = self.get_movie_reviews(movie['id'])
            if len(reviews) >= min_reviews:
                average = functools.reduce(lambda acc, rev: acc + rev['rating'], reviews, 0) / len(reviews)
                result.append((movie, average, len(reviews)))
        
        return sorted(result, key=lambda x: x[1], reverse=True)

    def get_movie_details(self, movie_id: int) -> Dict:
        """Returns basic details of a movie, including average rating"""
        movie = next((m for m in self.movies if m['id'] == movie_id), None)
        if not movie:
            return None
        
        details = movie.copy()
        details['average_rating'] = self.average_rating(movie_id)
        
        reviews = self.get_movie_reviews(movie_id)
        details['total_reviews'] = len(reviews)
        
        return details
