import spacy
nlp = spacy.load('en_core_web_sm')

# works with $, £, or €. Would have to be changed if $ comes after amount
doc = nlp(u'The firm earned £1.5 million in 2017, in comparison with $1.2 million in 2016.')
phrase = ''

for token in doc:
    print(token.text, token.pos_, token.tag_, spacy.explain(token.pos_))
print('\n')

phrase_lst = []
# extrace phrase for amount of money
for token in doc:
    if token.tag_ == '$':
        phrase = token.text
        i = token.i+1
        while doc[i].tag_ == 'CD':
            phrase += doc[i].text + ' '
            i+=1
        # break
        phrase_lst.append(phrase[:-1])
# phrase = phrase[:-1]
print(phrase_lst)
