from memeAPI import processMeme, genMeme

def processString(inptStr):
    ''' 
    inptStr may be a string of the following forms:
    * 'meme: text0 | text1'
    * 'xkcd: search_keywords'
    * 'gif: search_keywords'

    If not, it returns an appropriate error message,
    stating an improperly formatted <magic> tag.
    '''
    imgParamList = inptStr.split(':')

    if len(imgParamList) < 2:
        print("Not enough information for searching for image.")
        return -1

    else:

        imgType = imgParamList[0]
        imgParams = imgParamList[1]
        
        if imgType == 'meme':
            template_id = processMeme(imgParams)

            if template_id is None:
                return -1

            # if template_id exists
            imgParams = imgParams.split('|')

            if len(imgParams) == 2 or len(imgParams) == 1:
                text0 = imgParams[0]
                if len(imgParams) == 2:
                    text1 = imgParams[1]
                elif len(imgParams) == 1:
                    text1 = ''
                imgURL = genMeme(template_id, text0, text1)
                print(imgURL)
                return imgURL

            elif len(imgParams) > 2:
                print("Too many lines of captions! Cannot create meme.")
                return -1

            elif len(imgParams) < 1:
                print("Too few lines of captions! Cannot create meme.")
                return -1

        elif imgType == 'xkcd':
            pass
        elif imgType == 'gif':
            pass

        else:
            print("Improperly formatted <magic> tag.")
            return -1
        

# genImg(61579,'blah', 'blah')
# processString('meme: rains | y u no happen during summers')
