import spacy
import sys


def spacy_data(docu):
	nlp = spacy.load('en_core_web_sm')

	doc = nlp(docu)

	iterator = doc.__getitem__
	i = 0
	add = []
	for gpe in doc.ents:
		# print (gpe.label_)
		if gpe.label_ == 'GPE':
			add.append(gpe.text)
	#print (doc.ents[3])

	#sys.exit()
	flag = 0
	for ent in doc:
		i = i + 1
		if ent.text == ('at' or 'stuck' or 'stranded' or 'locked'):
			for k in range(i, len(doc)):
				for z in doc.ents:
					#print (z)
					#print (str(z))
					#print (doc[k])
					if (str(z)== str(doc[k])):
						add.append(doc[k])
						#print ("YEsjskdfjdkjfkdjf")
						flag = 1
						break
					else:
						add.append(doc[k])

				if (flag == 1):
					break

		if (flag == 1):
			break

	a = set(add)
	# print (list(a))

	donation = []

	for r in doc.ents:
		if r.label_ == 'MONEY' or 'TIME' or 'CARDINAL' or 'PRODUCT':
			#print r.label_
			donation.append(r.text)
	activity = []

	for r in doc:
		if r.pos_ == 'VERB':
			activity.append(r.text)	

	name = []

	for k in doc.ents:
		if k.label_ == 'PERSON':
			name.append(k.text)

	return (name,activity,donation,add)