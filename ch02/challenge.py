import spacy
from spacy.attrs import ORTH
nlp = spacy.load('en_core_web_sm')

txt = u'I have flown to LA. Now I am flying to Frisco.'.replace(u'Frisco',u'San Francisco')

special_case = [{ORTH: 'San Francisco'}]
nlp.tokenizer.add_special_case('San Francisco', special_case)

doc = nlp(txt)

print(u'\nGet intended action to fly to San Francisco')
intents = []
for sent in doc.sents:
    intent_dict = {}
    # print('sent: ' + str(sent))
    for w in sent:
        # print('w: ' + str(w))
        # Add to dictionary if dependency is ROOT and is a present or future tense verb 
        #  or dependency is pobj
        if (w.dep_ == 'ROOT' and (w.tag_=='VBG' or w.tag_=='VB')) \
            or w.dep_ == 'pobj':
            intent_dict[w.dep_] = w.lemma_
    # print(intent_dict)
    # Check the output contained both the ROOT Verb and pobj
    if u'ROOT' in intent_dict and u'pobj' in intent_dict:
        print([intent_dict[u'ROOT'], intent_dict[u'pobj']])
