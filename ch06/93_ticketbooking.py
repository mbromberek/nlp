import spacy
nlp = spacy.load('en_core_web_md')

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

def guess_destination(doc):
    for token in doc:
        if token.ent_type != 0 and token.ent_type_ == 'GPE':
            return token.text
    return 'Failed to determine'

def gen_response(doc):
    dest = det_destination(doc)
    if dest != 'Failed to determine':
        return 'When do you need to be in ' + dest + '?'
    dest = guess_destination(doc)
    if dest != 'Failed to determine':
        return 'You want a ticket to ' + dest + ', right?'
    return 'Are you flying somewhere?'

usr_msg_lst = [u'I am going to the conference in Berlin.', 
    u'I am attending the conference in Berlin.'
    , u'Is it a ticket-booking service?'
]

for msg in usr_msg_lst:
    print('User:     ' + msg)
    print('Response: ' + gen_response(nlp(msg)))
    print()


