from flask import Flask, jsonify, request, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Set up Elasticsearch connection
es = Elasticsearch(['http://localhost:9200'])  # Replace with your Elasticsearch host and port

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')

        # Use Elasticsearch to search for movies
        search_body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "genres"]
                }
            }
        }

        response = es.search(index='movies', body=search_body)

        # Extract movie hits from Elasticsearch response
        hits = response.get('hits', {}).get('hits', [])

        # Get information about the matched movie
        if hits:
            matched_movie = hits[0]['_source']

            # Get additional movies based on the matched movie's title or genre
            more_movies_body = {
                "query": {
                    "bool": {
                        "should": [
                            {"match": {"title": matched_movie['title']}},
                            {"match": {"genres": matched_movie.get('genres', '')}}
                        ],
                        "must_not": {"match": {"title": query}}
                    }
                },
                "size": 10
            }

            more_movies_response = es.search(index='movies', body=more_movies_body)
            more_movies = [hit['_source'] for hit in more_movies_response.get('hits', {}).get('hits', [])]

            return render_template('search.html', movie=matched_movie, recommendations=more_movies)

    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
