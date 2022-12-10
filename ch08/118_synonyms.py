import spacy
nlp = spacy.load('en_core_web_md')

# apply the pipleine to the sample sentence
text = u'I want a dish'
# text = u'I want to place an order for a pizza.'
# doc = nlp(u'I want a pizza and cola.')
# doc = nlp(u'I would like a pizza.')

doc = nlp(text)
# extract the transitive verb and its direct object from the dependency tree
for token in doc:
    # print(token.text, token.dep_)
    if token.dep_ == 'dobj':
        verb = token.head.text
        dobj = token.text
# print(verb + dobj.capitalize())
# print()

# create a list of tuples for possible verb synonyms
verbList = [('order', 'want', 'give','make'), ('show', 'find')]
# find the tuple containing the transitive verb extracted from the sample
verbSyns = [item for item in verbList if verb in item]
# print(verbSyns)

# create a list of tuples for possible direct object synonyms
dobjList = [('pizza','pie','dish'), ('cola','soda')]
# find the tuple containing the direct object extracted from the sample
dobjSyns = [item for item in dobjList if dobj in item]
# print(dobjSyns)

# replace the transitive verb and the direct object with synonyms supported by the application
# and compose the string that represents the intent
intent = verbSyns[0][0] + dobjSyns[0][0].capitalize()
print(intent)
