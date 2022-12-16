import spacy
nlp = spacy.load('en_core_web_md')

usr_intent = ''
usr_data = {}

def intent_ext(update):
    msg = update
    doc = nlp(msg)
    for token in doc:
        # print(token.text, token.dep_, token.pos_, token.tag_)
        if token.dep_ == 'dobj':
            intent = extract_intent(doc)
            # print('extract_intent: ', intent)
            if intent == 'orderPizza':
                usr_data['product'] = 'pizza'
                print('We need some more information to place your order. What type of pizza do you want?')
                return 'ADD_INFO'
            elif intent in ['showPizza','showMenu']:
                print('Would you like to look at your menu?')
                return 'MENU'
            else:
                print('Your intent is not recognized. Please rephrase your request.') 
                return 'ORDERING'
            return
    print('Please rephrase your request. Be as specific as possible!')
    return 'ORDERING'

def add_info(update):
    msg = update
    doc = nlp(msg)
    for token in doc:
        # print(token.text, token.dep_, token.pos_, token.tag_)
        # Book had check for dobj but not sure why that is needed when can 
        #  just check for amod. Which works for 'I want a Greek one.' and 'A Greek one.'
        # if token.dep_ == 'dobj':
        #     dobj = token
        #     for child in dobj.lefts:
        #         if child.dep_ == 'amod' or child.dep_ == 'compound':
        #             usr_data['type'] = child.text
        #             return(place_order(usr_data))
        if token.dep_ == 'amod' or token.dep_ == 'compound':
            amod = token
            usr_data['type'] = amod.text
            return(place_order(usr_data))
    print('Cannot extract necessary info. Please try again.')
    return 'ADD_INFO'

def cancel(update):
    print('Have a nice day!')
    return 'END'

def show_menu(update):
    print('Pizza Menu:')
    pizza_menu_lst = ['Pepperoni', 'Greek', 'Sausage', 'Cheese']
    print('\t' + '\n\t'.join(pizza_menu_lst))
    return 'ORDERING'

def format_order(usr_data):
    ret_lst = []
    if 'product' in usr_data:
        ret_lst.append('\tProduct - ' + usr_data['product'])
    if 'type' in usr_data:
        ret_lst.append('\tType - ' + usr_data['type'])
    return '\n'.join(ret_lst)
    
def place_order(ord_data):
    print('Your order has been placed.')
    print(format_order(ord_data))
    print('Have a nice day!')
    return 'END'


def extract_intent(doc):
    new_token = []
    # extract the transitive verb and its direct object from the dependency tree
    for token in doc:
        # print(token.text, token.dep_, token.pos_, token.tag_)
        if token.dep_ == 'dobj':
            for child in token.children:
                new_token = [obj for obj in child.children if obj.dep_ == 'pobj']
            # print(new_token)
            if (len(new_token)>0):
                verb = token.text
                dobj = new_token[0]
            else:
                verb = token.head.text
                dobj = token
            # print([child for child in token.children])
            break
    # print(verb + dobj.text.capitalize())
    # print()

    # create a list of tuples for possible verb synonyms
    verbList = [('order', 'want', 'give','make', 'eating'), ('show', 'find','see','what')]
    # find the tuple containing the transitive verb extracted from the sample
    verbSyns = [item for item in verbList if verb in item]
    # print(verbSyns)

    # create a list of tuples for possible direct object synonyms
    dobjList = [('pizza','pie','dish'), ('cola','soda'),('menu','choices')]
    # find the tuple containing the direct object extracted from the sample
    dobjSyns = [item for item in dobjList if dobj.text in item]

    # Try using semantic similarity to see if user wants food or drink
    if len(dobjSyns) == 0:
        foodTokens = nlp(u'food')
        drinkTokens = nlp(u'soda')
        # print(dobj.similarity(foodTokens[0]))
        # print(dobj.similarity(drinkTokens[0]))
        if dobj.similarity(foodTokens[0]) > 0.5:
            dobjSyns = [['food']]
        elif dobj.similarity(drinkTokens[0]) > 0.5:
            dobjSyns = [['drink']]

    # print(dobjSyns)

    if len(verbSyns) == 0 or len(dobjSyns) == 0:
        # print('unrecognized')
        return('unrecognized')
    else:
        # replace the transitive verb and the direct object with synonyms supported by the application
        # and compose the string that represents the intent
        intent = verbSyns[0][0] + dobjSyns[0][0].capitalize()
        # print(intent)
        return(intent)


# Replaced by intent_ext
'''
def utterance(update): 
    msg = update
    doc = nlp(msg)
    for token in doc:
        # print(token.text, token.dep_, token.pos_, token.tag_)
        if token.dep_ == 'dobj':
            usr_intent = extract_intent(doc)
            if usr_intent == 'orderPizza':
                print('We need some more information to place your order. What type of pizza do you want?')
            elif usr_intent == 'showPizza':
                print('Would you like to look at your menu?')
            else:
                print('Your request is not recognized')
            return
    print('Please rephrase your request. Be as specific as possible!')
'''

def start():
    print('Hi! This is a pizza ordering app. Do you want to order something?')
    return 'ORDERING'

def main():
    state = ''
    while True:
        # print('State: ', state)
        if state == 'ORDERING':
            input1 = input('Ordering: ')
            state = intent_ext(input1)
        elif state == 'ADD_INFO':
            input1 = input('Getting Order Information: ')
            state = add_info(input1)
        elif state == 'MENU':
            state = show_menu(input1)
        elif state == 'END':
            break
        else:
            state = start()

if __name__ == '__main__':
    main()
