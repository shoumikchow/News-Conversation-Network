from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
tagged = st.tag('Rami Eid is studying at Stony Brook University in NY'.split())
for tags in tagged:
	if 'PERSON' in tags or 'ORGANIZATION' in tags or 'LOCATION' in tags :
		print (tags)