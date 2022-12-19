import spacy
nlp = spacy.load('en_core_web_md')

# doc = nlp(u"Do you know what an elephant eats?")
doc = nlp(u'Tell me how a female cheetah hunts')
doc = nlp(u'Do you know how many eggs a sea turtle lays?')
print(doc.text)
for t in reversed(doc):
    print(t.text, t.dep_, t.pos_)
    if t.dep_ == 'nsubj' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
    # if t.dep_ == 'ccomp' and (t.pos_ == 'NOUN' or t.pos_ == 'PROPN'):
        # phrase = (' '.join([child.text for child in t.lefts]) + ' ' + t.text).lstrip()
        phrase_lst = []
        for child in t.lefts:
            if child.dep_ in ['amod','compound']:
                phrase_lst.append(child.text)
        phrase = (' '.join(phrase_lst) + ' ' + t.text).lstrip()
        # phrase = phrase + ' ' + t.head.text
        break
print(phrase)

