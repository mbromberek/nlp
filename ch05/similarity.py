import spacy
nlp = spacy.load('en_core_web_md')

doc = nlp('I want a green apple.')
print(doc.similarity(doc[2:5]))

doc2 = nlp('I like red oranges.')
print(doc2.similarity(doc[2:5]))

print('\n')
token = doc2[3:4][0]
print(token)
print(token.similarity(doc[4:5]))

