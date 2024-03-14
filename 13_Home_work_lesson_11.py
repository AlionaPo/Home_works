import requests

# search_word = input("What picture to find: ")
# open_url = 'http://api.giphy.com/v1/gifs/search'
# api_key = 'pMNNF0QTsdT0ePZuFoZTxfh4PtNga9yx' #token

search_word = input("What picture to find: ")

def search_gifs(search_word):
    api_key = 'pMNNF0QTsdT0ePZuFoZTxfh4PtNga9yx' #token
    open_url = 'http://api.giphy.com/v1/gifs/search'
    params = {
        'api_key': api_key,
        'q': search_word,
        'limit': 1  # Number of GIFs to retrieve
    }

    try:
        response = requests.get(open_url, params=params)
        data = response.json()
        gif_urls = [gif['url'] for gif in data['data']]
        return gif_urls
    except Exception as e:
        print("Error fetching GIFs:", e)
        return []

def main_func():
    gifs = search_gifs(search_word)
    if gifs:
        print("Here are the GIFs related to your search term:")
        for gif in gifs:
            print(gif)
    else:
        print("No GIFs found for the search term.")

if __name__ == "__main__":
    main_func()