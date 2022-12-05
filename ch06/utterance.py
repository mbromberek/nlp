import spacy
nlp = spacy.load('en_core_web_md')

'''
Iterate over the Doc object’s tokensv, searching for a “subject + auxiliary + verb” pattern. 
If we find this pat- tern, we check whether the verb has a direct object among its 
    syntactic childrenx 
Finally, if we find a direct object, the function returns True. 
Otherwise, it returns False
'''
def dep_pattern(doc):
    for i in range(len(doc) -1):
        if doc[i].dep_ == 'nsubj' and doc[i+1].dep_ == 'aux' and doc[i+2].dep_ == 'ROOT':
            for tok in doc[i+2].children:
                if tok.dep_ == 'dobj':
                    return True
    return False

doc = nlp(u'We can overtake them.')
if dep_pattern(doc):
    print('Found')
else:
    print('Not found')
