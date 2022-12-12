import spacy
nlp = spacy.load('en_core_web_md')

def word2int(numword):
    num = 0
    try:
        num = int(numword)
        return num
    except ValueError:
        pass
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    for idx, word in enumerate(words):
        if word in numword:
            num = idx
            break
    return num

text = u'I want a Greek pizza.'
doc = nlp(text)
orderdict = {}
for token in doc:
    if token.dep_ == 'dobj':
        dobj = token
        orderdict.update(product=dobj.lemma_)
        for child in dobj.lefts:
            if child.dep_ == 'amod' or child.dep_ == 'compound':
                orderdict.update(ptype=child.text)
            elif child.dep_ == 'det':
                orderdict.update(qty=1)
            elif child.dep_ == 'nummod':
                orderdict.update(qty=word2int(child.text))
        break

print(orderdict)