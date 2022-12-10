import spacy
nlp = spacy.load('en_core_web_md')

doc = nlp(u'In 2011, Google launched Google +, its fourth foray in social networking.')
doc.user_data['title'] = 'An example of a entity visualization'

# In the next block, instruct displaCy to render the markup wrapped as a full HTML page.
from spacy import displacy
html = displacy.render(doc, style='ent', page=True)

# Save the html file to disk
from pathlib import Path
output_path = Path('ent_visual.html')
output_path.open('w', encoding='utf-8').write(html)
