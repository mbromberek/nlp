import spacy
nlp = spacy.load('en_core_web_md')

# doc = nlp(u'show me the best hotel in berlin')
doc = nlp(u'I want a pizza and cola.')
# extract the direct object and the conjunct associated with it
for token in doc:
    # print (token.text, token.dep_)
    if token.dep_ == 'dobj':
        dobj = [token.text]
        conj = [t.text for t in token.conjuncts]
        # conj = [t.text for t in token.children if t.dep_ == 'conj']
        verb = token.head.text
        # print(token.head.text + token.text.capitalize())
# Compose the list of the extracted elements
dobj_conj = dobj + conj
print()
print(dobj_conj)
print(verb)

