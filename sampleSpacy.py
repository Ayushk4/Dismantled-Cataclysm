
import spacy
import sys

def spacy_data(docu):
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(docu)

	people = []
	info_people = ['people', 'People', 'peoples', 'men','Men','women','Women','child','children','boy','Boy','boys']

	for token in doc:
		for k in info_people:
			if str(token.head)== str(k):
				if token.pos_ == 'NUM':
					people.append(str(token)+'  '+str(token.head))

	ailment = []
	for token in doc:
		if token.head.pos_ == 'NOUN': 
			if token.pos_ == 'ADJ' :
				ailment.append(str(token)+'  '+str(token.head))
			elif token.pos_ == 'VERB':
				ailment.append(str(token)+'  '+str(token.head))

	ner = doc.ents
	i = 0
	address = []
	for token in doc:
		i = i + 1
		if token.tag_ == 'IN':
			if token.text != 'with':
				for j in range(i,len(doc)):
					for k in doc.ents:
						if str(k) != str(doc[j]):
							address.append(doc[j])
						else:
							address.append(doc[j])
							break
				break

	donation = []

	for r in doc.ents:
		if r.label_ == 'MONEY' or 'TIME' or 'CARDINAL' or 'PRODUCT':
			donation.append(r.text)

	name = []

	for k in doc.ents:
		if k.label_ == 'PERSON':
			name.append(k.text)

	return (name,ailment,donation,address,people)