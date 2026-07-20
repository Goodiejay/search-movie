import json
import requests
import os
genre_main={

}

def get_genres(ids: list, genres = genre_main )-> list:
    name=[]
    if not os.path.exists("genres.py"):
        create_genre_dict()
    with open("genres.json", "r") as f:
        genres=json.load(f)
    for id in ids:
            for genre_id in genres:
                if  str(id) == genre_id:
                    name.append(genres[genre_id])
                else:
                    pass
            # namee=[index["id"] for ids in id ]
    return name
        # print(index[id])
    # for ids in id:
    #     if 


def get_genre_id(names: list | str ) -> int | list:
    ids = []
    with open("genres.json", "r") as f:
        genres=json.load(f)
    for name in  names:
        for genre_id in genres:
            if genres[genre_id] == name:
                ids.append(genre_id)
            else:
                pass
    return ids
        


                



    # for genre in 


    # with open("genre.json", "w") as ge:
    #     json.dump(genres["genres"], ge, indent=4)

def create_genre_dict():
 
    genre1={
        
    }
    try:
        url ="https://api.themoviedb.org/3/genre/movie/list?api_key=45c9d50a02e5926e64e182ca5dedd828&language=en-US"
        response = requests.get(url=url)
        genres=response.json()
    except requests.Exception.ConnectionError:
        print(f"No internet connection")
    except Exception as error:
        print(f"unexpected error occured:  {error}")
        
    for genre in genres["genres"]:
        genre1[genre["id"]]= genre["name"]

    with open("genres.json", "w") as f:
        json.dump(genre1, f, indent=4 )

def main():
    id=[]
    genry=get_genres(id,genre_main)
    print(genry)


if __name__ == "__main__":
    main()
