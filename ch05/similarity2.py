import spacy
nlp = spacy.load('en_core_web_md')

# Create a token for the word "fruits"
token = nlp(u'fruits')[0]
doc = nlp(u'I want to buy this beautiful book at the end of the week. Sales of citrus have increased over the last year. How much do you know about this type of tree?')
# Split doc into sentences
for sent in doc.sents:
    print(sent.text)
    print('similarity to', token.text, 'is', token.similarity(sent),'\n')
