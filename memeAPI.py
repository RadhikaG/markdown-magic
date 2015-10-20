import requests, json

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
    '''

    username = 'blag'
    password = 'blag'

    if template_id == '':
        return None

    if text1 != '':
        payload = {
            'template_id': template_id,
            'username': username,
            'password': password,
            'text0': text0,
            'text1': text1,
        }

    elif text1 == '':
        payload = {
            'template_id': template_id,
            'username': username,
            'password': password,
            'text0': text0,
        }

    api_url = 'https://api.imgflip.com/caption_image'
    r = requests.get(api_url, params=payload)
    # print(parsed_json)
    parsed_json = json.loads(r.text)

    request_status = parsed_json['success']

    if request_status != True:
        error_msg = parsed_json['error_message']
        print(error_msg)
        return -1

    else:
        imgURL = parsed_json['data']['url']
        # print(imgURL)
        return imgURL


def processMeme(inptStr):
    '''
    inptStr may be a string of the following forms:
    * 'text0 | text1'
    * 'text0'
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
        print("Couldn't find a suitable match for meme :(")
        return None

