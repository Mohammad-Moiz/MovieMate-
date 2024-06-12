import sqlite3

# Function to connect to SQLite database
def connect_db():
    conn = sqlite3.connect('movie_reviews.db')
    return conn

# Function to create a reviews table if it doesn't exist
def create_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            user TEXT,
            email TEXT,
            review TEXT
        )
    ''')
    conn.commit()

# Function to fetch reviews for a given movie
def fetch_reviews(movie_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM reviews WHERE movie_id=?", (movie_id,))
    reviews = c.fetchall()
    conn.close()
    return reviews

# Function to insert a review into the database
def insert_review(movie_id, user, email, review):
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO reviews (movie_id, user, email, review) VALUES (?, ?, ?, ?)", (movie_id, user, email, review))
    conn.commit()
    conn.close()