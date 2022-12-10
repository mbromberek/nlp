# import spacy
# nlp = spacy.load('en_core_web_md')


sent = {
 "words": [
   {"text": "I", "tag": "PRON"},
   {"text": "want", "tag": "VERB"},
   {"text": "a", "tag": "DET"},
   {"text": "Greek", "tag": "ADJ"},
   {"text": "pizza", "tag": "NOUN"}
 ],
 "arcs": [
   {"start": 0, "end": 1, "label": "nsubj", "dir": "left"},
   {"start": 2, "end": 4, "label": "det", "dir": "left"},
   {"start": 3, "end": 4, "label": "amod", "dir": "left"},
   {"start": 1, "end": 4, "label": "dobj", "dir": "right"}
 ]
}

from spacy import displacy
html = displacy.render(sent, style='dep', manual=True, page=True)

from pathlib import Path
output_path = Path('108_render.html')
output_path.open('w', encoding='utf-8').write(html)
