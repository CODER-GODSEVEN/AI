import random
import json

with open('intents.json', 'r', encoding='UTF8')as f:
    data = json.load(f)

def del_stopwords(txt):
    stopwords = ['?', '!', '.', ',', ' ']

    for word in stopwords:
        if word in txt:
            txt = txt.split(word)
            txt = "".join(txt)

    return txt

while True:
    txt = input('USER ) ')
    txt = del_stopwords(txt)

    if txt == 'exit()':
        break

    for d in data:
        respone_list = {} 

        intents = data['intents']
        for intent in intents:

            w = 0 


            tag = intent['tag'] 
            patterns = intent['patterns'] 

            for pattern in patterns:
                for letter in txt:
                    for p in pattern:
                        if letter == p:
                            w += 1/len(txt)

            if w > 0:                 
                print(f'[{w}]\t{tag}')
            respone_list[tag] = w 


        
            
    respone_list = sorted(respone_list.items(), key=lambda x: x[1], reverse=True)[0]

    tag = respone_list[0]
    w = respone_list[1]
    print(f'\n{w}')
    print(f'{tag}\n')
   
    if w == 0: 
        print('TagError')

    else: 
        for intent in data['intents']:
            if intent['tag'] == tag:
                respones = intent['responses'] 

                x = random.randint(0, len(respones)-1)

                respone = respones[x]

                print(f'BOT ) {respone}')
