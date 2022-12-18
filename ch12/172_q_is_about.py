import spacy
nlp = spacy.load('en_core_web_md')

'''
Extract what a question is about
'''

doc = nlp(u"Have you heard of rhinos?")
doc = nlp(u"What can you say about wild mountain goats?")
print(doc.text)
for t in doc:
  if t.dep_ == 'pobj' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
    phrase = (' '.join([child.text for child in t.lefts]) + ' ' + t.text).lstrip()
    break
print(phrase)


doc = nlp(u"Tell me about the color of the sky.")
print(doc.text)
for t in doc:
    if t.dep_ == 'pobj' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
        phrase = (' '.join([child.text for child in t.lefts]) + ' ' + t.text).lstrip()
        if bool([prep for prep in t.rights if prep.dep_ == 'prep']):
            prep = list(t.rights)[0]
            pobj = list(prep.children)[0]
            phrase = phrase + ' ' + prep.text + ' ' + pobj.text
        break
print(phrase)

doc = nlp(u"Do you know what an elephant eats?")
print(doc.text)
for t in reversed(doc):
  if t.dep_ == 'nsubj' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
    phrase = t.text + ' ' + t.head.text
    break
print(phrase)

doc = nlp(u"How to feed a cat?")
print(doc.text)
for t in reversed(doc):
  if t.dep_ == 'dobj' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
    phrase = t.head.lemma_ + 'ing' + ' ' + t.text
    break
print(phrase)
