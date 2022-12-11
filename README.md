```
python3 -m venv $HOME/.virtualenvironments/nlp
source $HOME/.virtualenvironments/nlp/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
deactivate
```
See a dep_ stands for
```
>>> spacy.explain('pobj')
'object of preposition'
>>> spacy.explain('dobj')
'direct object'
>>> 
```

Site for seeing breakdown of a sentence
```
https://demos.explosion.ai/displacy?text=I%20want%20a%20dish&model=en_core_web_sm&cpu=1&cph=0
```