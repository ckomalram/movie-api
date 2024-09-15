from fastapi import FastAPI

app = FastAPI()
# app.title ='Mi primera app con fast api'
# app.version ='1.0.0'

# @app.get('/', tags=['home'])
# def message():
#     return "Hello Carlyle komalram asdas"

# properties
_movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	},
    {
		"id": 2,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]

# movies methods
@app.get('/movies', tags=['movies'])
def get_movies():
    return _movies

@app.get('/movies/{id}', tags=['movies'])
def get_movies_by_id(id: int):
    movie = [movie for movie in _movies if movie['id'] == id]
    if not movie:
        return []    
    return movie

# fastapi automatically put parameters as queryparams when endpoint ends with /
@app.get('/movies/', tags=['movies'])
def get_movies_with_query(category: str):
    movies = [movie for movie in _movies if movie['category'] == category]
    if not movies:
        return []    
    return movies