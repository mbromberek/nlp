import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp(u'I am flying to Frisco')
print([w.text for w in doc])

print('\nLemma')
doc = nlp(u'this product integrates both libraries for downloading and applying patches')
for token in doc:
    # left is token and right is lemmas
    print(token.text, token.lemma_)

