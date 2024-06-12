import streamlit as st
from utils.your_reviews_functions import connect_db, create_table, fetch_reviews, insert_review

def app():
    st.title('Movie Reviews')

    # Create reviews table if it doesn't exist
    conn = connect_db()
    create_table(conn)

    # Sample movie IDs and titles
    movies = {
        "Inception": 1,
        "The Shawshank Redemption": 2,
        "The Dark Knight": 3,
        "Pulp Fiction": 4,
        "The Godfather": 5
    }

    # Dropdown to select a movie
    selected_movie_name = st.selectbox("Select a movie:", list(movies.keys()))

    # Fetch reviews for the selected movie
    selected_movie_id = movies[selected_movie_name]
    reviews = fetch_reviews(selected_movie_id)

    # Display movie title
    st.subheader(f"Reviews for {selected_movie_name}")

    # Display existing reviews
    for review in reviews:
        st.write(f"**{review[2]}** says: {review[4]}")

    # Post Review section
    st.subheader("Post Your Review")

    # Get user's name
    user_name = st.text_input("Your Name:", "")

    # Get user's email
    user_email = st.text_input("Your Email:", "")

    # Get user's review
    user_review = st.text_area("Write your review here:", "")

    # Button to post review
    if st.button("Post Review"):
        # Insert the review into the database
        insert_review(selected_movie_id, user_name, user_email, user_review)
        st.success("Review posted successfully!")
