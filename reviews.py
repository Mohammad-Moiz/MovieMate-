import streamlit as st
import pickle
from utils.reviews_functions import fetch_movie_reviews, highlight_sentiment

def app():
    st.title('Movie Reviews')

    movies = pickle.load(open('utils/Models/movie_list.pkl', 'rb'))
    movie_list = movies['title'].values
    selected_review_movie = st.selectbox("Select a movie to see its reviews", movie_list)
    if st.button('Movie Reviews'):
        if selected_review_movie:
            movie_reviews = fetch_movie_reviews(selected_review_movie)
            if movie_reviews:
                for review in movie_reviews:
                    st.markdown(highlight_sentiment(review), unsafe_allow_html=True)
            else:
                st.write("No reviews available for this movie.")
