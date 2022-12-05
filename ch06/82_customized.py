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

'''
list that includes all the possible plural personal pronouns. 
Next, we define a loop that iterates over the tokens in the submitted 
    sentence, looking for a direct object that is a personal pronoun. 
If we find such a token, we check whether its in the list of plural personal pronouns. 
If so, the function returns plural. 
Otherwise, it returns singular. 
If the function either failed to detect a direct object or found one that isnt 
    a personal pronoun, it returns Not found 
'''
def pron_pattern(doc):
    plural = ['we', 'us', 'they', 'them']
    for token in doc:
        if token.dep_ == 'dobj' and token.tag_ == 'PRP':
            if token.text in plural:
                return 'plural'
            else:
                return 'singular'
    return 'not found'

doc = nlp(u'We can overtake them.')
# doc = nlp(u'I might send them a card as a reminder.')
if dep_pattern(doc) and pos_pattern(doc):
    print('Found: ', 'the pronoun in position of direct object is', pron_pattern(doc))
else:
    print('Not Found')

