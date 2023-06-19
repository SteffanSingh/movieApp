from istorage import IStorage
import json
import requests

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """function to get the list of  all the movies """
        try:
            with open("../project2/data.json", "r") as f:
                data = json.load(f)
        except Exception as e:
            print(f"The error is :{e}, Please check your internet connection and try again. ")
        return data

    def add_movie(self, title, year, rating, poster):
        """function to add a movie in the list"""
        movie_name =title
        image= poster
        Key = "2837c90f"
        Url = f"http://www.omdbapi.com/?apikey={Key}&t={movie_name}"
        res = requests.get(Url)
        data = res.json()
        movies = self.list_movies()
        movie_name_list = []
        for movie in movies.keys():
            movie_name_list.append(movie.lower())
        lower_movie_list = movie_name_list
        try:
            if data['Response'] == "False":
                print(f"The error <{data['Title']}> is not found in the database.")
            else:
                title = data["Title"]
                year = data["Year"]
                rating = data["imdbRating"]
                image = data["Poster"]
                movies = self.list_movies()
                if movie_name.lower() in lower_movie_list:
                    print(f"The movie <{movie_name}> already exists in the file")
                else:
                    new_movie = {"Rating": rating, "year": year, "Poster": image}
                    movies[data['Title']] = new_movie
                    print(f"Movie {data['Title']} is added successfully ")

        except Exception as e:
            print(f"The error is {data['Error']} in database")

        with open(self.file_path, "w") as f:
            f.write(json.dumps(movies))

    def delete_movie(self, title):
        """function to delete the movie"""
        movie_name= title
        movies = self.list_movies()
        if movie_name in list(movies.keys()):
            movies.pop(movie_name)
            print(f"The movie {movie_name} is successfully deleted !")
        else:
            print("oops !! The movie does not exist in the list.")
        with open(self.file_path, "w") as f:
            f.write(json.dumps(movies))

    def update_movie(self, title, notes):
        """ funciton to update the movie´s raiting and notes"""
        movies = self.list_movies()
        movie_name = title
        key_list = list(movies.keys())
        lower_movie_list_name = []
        for movie in list(movies.keys()):
            lower_movie_list_name.append(movie.lower())
        new_movie = " "
        if movie_name.lower() in lower_movie_list_name:
            index = lower_movie_list_name.index(movie_name.lower())
            new_movie = key_list[index]
        if movie_name.lower() in lower_movie_list_name:
            movies[new_movie]["Rating"] = input("Enter a new rating")
            movies[new_movie]["note"] = notes
            print(f"the movie {new_movie} is successfulley updated ")
            print(f"""{new_movie} ({movies[new_movie]['year']}) : new rating-{movies[new_movie]['Rating']}
                           note- {movies[new_movie]['note']}""")
        else:
            print(f"The movie '{movie_name}' does not exist in the list")

        with open(self.file_path, "w") as f:
            f.write(json.dumps(movies))

storage = StorageJson('data.json')
print(storage.list_movies())
storage.add_movie("Dead or alive", 1990, 8.9,"abc....")
print(storage.list_movies())
