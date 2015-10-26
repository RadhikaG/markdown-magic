import requests, json
import time
from .error_urls import meme_not_supported, couldnt_create_meme, too_many_lines, too_few_lines
from requests.exceptions import ConnectionError

meme_id_dict = [
    ['one does not simply','lord of the rings boromir', 61579],
    ['i don\'t always when i do','the most interesting man in the world', 61532],
    ['aliens','ancient aliens history channel guy', 101470],
    ['grumpy cat','grumpy cat', 405658],
    ['everywhere','buzz lightyear and woody from toy story', 347390],
    ['not sure if','futurama fry', 61520],
    ['y u no do dis', 'y u no guy', 61527],
    ['brace yourself yourselves','ned stark from game of thrones', 61546],
    ['all the','X all the Y', 61533],
    ['that would be that\'d be great', 'bill lumburgh from office space', 563423],
    ['too damn', 'the rent is too damn high', 61580],
    ['am i the only one around here','the big lebowski', 259680],
    ['what if i told you','matrix morpheus', 100947],
    ['ain\'t nobody got time for that','', 442575],
    ['nobody bats an eye everyone loses their minds','heath ledger joker', 1760995],
]


def genMeme(template_id, text0, text1):
    '''
    This function returns the url of the meme with the given
    template, upper text, and lower text using the ImgFlip
    meme generation API. Thanks!

    Returns None if it is unable to generate the meme.
    '''

    username = 'blag'
    password = 'blag'

    api_url = 'https://api.imgflip.com/caption_image'

    payload = {
        'template_id': template_id,
        'username': username,
        'password': password,
        'text0': text0,
    }
    # Add bottom text if provided
    if text1 != '':
        payload['text1'] = text1

    try:
        r = requests.get(api_url, params=payload)
    except ConnectionError:
        time.sleep(1)
        r = requests.get(api_url, params=payload)

    # print(parsed_json)
    parsed_json = json.loads(r.text)

    request_status = parsed_json['success']

    if request_status != True:
        error_msg = parsed_json['error_message']
        print(error_msg)
        return None

    else:
        imgURL = parsed_json['data']['url']
        # print(imgURL)
        return imgURL


def findMeme(inptStr):
    '''
    inptStr may be a string of the following forms:
    * 'text0 | text1'
    * 'text0'

    Returns None if it can't find find a meme from the list given above
    '''

    global meme_id_dict

    testStr = inptStr
    testStr.lower()

    template_id = 0

    '''
    meme_id_dict[i] is of form:
    [meme_tagline, meme_name, template_id]
    '''
    for i in range(len(meme_id_dict)):
        test_words = testStr.strip('|.,?!').split(' ')

        meme_words = meme_id_dict[i][0].split(' ')
        common_words = len(list(set(meme_words).intersection(test_words)))

        if (len(meme_words) >= 4 and common_words >= 3) or (len(meme_words) < 4 and common_words >= 1):
            template_id = meme_id_dict[i][2]
            return template_id

    if template_id == 0:
        return None


def processMeme(imgParams):
    '''
    Wrapper function for genMeme() and findMeme()
    imgParams may be a string of the following forms:
    * 'text0 | text1'
    * 'text0'
    * ' | text1'

    Fails gracefully when it can't find or generate a meme
    by returning an appropriate image url with the failure
    message on it.
    '''

    template_id = findMeme(imgParams)

    if template_id is None:
        print("Couldn't find a suitable match for meme :(")
        return meme_not_supported

    # if template_id exists
    imgParams = imgParams.split('|')

    if len(imgParams) == 2 or len(imgParams) == 1:
        text0 = imgParams[0]

        if len(imgParams) == 2:
            text1 = imgParams[1]    # Bottom text text1 exists
        elif len(imgParams) == 1:
            text1 = ''              # No bottom text

        imgURL = genMeme(template_id, text0, text1)

        if imgURL is None:          # Couldn't generate meme
            print("Couldn't generate meme :(")
            return couldnt_create_meme
        else:                       # Success!
            # print(imgURL)
            return imgURL

    elif len(imgParams) > 2:
        print("Too many lines of captions! Cannot create meme.")
        return too_many_lines

    elif len(imgParams) < 1:        # No top text text0 exists
        print("Too few lines of captions! Cannot create meme.")
        return too_few_lines
