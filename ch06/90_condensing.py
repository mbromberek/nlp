import spacy
nlp = spacy.load('en_core_web_md')

doc = nlp(u'The product sales hit a new record in the first quarter, with 18.6 million units sold.')
phrase = ''
for token in doc:
    if token.pos_ == 'NUM':
        while True:
            phrase = phrase + ' ' + token.text
            token = token.head
            if token not in list(token.head.lefts):
                phrase = phrase + ' ' + token.text
                break
        break
print(phrase.strip())

while True:
    token = doc[token.i].head
    # print(token.text, token.pos_, token.dep_)
    if token.pos_ != 'ADP':
        phrase = token.text + phrase
    if token.dep_ == 'ROOT':
        break

for tok in token.lefts:
    if tok.dep_ == 'nsubj':
        # print(tok.text, tok.dep_)
        phrase   = ' '.join([tok.text for tok in tok.lefts]) + ' ' + tok.text + ' ' + phrase
        break
print(phrase)