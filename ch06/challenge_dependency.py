import spacy
nlp = spacy.load('en_core_web_md')

doc1 = nlp(u'We can overtake them. You must specify it. I could do it.')
sents = list(doc1.sents)

for sent in sents[1:]:
    print('\n' + str(sent))
    for i in range(len(sent)-1):
        if sents[0][i].dep_ == sent[i].dep_:
            print(sents[0][i].text, sent[i].text, sents[0][i].dep_, spacy.explain(sents[0][i].dep_))
