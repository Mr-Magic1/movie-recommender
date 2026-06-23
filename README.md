# 🎬 Semantic Movie Recommender System

A context-aware movie recommendation web application built with **Flask**, **PyTorch**, and **Sentence-Transformers**. Unlike traditional keyword-based recommendation systems, this application uses **Semantic Search** to understand the meaning behind natural language queries.

For example, searching for:

> "a science fiction robotic war movie"

can accurately return movies like **The Terminator**, **Automata**, or similar films, even when those exact words are not present in the movie title.

---

## 🚀 Live Demo

Try the application live:

🌐 **Live Demo:** https://kailash191-movie-recommender.hf.space

Search movies using natural language queries such as:

- "robot war in the future"
- "romantic movie with sad ending"
- "space exploration adventure"
- "psychological thriller with twists"

and receive semantically relevant movie recommendations instantly.

---

## ✨ Features

### 🧠 Semantic Understanding

Powered by the **all-MiniLM-L6-v2** transformer model to convert movie descriptions and user queries into high-dimensional embeddings.

### ⚡ Real-Time Recommendations

Uses **Cosine Similarity** to instantly match user queries against precomputed movie embeddings.

### 🎯 Natural Language Search

Search using complete sentences instead of exact movie titles.

Examples:

* "romantic movie with sad ending"
* "space adventure with aliens"
* "mind bending psychological thriller"

### 🚀 Production Ready

Configured with **Gunicorn** and Docker for scalable deployment.

### 🎨 Clean User Interface

Displays:

* Movie Title
* Similarity Score
* Director
* Top Cast Members
* Overview

---

## 🛠️ Tech Stack

### Backend

* Flask
* Gunicorn

### Machine Learning

* Sentence-Transformers
* PyTorch
* Scikit-Learn

### Data Processing

* Pandas
* NumPy

### Deployment

* Docker
* Hugging Face Spaces

---

## 📂 Project Directory Structure

```text
├── .github/                     # GitHub workflows
├── models/                      # Local transformer model cache (ignored by Git)
├── static/                      # CSS, JavaScript and assets
├── templates/
│   └── index.html               # Frontend UI
├── .gitignore
├── app.py                       # Flask application
├── Dockerfile                   # Hugging Face Docker configuration
├── movie_embeddings.pkl         # Precomputed semantic embeddings
├── new_movies.pkl               # Movie metadata dataset
├── README.md
├── requirements.txt
├── runtime.txt
├── trial.ipynb                  # Development notebook
└── Untitled.ipynb               # Experimental notebook
```

---

## ⚙️ Local Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv movie_env
```

#### Windows

```bash
movie_env\Scripts\activate
```

#### macOS/Linux

```bash
source movie_env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🔍 How It Works

### Step 1: Movie Embeddings

Movie metadata including:

* Genres
* Keywords
* Cast
* Director
* Overview

is combined into a single text representation.

### Step 2: Semantic Encoding

The **all-MiniLM-L6-v2** transformer model converts every movie into a dense vector embedding.

### Step 3: Query Encoding

When a user enters a search query, it is encoded into the same vector space.

### Step 4: Similarity Search

Cosine similarity is calculated between the query embedding and all movie embeddings.

### Step 5: Recommendation Ranking

Movies are ranked based on similarity scores and the top matches are returned.

---

## 🐳 Dockerization & Deployment

### Build Docker Image

```bash
docker build -t movie-recommender .
```

### Run Docker Container

```bash
docker run -p 7860:7860 movie-recommender
```

Access the application:

```text
http://localhost:7860
```

---

## 🤗 Deploying to Hugging Face Spaces

### Create a Docker Space

1. Go to Hugging Face Spaces.
2. Click **Create New Space**.
3. Select **Docker** as the SDK.

### Push Your Project

```bash
git add .
git commit -m "Initial deployment"
git push origin main
```

Hugging Face automatically:

* Builds the Docker image
* Installs dependencies
* Starts Gunicorn
* Serves your Flask application

---

## 📊 Example Queries

Try searching:

```text
space exploration movie
```

```text
robot uprising science fiction
```

```text
romantic comedy set in europe
```

```text
crime thriller with detective
```

```text
post apocalyptic survival story
```

---

## 🔮 Future Improvements

* Movie posters integration
* TMDB API support
* Genre filtering
* User ratings
* Hybrid recommendation engine
* Faster vector search using FAISS
* Personalized recommendations

---

## 👨‍💻 Author

**Kailash Vishwakarma**

Built using Flask, PyTorch, Sentence-Transformers, and Hugging Face Spaces.
