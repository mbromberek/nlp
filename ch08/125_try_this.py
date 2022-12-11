import spacy
nlp = spacy.load('en_core_web_md')

# text = u'I have finished my pizza. I want another one.'
text = u'I have finished my pizza. It was delicious. I want another one.'
doc = nlp(text)

verbList = [('order','want','give','make'),('show','find')]
dobjList = [('pizza','pie','pizzaz'),('cola','soda')]

#Unlike the transitive verb and direct object lists, the substitute 
# list has a simple structure, because we don’t need to group substitutes. 
# The same sub- stitute could refer to any of the direct objects.
substituteList = ('one','it','same','more')

intent = {'verb': '', 'dobj': ''}

print(doc.text)
for sent in doc.sents:
    print('Sentence: ', sent.text)
    for token in sent:
        print('Token: ', token.text, token.dep_, token.head.text)
        if token.dep_ == 'dobj':
            verbSyns = [item for item in verbList if token.head.text in item]
            # print(verbSyns)
            dobjSyns = [item for item in dobjList if token.text in item]
            # print(dobjSyns)
            substitute = [item for item in substituteList if token.text in item]
            # print(substitute)
            if (dobjSyns != [] or substitute != []) and verbSyns != []:
                intent['verb'] = verbSyns[0][0]
            if dobjSyns != []:
                intent['dobj'] = dobjSyns[0][0]

intentStr = intent['verb'] + intent['dobj'].capitalize()
print(intentStr)
