from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {"id": 101, "movie_name": "Interstellar", "language": "English", "duration": "2h 49m", "price": 250},
    {"id": 102, "movie_name": "Inception", "language": "English", "duration": "2h 28m", "price": 220}
]
print("🎬 MOVIE BOOKING API SERVER STARTED")

bookings = []

# GET all movies
@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

# GET movie by ID
@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"message": "Movie not found"}), 404

# POST add movie
@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.json
    movies.append(data)
    return jsonify(data), 201

# PUT update movie
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.json
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify(movie), 200
    return jsonify({"message": "Movie not found"}), 404

# DELETE movie
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"message": "Movie not found"}), 404

# POST booking tickets
@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.json
    movie = next((m for m in movies if m["id"] == data["movie_id"]), None)

    if not movie:
        return jsonify({"message": "Movie not found"}), 404

    booking = {
        "booking_id": len(bookings) + 1,
        "movie_id": data["movie_id"],
        "tickets": data["tickets"],
        "total_price": movie["price"] * data["tickets"]
    }
    bookings.append(booking)
    return jsonify(booking), 201


if __name__ == "__main__":
    app.run(debug=True,port=5000)
