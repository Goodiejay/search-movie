
import requests 
import json
from genre import get_genres
apikey="api_key=45c9d50a02e5926e64e182ca5dedd828"
# genres=[] # use it when i  wanna add discover movie feature
search_movie="/search/movie?"
# discover_movie="/discover/movie?"
m="&query="
url="https://api.themoviedb.org/3/search/movie?"
filter="&include_video=true&language=en-US&sort_by=vote_average.desc"
user_input=""

movie_details = {

}

def search_movie_by_name(url: str, apikey: str, user_input: str, filter: str):
    try:
        response=requests.get(url+apikey+m+user_input+filter)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return
        movies=response.json()
        for index, movie in enumerate(movies["results"][:5]): # filter the search so it returnes only 5 movies
            movie_details[index] = movie
            if movie_details == {}:
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
        print(f"{index+1}: Movie Title:  {movie_details[index]["title"]}")
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
    id-=1
    
    for index,movie in movie_details.items():# movie_details is a list in contains each movie
        genre_names=get_genres(ids=movie["genre_ids"])
        if id == index:
              print(f"{index+1}: Movie Title:  {movie_details[index]["original_title"]}")
              print(f"Genre:  {",".join(genre_names)}")
              print(f"Rating:  {round(movie["vote_average"],1)}/10")
              print(f"Year:  {movie["release_date"][:4]}")
              print(f"Langauge:  {movie_details[index]["original_language"]}")
              print("="*40)
              print(f"Overview: \n{movie["overview"]}")
        else:
            pass
       
    


      
def main():
    while True:
        name=input("Enter movie name: ").lower().strip()
        if not name:
            print("Please enter a movie name")
            continue
        break
    search_movie_by_name(url, apikey, name, filter=filter)
    display_movie()


    
    
if __name__ == "__main__":
    main()

# def show_genre():
