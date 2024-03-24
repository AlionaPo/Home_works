# Net in the Web: The API High-Wire Act

#Create a program that allows you to search for images in gif format. 
# The program should allow you to enter a search word. 
# Using this word, search for GIFs using the Giphy API. 
# As a result, print the links to the GIFs.
# Optional: Add the Telegram bot to the previous exercise. 
# Ask the user to enter a search word in the Telegram interface and get a gif image as a result.

# Homework should be submitted via GitHub



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