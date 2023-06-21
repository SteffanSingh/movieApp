import sys

from storage_json import StorageJson
from movie_app import MovieApp
from storage_csv import StorageCsv
def main():

    file_path = input("Enter  the storage type :")

    if file_path == 'data.json':
        storage = StorageJson('data.json')
        movie_app = MovieApp(storage)
        movie_app.run()
    elif file_path == "data.csv":
        storage = StorageCsv("data.csv")
        movie_app = MovieApp(storage)
        movie_app.run()
    else:
        print("file path does not exist")
        sys.exit()



if __name__ == "__main__":
    main()

