import spacy
nlp = spacy.load('en_core_web_md')

'''
Iterate over the Doc objects tokensv, searching for a “subject + auxiliary + verb” pattern. 
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

'''
checks whether a certain part of a sentence matches a certain part-of-speech tag. 
When the function detects a mismatch, it returns False
'''
def pos_pattern(doc):
    for token in doc:
        if token.dep_ == 'nsubj' and token.tag_ != 'PRP':
            return False
        if token.dep_ == 'aux' and token.tag_ != 'MD':
            return False
        if token.dep_ == 'ROOT' and token.tag_ != 'VB':
            return False
        if token.dep_ == 'dobj' and token.tag_ != 'PRP':
            return False
    return True

# Testing code
# doc = nlp(u'We can overtake them.')
doc = nlp(u'I might send them a card as a reminder.')
if dep_pattern(doc) and pos_pattern(doc):
    print('Found')
else:
    print('Not Found')

