from .memeAPI import processMeme
from .gifAPI import processGif
from .error_urls import not_enough_info, improperly_formatted_tag

def processString(inptStr):
    ''' 
    inptStr may be a string of the following forms:
    * 'meme: text0 | text1'
    * 'gif: search_keywords'

    If not, it returns an appropriate error message,
    stating an improperly formatted <magic> tag.
    
    Fails gracefully when it can't find or generate a meme
    or a gif, by returning an appropriate image url with the
    failure message on it.

    TODO: Find a way to efficiently search for xkcd comics
    '''

    inptStr.strip(' ')
    imgParamList = inptStr.split(':')

    if len(imgParamList) < 2:
        print("Not enough information for searching for image.")
        return not_enough_info

    else:

        imgType = imgParamList[0]
        imgParams = imgParamList[1]
        
        if imgType == 'meme':
            imgURL = processMeme(imgParams)
            # print(imgURL)
            return imgURL

        elif imgType == 'gif':
            gifURL = processGif(imgParams)
            # print(gifURL)
            return gifURL

        else:
            print("Improperly formatted <magic> tag.")
            return improperly_formatted_tag
        

# processString('meme: rains | y u no happen during summers')
# processString('gif: spongebob squarepants')
# processString('meme: blabldhishdf')
