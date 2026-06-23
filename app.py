from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pickle
import os

app = Flask(__name__)

# Load saved files
with open("new_movies.pkl", "rb") as f:
    new_df = pickle.load(f)

with open("movie_embeddings.pkl", "rb") as f:
    movie_embeddings = pickle.load(f)

# Lazy loading
model = None

def get_model():
    global model

    if model is None:
        print("Loading SentenceTransformer model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")

    return model


def recommend(query, top_n=10):
    model = get_model()

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    similarity = cosine_similarity(
        query_embedding,
        movie_embeddings
    )[0]

    movie_indices = similarity.argsort()[::-1][:top_n]

    recommendations = []

    for idx in movie_indices:
        cast_list = new_df.iloc[idx]["cast"]

        cast_str = (
            ", ".join(c.title() for c in cast_list)
            if isinstance(cast_list, list)
            else cast_list
        )

        recommendations.append({
            "title": new_df.iloc[idx]["title_y"],
            "score": round(float(similarity[idx]), 3),
            "cast": cast_str,
            "director": new_df.iloc[idx]["crew"],
            "poster_url": new_df.iloc[idx]["poster_path"]
        })

    return recommendations


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            recommendations = recommend(query)

    return render_template(
        "index.html",
        recommendations=recommendations
    )


if __name__ == "__main__":
    # Get port from environment variable, default to 5000 if running locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)