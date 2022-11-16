import spacy
# from spacy.attrs import ORTH
nlp = spacy.load('en_core_web_sm')

txt = u'A noun chunk is a phrase that has a noun as its head.'
doc = nlp(txt)

for chunk in doc.noun_chunks:
    print(chunk)

print('\n')
for token in doc:
    if token.pos_ == 'NOUN':
        chunk = ''
        for w in token.children:
            if w.pos_ == 'DET' or w.pos_ == 'ADJ':
                chunk = chunk + w.text + ' '
        chunk = chunk + token.text
        print(chunk)


print('\n')
for token in doc:
    if token.pos_ == 'NOUN':
        chunk = ''
        for w in token.lefts:
            chunk = chunk + w.text + ' '
        chunk = chunk + token.text
        print(chunk)

