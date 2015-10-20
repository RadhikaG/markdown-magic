import requests, json
import string

def processGif(searchStr):
    '''
    This function returns the url of the gif searched for
    with the given search parameters using the Giphy API.
    Thanks!

    Fails gracefully when it can't find a gif by produing an 
    appropriate image url with the failure message on it.
    '''
    
    # Sanitizing searchStr
    # TODO: Find a better way to do this
    searchStr.replace('| ', ' ')
    searchStr.replace('|', ' ')
    searchStr.replace(', ', ' ')
    searchStr.replace(',', ' ')
    searchStr.rstrip()
    searchStr = searchStr.strip('./?\'!,')
    searchStr = searchStr.replace(' ', '+')

    if searchStr is None or searchStr == '':
        print("No search parameters specified!")
        return -1

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
        print("Couldn't find suitable match for gif! :(")
        return -1

    else:               # Success!
        imgURL = parsed_json['data'][0]['images']['fixed_height']['url']
        # print(imgURL)
        return imgURL
