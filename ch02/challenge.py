import spacy
from spacy.attrs import ORTH
nlp = spacy.load('en_core_web_sm')

txt = u'I have flown to LA. Now I am flying to Frisco.'.replace(u'Frisco',u'San Francisco')

special_case = [{ORTH: 'San Francisco'}]
nlp.tokenizer.add_special_case('San Francisco', special_case)
# print([w.lemma_ for w in nlp(txt)])

doc = nlp(txt)
# print([w.lemma_ for w in nlp(txt)])
print(u'\nVerb')
intent_action = [w.text for w in doc if w.tag_=='VBG' or w.tag_=='VB']
print(intent_action)

print(u'\nLocate words that are assigned to dependency labels')
intent_dependencies = []
for sent in doc.sents:
    intent_dependencies.append([w.text for w in sent if w.dep_ == 'ROOT' or w.dep_ == 'pobj'])
print(intent_dependencies)

print(u'\nGet intended action to fly to San Francisco')
for intent in intent_dependencies:
    if intent[0] == intent_action[0]:
        print(intent)

# for token in doc:
#     # left is token and right is lemmas
#     print(token.text, token.lemma_)

# for token in doc:
#     if token.ent_type != 0:
#         print(token.text, token.ent_type_)