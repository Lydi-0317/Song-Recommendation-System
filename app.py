from flask import Flask, request, jsonify
from flask_cors import CORS

print("Importing load_data and recommend_songs_from_cluster...")
from recommendation.preprocessing import load_data
from recommendation.model import recommend_songs_from_cluster

print("Creating Flask app...")
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

print("Loading dataset...")
df = load_data()
print("Dataset loaded!")

@app.route('/')
def home():
    return '✅ Flask backend is running!'

# New route to get all song names
@app.route('/get_song_names', methods=['GET'])
def get_song_names():
    song_names = df['name'].tolist()  # Extract song names from the dataframe
    return jsonify(song_names)  # Return song names as a JSON array

@app.route('/recommend', methods=['GET'])
def recommend():
    song = request.args.get('song')
    if not song:
        return jsonify({'error': 'Please provide a song name using ?song='}), 400
    
    results = recommend_songs_from_cluster(song, df)
    
    if hasattr(results, 'to_dict'):
        return jsonify(results.to_dict(orient='records'))
    else:
        return jsonify({'recommendations': results})

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)

