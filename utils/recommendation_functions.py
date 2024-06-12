import requests
import os, pickle
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
movie_list_path = os.path.join(base_dir, 'Models/movie_list.pkl')
similarity_path = os.path.join(base_dir, 'Models/similarity.pkl')

movies = pickle.load(open(movie_list_path, 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))

def fetch_movie_details(movie_id):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"
    base_url = "https://api.themoviedb.org/3"
    
    # Fetch basic movie details
    movie_url = f"{base_url}/movie/{movie_id}?api_key={api_key}&language=en-US"
    movie_data = requests.get(movie_url).json()
    
    # Fetch credits to get director and cast details
    credits_url = f"{base_url}/movie/{movie_id}/credits?api_key={api_key}&language=en-US"
    credits_data = requests.get(credits_url).json()
    
    # Extract director and producers
    director = next((member['name'] for member in credits_data['crew'] if member['job'] == 'Director'), 'N/A')
    producers = [member['name'] for member in credits_data['crew'] if member['job'] == 'Producer']
    
    # Extract cast details
    cast_details = []
    for member in credits_data['cast'][:5]:  # Get top 5 cast members
        actor_id = member['id']
        actor_details = fetch_actor_details(actor_id)
        cast_details.append({
            "name": member['name'],
            "character": member['character'],
            "profile_path": f"https://image.tmdb.org/t/p/w500/{member['profile_path']}" if member['profile_path'] else "",
            "age": actor_details.get('age', 'N/A'),
            "famous_films": actor_details.get('famous_films', 'N/A'),
            "awards": actor_details.get('awards', 'N/A')
        })
    
    # Prepare details dictionary
    details = {
        "title": movie_data.get('title', 'N/A'),
        "overview": movie_data.get('overview', 'N/A'),
        "release_date": movie_data.get('release_date', 'N/A'),
        "runtime": movie_data.get('runtime', 'N/A'),
        "genres": ", ".join([genre['name'] for genre in movie_data.get('genres', [])]),
        "poster": f"https://image.tmdb.org/t/p/w500/{movie_data.get('poster_path', '')}",
        "rating": movie_data.get('vote_average', 'N/A'),
        "director": director,
        "producers": ", ".join(producers),
        "cast": cast_details
    }

    return details

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(fetch_movie_details(movie_id))
    
    return recommended_movies

def display_star_rating(rating):
    if rating == 'N/A':
        return 'N/A'
    else:
        rating = float(rating)
        full_stars = int(rating)
        half_star = int((rating * 10) % 10 >= 5)
        empty_stars = 10 - full_stars - half_star
        return "⭐" * full_stars + "½" * half_star + "☆" * empty_stars

def fetch_actor_details(actor_id):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"
    base_url = "https://api.themoviedb.org/3"
    
    # Fetch actor details
    actor_url = f"{base_url}/person/{actor_id}?api_key={api_key}&language=en-US"
    actor_data = requests.get(actor_url).json()
    
    # Fetch actor credits
    actor_credits_url = f"{base_url}/person/{actor_id}/movie_credits?api_key={api_key}&language=en-US"
    actor_credits_data = requests.get(actor_credits_url).json()
    
    # Extract actor's age
    birthday = actor_data.get('birthday', 'N/A')
    age = calculate_age(birthday)
    
    # Extract actor's famous films
    famous_films = [credit['title'] for credit in actor_credits_data.get('cast', []) if credit['vote_average'] >= 7.5]
    
    # Extract actor's awards
    awards = actor_data.get('known_for_department', 'N/A')
    
    # Prepare actor details dictionary
    actor_details = {
        "age": age,
        "famous_films": famous_films,
        "awards": awards
    }
    
    return actor_details

def calculate_age(birthday):
    # Calculate age from birthday
    if birthday and birthday != 'N/A':
        birth_year = int(birthday.split('-')[0])
        current_year = pd.Timestamp.now().year
        age = current_year - birth_year
        return age
    else:
        return 'N/A'
