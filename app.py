from os import listdir
from fastapi import FastAPI

app = FastAPI(docs_url=None,redoc_url=None)

@app.get("/")
def home():
    with open('discover.txt') as f:
        discover = f.read()

    with open('newsletter.txt') as f:
        newsletter = f.read()

    for file in listdir('./need_to_do/'):
        with open(f'./need_to_do/{file}') as f:
            if file == 'choose.txt': choose = f.read()
            if file == 'find.txt': find = f.read()
            if file == 'move.txt': move = f.read()

    return {
        'discover': discover,
        'newsletter': newsletter,
        'need_to_do': {
            'choose': choose,
            'find': find,
            'move': move
        },
        'contact_us':{
            'location': 'Jalan Raya Kerobokan 70 Kuta Utara, Kabupaten Badung, Bali, Indonesia',
            'email': 'balihotproperties@gmail.com',
            'phone': '822-3663-8529'
        },
        'social_media': {
            'facebook':'https://www.facebook.com',
            'twitter': 'https://twitter.com/BaliHotProperty',
            'instagram': 'https://www.instagram.com/balihotproperty'
        }
    }
