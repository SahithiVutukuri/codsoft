import pandas as pd

# Sample data (user-item matrix: movies vs user ratings)
data = {
    'Movie1': [5, 4, 0, 2, 1],
    'Movie2': [4, 0, 0, 3, 4],
    'Movie3': [2, 0, 0, 5, 4],
    'Movie4': [1, 1, 5, 4, 0],
    'Movie5': [3, 4, 4, 2, 5]
}

# Create a DataFrame (users are rows, movies are columns)
df = pd.DataFrame(data)

# Print the DataFrame to see the ratings matrix
print(df)




from sklearn.metrics.pairwise import cosine_similarity

# Transpose the DataFrame (movies as rows and users as columns)
movie_ratings_transposed = df.T

# Calculate cosine similarity between movies (columns in the transposed matrix)
cosine_sim = cosine_similarity(movie_ratings_transposed)

# Convert to DataFrame for easier interpretation
cosine_sim_df = pd.DataFrame(cosine_sim, index=df.columns, columns=df.columns)

# Print cosine similarity matrix
print(cosine_sim_df)






def recommend_movies(movie_name, top_n=3):
    # Get similar movies by sorting the similarity values in descending order
    similar_scores = cosine_sim_df[movie_name].sort_values(ascending=False)
    
    # Remove the movie itself from the list (since it’s the most similar to itself)
    similar_scores = similar_scores.drop(movie_name)
    
    # Get the top N similar movies
    return similar_scores.head(top_n)

# Example: Recommend movies similar to 'Movie1'
recommended_movies = recommend_movies('Movie1', top_n=3)
print("Recommended Movies for 'Movie1':")
print(recommended_movies)





liked_movies = ['Movie2', 'Movie3']

# Collect recommendations for each liked movie
all_recommendations = {}
for movie in liked_movies:
    all_recommendations[movie] = recommend_movies(movie, top_n=3)

# Print recommendations for all liked movies
print("All Recommendations:")
for movie, recommendations in all_recommendations.items():
    print(f"Recommendations for {movie}:")
    print(recommendations)
























