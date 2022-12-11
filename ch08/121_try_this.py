'''
Use recongnizing synonyms to get intent
If that does work for object then 
Use semantic similarity 
'''
import spacy
nlp = spacy.load('en_core_web_md')

# apply the pipleine to the sample sentence
# text = u'I want a dish'
# text = u'I want a pizza and cola.'
# text = u'I would like a pizza.' #Says unrecognized since like is not in the verbList
text = u'I want to place an order for a pizza.'
# text = u'I would like to order a pizza.'
# text = u'I would like to order two pizzas.'
# text = u'I feel like eating a pie.'
text = u'I feel like eating breadsticks.'
# text = u'I want a pepsi.'

doc = nlp(text)
new_token = []
# extract the transitive verb and its direct object from the dependency tree
for token in doc:
    print(token.text, token.dep_, token.pos_, token.tag_)
    if token.dep_ == 'dobj':
        for child in token.children:
            new_token = [obj for obj in child.children if obj.dep_ == 'pobj']
        # print(new_token)
        if (len(new_token)>0):
            verb = token.text
            dobj = new_token[0]
        else:
            verb = token.head.text
            dobj = token
        # print([child for child in token.children])
        break
print(verb + dobj.text.capitalize())
print()

# create a list of tuples for possible verb synonyms
verbList = [('order', 'want', 'give','make', 'eating'), ('show', 'find')]
# find the tuple containing the transitive verb extracted from the sample
verbSyns = [item for item in verbList if verb in item]
# print(verbSyns)

# create a list of tuples for possible direct object synonyms
dobjList = [('pizza','pie','dish'), ('cola','soda')]
# find the tuple containing the direct object extracted from the sample
dobjSyns = [item for item in dobjList if dobj.text in item]

# Try using semantic similarity to see if user wants food or drink
if len(dobjSyns) == 0:
    foodTokens = nlp(u'food')
    drinkTokens = nlp(u'soda')
    # print(dobj.similarity(foodTokens[0]))
    # print(dobj.similarity(drinkTokens[0]))
    if dobj.similarity(foodTokens[0]) > 0.5:
        dobjSyns = [['food']]
    elif dobj.similarity(drinkTokens[0]) > 0.5:
        dobjSyns = [['drink']]

# print(dobjSyns)

if len(verbSyns) == 0 or len(dobjSyns) == 0:
    print('unrecognized')
else:
    # replace the transitive verb and the direct object with synonyms supported by the application
    # and compose the string that represents the intent
    intent = verbSyns[0][0] + dobjSyns[0][0].capitalize()
    print(intent)

