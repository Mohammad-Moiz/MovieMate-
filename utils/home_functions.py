import pandas as pd

# Function to load IMDb dataset
def load_data():
    movies_metadata = pd.read_csv('Data/tmdb_5000_movies.csv', low_memory=False)
    return movies_metadata