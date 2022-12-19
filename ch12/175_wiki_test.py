import spacy
import wikipedia
nlp = spacy.load('en_core_web_md')

doc = nlp(u"what do you know about rhinos?")
print(doc.text)
for t in doc:
    if t.dep_ == 'pobj' and (t.pos_ == 'NOUN' or tpos_ == 'PROPN'):
        phrase = (' '.join([child.text for child in t.lefts]) + ' ' + t.text).lstrip()
        break

wiki_resp = wikipedia.page(phrase)
print("Article title: ", wiki_resp.title)
print("Article url: ", wiki_resp.url)
print("Article summary: ", wikipedia.summary(phrase, sentences=1))
