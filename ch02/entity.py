import spacy
from spacy.attrs import ORTH
nlp = spacy.load('en_core_web_sm')

# txt = u'I have flown to LA. Now I am flying to Frisco.'
txt = u'I have flown to LA. Now I am flying to Chicago.'.replace(u'Frisco',u'San Francisco')

special_case = [{ORTH: 'San Francisco'}]
nlp.tokenizer.add_special_case('San Francisco', special_case)
doc = nlp(txt)

for token in doc:
    if token.ent_type != 0: 
        print(token.text, token.ent_type_)
