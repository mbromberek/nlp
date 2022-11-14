import spacy

# From what I can tell the logic in the book is no longer possible. 
# Instead I used string replace to change Frisco to San Francisco and 
#  then used special_case to keep San Francisco as one word instead of two. 

from spacy.symbols import ORTH, NORM
# from spacy.attrs import ORTH
nlp = spacy.load("en_core_web_sm")
txt = u'I don\'t fly to Frisco'.replace(u'Frisco',u'San Francisco')
# txt = u'I am flying to Frisco'
# doc = nlp(u'I am flying to Frisco')
doc = nlp(txt)
print([w.text for w in doc])
# Output: ['I', 'do', "n't", 'fly', 'to', 'San', 'Francisco']
# special_case = [{ORTH: u'Frisco', NORM: u'San Francisco'}]
special_case = [{ORTH: 'San Francisco'}]
nlp.tokenizer.add_special_case('San Francisco', special_case)
print([w.lemma_ for w in nlp(txt)])
# Output: ['I', 'do', 'not', 'fly', 'to', 'san francisco']

'''
import spacy
from spacy.symbols import ORTH, NORM
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I am flying to Frisco')
print([w.text for w in doc])
special_case = [{ORTH: u'Frisco', NORM: u'San Francisco'}]
nlp.tokenizer.add_special_case(u'Frisco', special_case)
print([w.lemma_ for w in nlp(u'I am flying to Frisco')])
'''
