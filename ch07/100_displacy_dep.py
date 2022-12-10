import spacy
nlp = spacy.load('en_core_web_md')

doc = nlp(u'I want a Greek pizza.')
from spacy import displacy
# displacy.serve(doc, style='dep')

html = displacy.render([doc], style='dep', page=True)

from pathlib import Path
output_path = Path("sentence.html")
output_path.open("w", encoding="utf-8").write(html)

