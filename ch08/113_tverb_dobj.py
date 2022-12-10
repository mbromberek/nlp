import spacy
nlp = spacy.load('en_core_web_md')

doc = nlp(u'show me the best hotel in berlin')
for token in doc:
    # print (token.text, token.dep_)
    if token.dep_ == 'dobj':
        print(token.head.text + token.text.capitalize())
