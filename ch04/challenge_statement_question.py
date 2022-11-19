import spacy
nlp = spacy.load('en_core_web_sm')

'''
replaces first instance of find_word with find_tag with replace_word
if find_tag is empty it only replaces the find_word
if find_word is empty the replace_word will be put before the word found
 with find_tag
If find_tag and find_word are not found returns the original txt
'''
def replace_text(txt, replace_word, find_tag='', find_word=''):
    # replace_pos is one to result in skipping the found word
    #  use 0 so the replace_text is put in the sentence without replacing other words
    replace_pos = 0 if find_word == '' else 1
    
    doc = nlp(txt)
    for i, token in enumerate(doc):
        if (token.tag_ == find_tag or find_tag=='') \
            and (token.text == find_word or find_word == ''):
            sent = doc[:i].text + ' ' + replace_word + ' ' + doc[i+replace_pos:].text
            return sent
    return txt
    

original_txt = u'I can promise it is worth your time.'
doc = nlp(original_txt)

for token in doc:
    print(token.text, token.pos_, token.tag_)
print('\n')

sent = ''
for i, token in enumerate(doc):
    if token.tag_ == 'PRP' and doc[i+1].tag_ == 'MD' and doc[i+2].tag_ == 'VB':
        sent = doc[i+1].text.capitalize() + ' ' + doc[i].text
        sent = sent + ' ' + doc[i+2:].text
        break
#By now, you should have: 'Can I promise it is worth your time.'

#Retokenization
sent = replace_text(sent, 'you', 'PRP', 'I')
#By now, you should have: 'Can you promise it is worth your time.'

sent = replace_text(sent, 'my', 'PRP$', 'your')
#By now, you should have: 'Can you promise it is worth my time.'

sent = replace_text(sent, 'really', 'VB')
#By now, you should have: 'Can you really promise it is worth my time.'

doc = nlp(sent)
sent = doc[:len(doc)-1].text + '?'
#Finally, you should have: 'Can you really promise it is worth my time?'

print(sent)

