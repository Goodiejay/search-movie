
import requests 
import json
from genre import get_genres
from genre import get_genre_id
apikey="45c9d50a02e5926e64e182ca5dedd828"


movie_details = {}


def search_movie(  params: dict, url : str, ) -> None:
    try:
        print(params)
        response=requests.get(url, params=params )
        if response.status_code != 200:
            print(f"Error: {response.status_code}: {response.reason}: {response.text}")
            return
        movies=response.json()
        for index, movie in enumerate(movies["results"][:10], start= 1): # filter the search so it returnes only 10 movies
            movie_details[index] = movie
        if movie_details == { }:
            print("No movie found")
                
    
    
    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except Exception as error:
        print(f"Error:  {error}")
    


    


def display_movie()-> None:
    print("="*40)
    print("Movie Viewer".center(40))
    print("="*40)
    for index in movie_details: # filter the search so it returnes only 5 movies
        print(f"{index}: Movie Title:  {movie_details[index]["title"]}")
        print(f"Rating:  {round(movie_details[index]["vote_average"],1)}/10")
    print("_"*40)
    while True:
        try:
            id=int(input("Enter the movie id to view details of movie: "))
            if not id:
                print("please input something")
                continue
            break
        except ValueError:
            print("Enter the movie id Please!")
            continue
    
    for index,movie in movie_details.items():# movie_details is a list in contains each movie
        genre_names=get_genres(ids=movie["genre_ids"])
        if id == index:
              print(f"\n{index}: Movie Title:  {movie_details[index]["original_title"]}")
              print(f"Genre:  {",".join(genre_names)}")
              print(f"Rating:  {round(movie["vote_average"],1)}/10")
              print(f"Year:  {movie["release_date"][:4]}")
              print(f"Langauge:  {movie_details[index]["original_language"]}")
              print("="*40)
              print(f"Plot: \n{movie["overview"]}")
        else:
            pass
     



      
def main():
    while True:
      
        user_choice=menu()
        if user_choice == "1":
            params={
            "api_key": apikey,
            "query": "",
            "include_video": True,
            "language": "en-US",
            "sort_by": "vote_average.desc",
            "vote_count.gte": 1000,
            "vote_average.gte": 7.5
              }
            url="https://api.themoviedb.org/3/search/movie?"
            while True:
                name=input("Enter movie name: ").lower().strip()
                if not name:
                    print("Please enter a movie name")
                    continue
                break
            params["query"]=name
            search_movie(params, url)
            display_movie()
        elif user_choice == "2":
            params={
            "api_key": apikey,
            "with_genres": "",
            "include_video": True,
            "language": "en-US",
            "sort_by": "vote_average.desc",
            "vote_count.gte": 1000,
            "vote_average.gte": 7.5

        }
            urll="https://api.themoviedb.org/3/discover/movie?"
            search=input("Enter genre: ").lower().strip().title()
            search=search.split(" ")
            genre_id = get_genre_id(search)
            genre_id = ",".join(genre_id)
            params["with_genres"] = genre_id
            discover_movies(params, urll)
        elif user_choice == "3":
            print("Bye...")
            exit()
        else:
            print("Enter Num(1-3)")

        
            
        
        

        

def menu()-> str:
    print("="*40)
    print("Movie Viewer".center(40))
    print("="*40)
    menu=input("1. Search by movie name\n2. Search by genre (e.g. Action, Comedy, Drama, Horror, Romance, Thriller etc...)\n3. Exit\n?: ")
    return menu
    
    
    
# if __name__ == "__main__":
#     main()

# def show_genre():






def discover_movies(params: dict, url: str):

    search_movie( params=params, url=url)
    for index, movie in movie_details.items():
        genre_names=get_genres(ids=movie["genre_ids"])
        print("-"*40)
        print(f"#{index+1}. {movie["title"]}     {movie["release_date"]}")
        print(f"Genre:  {",".join(genre_names)}Language:  {movie["original_language"]}")
        print(f"Rating:  {round(movie.get("vote_average", 0.0),1)}/10")
        print(f"Plot:  {movie["overview"]}")
        

if __name__ == "__main__":
    main()

    
    


