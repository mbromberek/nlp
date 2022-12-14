import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp(u'find a high paying job with no experience')
heads = []
for token in doc:
    heads.append(token.head.i)
print(heads)