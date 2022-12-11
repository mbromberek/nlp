import spacy
nlp = spacy.load('en_core_web_md')

text = u'I feel like eating a pie.'
doc = nlp(text)

for token in doc:
    print(token.text, token.dep_)
    if token.dep_ == 'dobj':
        dobj = token
tokens = nlp(u'food')

print(dobj.similarity(tokens[0]))
if dobj.similarity(tokens[0]) > 0.6:
    question = 'Would you like to look at our menu?'

print(question)

'''
shows pie as the dobj but similarity to food is 0.24, so not very similar
'''
