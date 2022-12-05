import spacy
nlp = spacy.load('en_core_web_md')

'''
Figures out the destination
'''
def det_destination(doc):
    for i, token in enumerate(doc):
        # Checks if token is a GPE entity
        if token.ent_type != 0 and token.ent_type_ == 'GPE':
            # Loop through head of token, stops once find word "to" or ROOT
            while True:
                token = token.head
                if token.text == 'to':
                    return doc[i].text
                if token.head == token:
                    return 'Failed to determine'
    return 'Failed to determine'

# Testing the det_destination function
doc = nlp(u'I am going to the conference in Berlin.')
dest = det_destination(doc)
print('It seems the user wants a ticket to ' + dest)
