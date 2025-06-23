# Song recommendation
def recommend_songs_from_cluster(song_name, df, n_recommendations=5):
    song_name = song_name.strip().lower()
    
    if song_name not in df['name'].values:
        return ["Song not found in the dataset."]
        return

    cluster = df[df['name'] == song_name]['Clusters'].values[0]  # updated column name
    print(f"'{song_name}' belongs to Cluster {cluster}.")

    similar_songs = df[(df['Clusters'] == cluster) & (df['name'] != song_name)]
    recommendations = similar_songs.sample(n=min(n_recommendations, len(similar_songs)))

    return recommendations[['name', 'artists', 'popularity', 'duration_ms']]

# Example call
#recommend_songs_from_cluster("l'oiseau", df_clustered)