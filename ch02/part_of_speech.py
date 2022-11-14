import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I have flown to LA. Now I am flying to Frisco.') 
print([w.text for w in doc])
# Output: ['I', 'have', 'flown', 'to', 'LA', '.', 'Now', 'I', 'am', 'flying', 'to', 'Frisco', '.']
print([w.text for w in doc if w.tag_=='VBG' or w.tag_=='VB'])
# Output: ['flying']

print([w.text for w in doc if w.pos_ == 'PROPN'])
# Output: ['LA', 'Frisco']
