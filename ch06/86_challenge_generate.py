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

'''
Takes two parameters
sents - contains a list of the sentences fromt he beginning fo the discourse 
    up to the sentence that satisfies all the patterns here.
num - number of direct object prounoun in the sentence that satisfies all 
    the patterns. 
'''
def find_noun(sents, num):
    if num == 'plural':
        taglist = ['NNS', 'NNPS']
    if num == 'singular':
        taglist = ['NN', 'NNP']
    for sent in reversed(sents):
        for i, token in enumerate(sent):
            if token.tag_ in taglist:
                if sent[i-1].dep_ == 'det':
                    return sent[i-1].lemma_ + ' ' + token.text
                return token.text
    return 'Noun not found'

'''
Iterate over the tokens in doc looking for a direct object that is a personal
    prounoun. 
Change the original sentence by replacing the personal pronoun with the 
    matching noun and appending "too" to the end of it. 
'''
def gen_utterance(doc, noun):
    print('\n', doc, '\n')
    sent = ''
    for i, token in enumerate(doc):
        if token.dep_ == 'dobj' and token.tag_ == 'PRP':
            sent = doc[:i].text + ' '  + noun + ' ' + doc[i+1:len(doc)-2].text + 'too.'
            return sent
    return 'Failed to generate an utterance'

doc = nlp(u'The symbols are clearly distinguishable. I can recognize them promptly.')
print(doc, '\n')
for token in doc:
    print(token.text, token.lemma_, token.dep_, token.tag_)
print()

sents = list(doc.sents)
response = ''
noun = ''
for i, sent in enumerate(sents):
    if dep_pattern(sent) and pos_pattern(sent):
        noun = find_noun(sents[:i], pron_pattern(sent))
        if noun != 'Noun not found':
            response = gen_utterance(sents[i], noun)
            break
print(response)

