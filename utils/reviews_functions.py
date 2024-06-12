import requests
from textblob import TextBlob

def fetch_movie_reviews(movie_title):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"
    base_url = "https://api.themoviedb.org/3"
    
    # Find the movie ID from its title
    search_url = f"{base_url}/search/movie?api_key={api_key}&query={movie_title}"
    search_response = requests.get(search_url).json()
    if not search_response['results']:
        return []
    
    movie_id = search_response['results'][0]['id']
    
    # Fetch reviews for the movie
    reviews_url = f"{base_url}/movie/{movie_id}/reviews?api_key={api_key}&language=en-US"
    reviews_response = requests.get(reviews_url).json()
    
    reviews = [review['content'] for review in reviews_response['results']]
    return reviews

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def highlight_sentiment(text):
    sentiment = analyze_sentiment(text)
    if sentiment == "positive":
        return f'<span style="color:green">{text}</span>'
    elif sentiment == "negative":
        return f'<span style="color:red">{text}</span>'
    else:
        return text