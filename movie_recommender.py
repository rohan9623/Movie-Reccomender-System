import math
from collections import Counter
movies = [
    ("Inception", "scifi action thriller"),
    ("Interstellar", "scifi drama adventure"),
    ("Dark Knight", "action crime drama"),
    ("Avengers", "action scifi fantasy"),
    ("Titanic", "romance drama")
]
def tokenize(text):
    return text.lower().split()
vocab = set()
for _, genre in movies:
    vocab.update(tokenize(genre))
vocab = list(vocab)
def vectorize(text):
    words = tokenize(text)
    word_count = Counter(words)
    return [word_count.get(word, 0) for word in vocab]
def cosine_similarity(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a*a for a in v1))
    mag2 = math.sqrt(sum(b*b for b in v2))
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot / (mag1 * mag2)
def recommend_movie(movie_name, top_n=3):
    titles = [m[0] for m in movies]
    if movie_name not in titles:
        return "Movie not found!"
    index = titles.index(movie_name)
    target_vector = vectorize(movies[index][1])
    scores = []
    for i, (_, genre) in enumerate(movies):
        if i != index:
            sim = cosine_similarity(target_vector, vectorize(genre))
            scores.append((titles[i], sim))
        scores.sort(key=lambda x: x[1], reverse=True)
    return [movie for movie, _ in scores[:top_n]]
if __name__ == "__main__":
    movie = input("Enter movie name: ")
    result = recommend_movie(movie)

    print("\nRecommended Movies:")
    if isinstance(result, list):
        for r in result:
            print(r)
    else:
        print(result)
