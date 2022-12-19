import spacy
import wikipedia
nlp = spacy.load('en_core_web_md')

doc = nlp(u"what do you know about rhinos?")
# doc = nlp(u'Have you heard of fried eggs with yellow tomatoes?')
print(doc.text)
# for token in doc:
    # print(token.text, token.dep_, token.pos_, token.tag_)

for t in doc:
    if t.dep_ == 'pobj' and (t.pos_ == 'NOUN' or tpos_ == 'PROPN'):
        phrase = (' '.join([child.text for child in t.lefts]) + ' ' + t.text).lstrip()
        first_noun = t.text
        break

for t in reversed(doc):
    if t.dep_ == 'pobj' and (t.pos_ == 'NOUN' or tpos_ == 'PROPN') and t.text != first_noun:
        phrase = phrase + ' ' + (t.head.text + ' ' + ' '.join([child.text for child in t.lefts]) + ' ' + t.text).lstrip()
        break

print('Phrase: ', phrase)
wiki_resp = wikipedia.page(phrase)
print("Article title: ", wiki_resp.title)
print("Article url: ", wiki_resp.url)
print("Article summary: ", wikipedia.summary(phrase, sentences=1))
