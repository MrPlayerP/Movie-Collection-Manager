# Assignment Information
# Author: Pedro Gonzalez San Martin
# Date: 09-26-2026
# Assignment: Programming Assignment - Movie Collection Manager


def create_movie(title, year, genres, rating):
    # Accepts title, year, genres, and rating, and returns a new movie dictionary.
    return {
        "title": title,
        "year": year,
        "genres": genres,
        "rating": rating,
    }


def display_movies(movies, heading):
    # Prints a formatted table of all movies in the collection under the provided heading.
    print(f"\n{heading}")
    print("-" * len(heading))

    if len(movies) == 0:
        print("No movies in this collection.")
        return

    print(f"{'Title':<25} | {'Year':<4} | {'Genres':<25} | {'Rating'}")
    print("-" * 75)

    for movie in movies:
        joined_genres = " / ".join(movie["genres"])
        display_title = movie["title"][:22] + "..." if len(movie["title"]) > 25 else movie["title"]
        print(f"{display_title:<25} | {movie['year']:<4} | {joined_genres:<25} | {movie['rating']:.1f}")


def find_top_rated(movies, n):
    # Returns a new list containing the top n movies sorted by rating in descending order.
    sorted_by_rating = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return sorted_by_rating[:n]


def get_average_rating(movies):
    # Calculates the average rating across all movies using a for loop and accumulator.
    if len(movies) == 0:
        return 0.0

    total_rating = 0.0
    for movie in movies:
        total_rating += movie["rating"]

    average = total_rating / len(movies)
    return round(average, 2)


def main():
    # Define the five-movie starter list
    movies = [
        {"title": "Inception", "year": 2010, "genres": ["Sci-Fi", "Thriller"], "rating": 8.8},
        {"title": "The Shawshank Redemption", "year": 1994, "genres": ["Drama"], "rating": 9.3},
        {"title": "The Godfather", "year": 1972, "genres": ["Crime", "Drama"], "rating": 9.2},
        {"title": "Schindler's List", "year": 1993, "genres": ["Drama", "History"], "rating": 8.9},
        {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"], "rating": 9.0},
    ]

    # Display the collection as loaded
    display_movies(movies, "Your Movie Collection")

    # Ask the user to add two new movies
    print("\nPlease add two new movies to the collection:")
    for i in range(2):
        print(f"\n--- Entering Movie {i + 1} ---")
        title = input("Enter title: ")
        year = int(input("Enter release year: "))

        genres_input = input("Enter genres (separated by commas): ")
        genres = [genre.strip() for genre in genres_input.split(",")]

        rating = float(input("Enter rating: "))

        new_movie = create_movie(title, year, genres, rating)
        movies.append(new_movie)

    # Sort the movies list in-place by year and display
    movies.sort(key=lambda m: m["year"])
    display_movies(movies, "All Movies Sorted by Year")

    # Call find_top_rated() and display the result
    top_movies = find_top_rated(movies, 3)
    display_movies(top_movies, "Top 3 Rated Movies")

    # Call get_average_rating() and print the labeled result
    avg_rating = get_average_rating(movies)
    print(f"\nCollection average rating: {avg_rating}")


if __name__ == "__main__":
    main()