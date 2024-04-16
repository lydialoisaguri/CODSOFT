import pandas as pd

# Load the dataset
file_path = '/content/title.basics.tsv'
df = pd.read_csv(file_path, sep='\t', encoding='utf-8')

# Function to recommend movies based on a given movie title
def recommend_similar_movies(movie_title, df):
  # Find movie in the dataset
  movie = df[df['primaryTitle'].str.lower() == movie_title.lower()]
  if movie.empty:
    return "Movie not found in the dataset. Please try another movie."

  # Extract genre and start year of the given movie
  genre = movie['genres'].values[0]
  start_year = movie['startYear'].values[0]

  # Filter movies based on similar genre and start year
  similar_movies = df[(df['genres'].str.contains(genre, case=False)) & (df['startYear'] == start_year)]

  # Sort similar movies by runtime minutes (proxy for popularity)
  recommended_movies = similar_movies.sort_values(by=['runtimeMinutes'], ascending=False)

  return recommended_movies[['primaryTitle', 'startYear', 'genres', 'runtimeMinutes']].head(10)

# Get user input for the movie title
user_movie_title = input("Enter a movie title: ")

# Call the function to recommend similar movies based on used input
recommended_movies = recommend_similar_movies(user_movie_title, df)

# Print the recommended movies
print("Recommended Movies are: ")
print(recommended_movies)
