import spacy
nlp = spacy.load('en_core_web_md')

# apply the pipeline to the sample sentence
doc = nlp(u'I want to place an order for a pizza.')
# doc = nlp(u'I want a pizza and cola.')
# doc = nlp(u'I would like a pizza.')
# extract the direct object and its transitive verb
dobj = ''
tverb = ''
for token in doc:
    if token.dep_ == 'dobj':
        dobj = token
        tverb = token.head

# extract the verb fro the intents definition
intentVerb = ''
verbList = ['want', 'like', 'need', 'order']
if tverb.text in verbList:
    intentVerb = tverb
else:
    if tverb.head.dep_ == 'ROOT':
        intentVerb = tverb.head

# extract the object for the intents definition
intentObj = ''
objList = ['pizza', 'cola']
if dobj.text in objList:
    intentObj = dobj
else:
    for child in dobj.children:
        if child.dep_ == 'prep':
            intentObj = list(child.children)[0]
            break
        elif child.dep_ == 'compound':
            intentObj = child
            break
# print the intent expressed in the sample sentence
print(intentVerb.text + intentObj.text.capitalize())
