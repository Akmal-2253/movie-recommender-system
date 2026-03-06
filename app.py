import streamlit as st
import joblib
import requests
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# API Key & Placeholder 
API_KEY = "f03e5511ca56e916189139271ec362e9"
NO_POSTER = "https://via.placeholder.com/500x750?text=No+Poster"

# Minimal CSS
st.markdown("""
    <style>
    .movie-title { text-align: center; font-size: 13px; font-weight: bold; margin-top: 8px; min-height: 40px; }
    .match-score { text-align: center; font-size: 12px; }
    img { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# Page Config 
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# API Function 
def fetch_movie_details(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US',
            timeout=5
        )
        data = response.json()
        poster = f"https://image.tmdb.org/t/p/w500{data['poster_path']}" if data.get('poster_path') else NO_POSTER
        rating = data.get('vote_average', 'N/A')
        overview = data.get('overview', 'No overview available.')
        genres = ", ".join([g['name'] for g in data.get('genres', [])])
        release = data.get('release_date', 'N/A')[:4] if data.get('release_date') else 'N/A'
        return poster, rating, overview, genres, release
    except:
        return NO_POSTER, "N/A", "No overview available.", "N/A", "N/A"

# Load Data & Recreate Similarity
@st.cache_resource
def load_data():
    # Change this line:
    movies = joblib.load('movies.pkl')  # ← joblib instead of pickle!
    
    # Recreate similarity at runtime
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags'])
    sim = cosine_similarity(vectors)
    
    return movies, sim

movies_df, similarity = load_data()
movies_list = movies_df['title'].values

# Recommend Function 
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    results = []
    for i in movies_sorted:
        row = movies_df.iloc[i[0]]
        poster, rating, overview, genres, release = fetch_movie_details(row.movie_id)
        results.append({
            "title": row.title,
            "poster": poster,
            "rating": rating,
            "overview": overview,
            "genres": genres,
            "release": release,
            "score": round(distances[i[0]] * 100, 1)
        })
    return results

# Header 
st.title("🎬 Movie Recommender System")
st.caption("Select a movie and discover similar ones you'll love")
st.divider()

# Selected Movie Info 
col_select, col_info = st.columns([1, 2])

with col_select:
    selected_movie_name = st.selectbox("🎥 Select a Movie:", movies_list)
    recommend_btn = st.button("🔍 Recommend", use_container_width=True)

with col_info:
    selected_id = movies_df[movies_df['title'] == selected_movie_name].iloc[0].movie_id
    poster, rating, overview, genres, release = fetch_movie_details(selected_id)

    info_col1, info_col2 = st.columns([1, 2])
    with info_col1:
        st.image(poster, width=150)
    with info_col2:
        st.subheader(f"{selected_movie_name} ({release})")
        st.metric(label="TMDB Rating", value=f"⭐ {rating}/10")
        st.caption(f"🎭 Genres: {genres}")
        st.info(str(overview[:200]) + "...")

# Recommendations 
if recommend_btn:
    st.divider()
    st.subheader("🍿 Recommended Movies")

    with st.spinner("Finding movies you might like..."):
        results = recommend(selected_movie_name)

    cols = st.columns(5)
    for col, movie in zip(cols, results):
        with col:
            st.image(movie['poster'], use_container_width=True)
            st.markdown(f"<div class='movie-title'>{movie['title']} ({movie['release']})</div>", unsafe_allow_html=True)
            st.metric(label="Rating", value=f"⭐ {movie['rating']}", delta=f"Match {movie['score']}%", delta_color="off")
            with st.expander("📖 Overview"):
                st.write(movie['overview'])
                st.caption(f"🎭 {movie['genres']}")
