'''
Works but feel like I did not do it correctly. 
'''
import spacy
nlp = spacy.load('en_core_web_md')

# doc = nlp(u'The product sales hit a new record in the first quarter, with 18.6 million units sold.')
doc = nlp(u'The company, whose profits reached a record high this year, largely attributed to changes in management, earned a total revenue of $4.26 million.')
phrase = ''
for token in doc:
    if token.pos_ == 'NUM':
        while True:
            print(token.text)
            print([tok.text for tok in token.lefts])
            phrase = phrase + ' ' + token.text
            token = token.head
            print(token.text)
            print([tok.text for tok in token.lefts])
            # print([tok.text for tok in token.rights])
            if token not in list(token.head.lefts):
                phrase = ''.join([tok.text for tok in token.lefts]) + ' ' + token.text
                break
        break
phrase = phrase.strip()
print(phrase)


while True:
    token = doc[token.i].head
    print(token.text, token.pos_, token.dep_, token.head)
    # if token.pos_ != 'ADP':
    phrase = token.text + ' ' + phrase
    if token.dep_ == 'ROOT':
        break
print(phrase.strip())

for tok in token.lefts:
    if tok.dep_ == 'nsubj':
        print(tok.text, tok.dep_)
        phrase   = ' '.join([tok.text for tok in tok.lefts]) + ' ' + tok.text + ' ' + phrase
        break
print(phrase)