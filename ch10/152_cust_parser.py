'''
Not working. There are changes due to newer version of Spacy but not sure how to make it work
'''
from spacy.training import Example
import spacy
nlp = spacy.blank('en')

TRAINING_DATA = [
    ('find a high paying job with no experience', {
        'heads': [0, 4, 4, 4, 0, 7, 7, 4],
        'deps': ['ROOT', '-', 'QUALITY', 'QUALITY', 'ACTIVITY', '-', 'QUALITY', 'ATTRIBUTE']
    }),
    ('find good workout classes near home', {
        'heads': [0, 4, 4, 0, 6, 4],
        'deps': ['ROOT', '-', 'QUALITY', 'ACTIVITY', 'QUALITY', 'ATTRIBUTE']
}) 
]

parser = nlp.create_pipe('parser')
nlp.add_pipe('parser', first=True)
for text, annotations in TRAINING_DATA:
    for d in annotations.get('deps', []):
        parser.add_label(d)
optimizer = nlp.begin_training()

import random
for i in range(25):
    random.shuffle(TRAINING_DATA)
    for text, annotations in TRAINING_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], drop=0.3)
        # nlp.update([text], [annotations], sgd=optimizer)
    # nlp.update(TRAINING_DATA, sgd=optimizer)
parser.to_dist('parser')
