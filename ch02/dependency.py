import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I have flown to LA. Now I am flying to Frisco.')
for token in doc:
    # print(token.text, token.pos_, token.dep_)
    print(token.head.text, token.dep_, token.text)
    '''
    Output:
    flown nsubj I
    flown aux have
    flown ROOT flown
    flown prep to
    to pobj LA
    flown punct .
    flying advmod Now
    flying nsubj I
    flying aux am
    flying ROOT flying
    flying prep to
    to pobj Frisco
    flying punct .
    '''

print(u'\nLocate words that are assigned to dependency labels')
for sent in doc.sents:
    print([w.text for w in sent if w.dep_ == 'ROOT' or w.dep_ == 'pobj'])
    # Output: ['flown', 'LA']
    #         ['flying', 'Frisco']