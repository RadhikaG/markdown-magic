import requests, json
import string

def genGif(searchStr):
    '''
    This function returns the url of the gif searched for
    with the given search parameters using the Giphy API.
    Thanks!
    '''

    if searchStr is None or searchStr == '':
        print("No parameters specified!")
        return -1
    
    searchStr = searchStr.strip('./?\'!,')
    searchStr = searchStr.replace(' ', '+')

    api_url = 'http://api.giphy.com/v1/gifs/search'
    api_key = 'dc6zaTOxFJmzC'

    payload = {
        'q': searchStr,
        'limit': 1,
        'api_key': api_key,
    }

    r = requests.get(api_url, params=payload)
    parsed_json = json.loads(r.text)
    # print(parsed_json)

    if len(parsed_json['data']) == 0:
        print("Couldn't find appropriate gif! :(")
        return -1

    else:
        imgURL = parsed_json['data'][0]['images']['fixed_height']['url']
        # print(imgURL)
        return imgURL

# genGIF('spongebob squarepants')
