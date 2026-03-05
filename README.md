# 🎬 Movie Recommender System

A content-based movie recommender system built with Python and Streamlit that suggests similar movies based on genres, keywords, cast, and crew.

---

---

## 📌 Features
- Recommends top 5 similar movies based on selected movie
- Uses content-based filtering (genres, keywords, cast, crew)
- Clean and simple UI built with Streamlit
- Fast recommendations using Cosine Similarity

---

## 🧠 How It Works

```
1. Data is loaded from TMDB 5000 Movie Dataset
2. Features (genres, keywords, cast, crew, overview) are combined into tags
3. Tags are vectorized using CountVectorizer (Bag of Words)
4. Cosine Similarity is calculated between all movies
5. Top 5 most similar movies are recommended
```

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| Scikit-learn | CountVectorizer & Cosine Similarity |
| NLTK | Stemming |
| Streamlit | Web app interface |
| Pickle | Model serialization |

---

## 📂 Project Structure

```
movie-recommender-system/
│
├── DATASETS/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│   └── movies-recom-sys.ipynb
│
├── app.py                  ← Streamlit web app
├── main.py                 ← Core ML pipeline
├── requirements.txt        ← Dependencies
├── setup.sh                ← Streamlit config
├── Procfile                ← Deployment config
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Akmal-2253/movie-recommender-system.git
cd movie-recommender-system
```

### 2. Create Virtual Environment
```bash
python -m venv myenv
myenv\Scripts\activate        # Windows
source myenv/bin/activate     # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

### 5. Open in Browser
```
http://localhost:8501
```

---

## 📊 Dataset
- **Source:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Movies:** 4806 movies
- **Features used:** genres, keywords, cast, crew, overview

---

## 🔍 ML Concepts Used

### Bag of Words (BOW)
Converts text tags into numerical vectors by counting word frequencies.

### Cosine Similarity
Measures similarity between two movies by calculating the angle between their vectors. Score closer to 1.0 means more similar.

### Stemming
Reduces words to their root form (e.g. "action", "actions" → "action") to improve matching accuracy.

---

## 📦 Dependencies
```
streamlit
pandas
numpy
scikit-learn
nltk
```

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

---

## 📝 License
This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author
**Akmal**
- GitHub: [@Akmal-2253](https://github.com/Akmal-2253)

---

