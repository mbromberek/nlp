import spacy
nlp = spacy.load('en_core_web_sm')

# doc = nlp('I want a green apple.')
# print(doc[2:5])

doc = nlp(u'The Golden Gate Bridge is an iconic landmark in San Francisco.')
print ([doc[i] for i in range(len(doc))])

# span.merge is no longer allowed, need to use retokenize
'''
span = doc[1:4]
lem_id = doc.vocab.strings[span.text]
print(span.merge(lemma = lem_id))
'''

with doc.retokenize() as retokenizer:
    retokenizer.merge(doc[1:4])
    retokenizer.merge(doc[9:11])
print ([doc[i] for i in range(len(doc))])

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_)
