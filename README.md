```
python3 -m venv $HOME/.virtualenvironments/nlp
source $HOME/.virtualenvironments/nlp/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
deactivate
```
See a dep_ stands for
>>> spacy.explain('pobj')
'object of preposition'
>>> spacy.explain('dobj')
'direct object'
>>> 
