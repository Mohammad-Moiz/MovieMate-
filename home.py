import streamlit as st
import pandas as pd
from recommendations import fetch_movie_details
from utils.home_functions import load_data

def app():
    st.title('Welcome to MovieMate!')

    # Load IMDb dataset
    movies_metadata = load_data()

    # Apply custom CSS for styling
    st.markdown("""
        <style>
        body {{
            background-color: #f2f2f2;  /* Light gray background */
            color: black;
            padding: 20px;
        }}
        .main {{
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .stButton>button {{
            background-color: #f63366;
            color: white;
            border-radius: 10px;
        }}
        .stButton>button:hover {{
            background-color: #ff4b4b;
        }}
        .stTextArea textarea {{
            background: rgba(255, 255, 255, 0.1);
            color: black;
        }}
        .tabs {{
            background-color: #e6e6e6;  /* Light gray color for tabs */
            border-radius: 10px;
            padding: 10px;
            margin-top: 20px;
        }}
        .tab-content {{
            background-color: #ffffff;  /* White color for remaining portion */
            border-radius: 10px;
            padding: 20px;
            margin-top: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .movie-img {{
            width: 150px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        </style>
    """, unsafe_allow_html=True)

    # Main container
    with st.container():
        # Display some movie titles and images
        st.subheader('Featured Movies')
        row1_col1, row1_col2, row1_col3 = st.columns(3)
        for index, movie in movies_metadata.head(9).iterrows():
            if index < 3:
                with row1_col1:
                    st.image(fetch_movie_details(movie['id'])['poster'], caption=movie['title'], use_column_width=True)
                    st.write(movie['title'])

            elif index < 6:
                with row1_col2:
                    st.image(fetch_movie_details(movie['id'])['poster'], caption=movie['title'], use_column_width=True)
                    st.write(movie['title'])

            else:
                with row1_col3:
                    st.image(fetch_movie_details(movie['id'])['poster'], caption=movie['title'], use_column_width=True)
                    st.write(movie['title'])
