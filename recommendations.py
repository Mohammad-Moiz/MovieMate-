import streamlit as st
import pickle
from utils.recommendation_functions import fetch_movie_details, display_star_rating, recommend

def app():
    st.title('Movie Recommendations')

    movies = pickle.load(open('utils/Models/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('utils/Models/similarity.pkl', 'rb'))

    movie_list = movies['title'].values
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

    if st.button('Show Recommendation'):
        movie_details = fetch_movie_details(movies[movies['title'] == selected_movie].iloc[0].movie_id)

        st.subheader(movie_details['title'])
        st.image(movie_details['poster'])
        st.write(f"**Overview:** {movie_details['overview']}")
        st.write(f"**Release Date:** {movie_details['release_date']}")
        st.write(f"**Runtime:** {movie_details['runtime']} minutes")
        st.write(f"**Genres:** {movie_details['genres']}")
        st.write(f"**Rating:** {movie_details['rating']} ({display_star_rating(movie_details['rating'])})")
        st.write(f"**Director:** {movie_details['director']}")
        st.write(f"**Producers:** {movie_details['producers']}")
        st.write("**Cast:**")
        for cast in movie_details['cast']:
            col1, col2 = st.columns([1, 4])
            with col1:
                if cast['profile_path']:
                    st.image(cast['profile_path'])
            with col2:
                st.write(f"{cast['name']} as {cast['character']}")

        st.write("---")
        st.write("**Recommended Movies:**")

        recommended_movies = recommend(selected_movie)

        for idx, movie in enumerate(recommended_movies):
            if st.button(movie['title'], key=idx):
                st.subheader(movie['title'])
                st.image(movie['poster'])
                st.write(f"**Overview:** {movie['overview']}")
                st.write(f"**Release Date:** {movie['release_date']}")
                st.write(f"**Runtime:** {movie['runtime']} minutes")
                st.write(f"**Genres:** {movie['genres']}")
                st.write(f"**Rating:** {movie['rating']} ({display_star_rating(movie['rating'])})")
                st.write(f"**Director:** {movie['director']}")
                st.write(f"**Producers:** {movie['producers']}")
                st.write("**Cast:**")
                for cast in movie['cast']:
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        if cast['profile_path']:
                            st.image(cast['profile_path'])
                    with col2:
                        st.write(f"{cast['name']} as {cast['character']}")
                st.write("---")
