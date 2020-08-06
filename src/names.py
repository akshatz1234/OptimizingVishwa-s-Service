from nltk.tag.stanford import StanfordNERTagger as st

# NER TAGGER
stanford_dir = '/home/akshatz/Documents/stanford-ner-4.0.0'
jarfile = stanford_dir + 'stanford-corenlp-3.7.0.jar'
st = st('/home/akshatz/Documents/stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz','/home/akshatz/Documents/stanford-ner-4.0.0/stanford-ner.jar')
# name extraction

def nameex(output):
    for tag, chunk in groupby(txt, lambda x:x[1]):
        if tag != "O" and tag == 'PERSON':
            a=" ".join(w for w, t in chunk)
            return(a)


tagged_sent = st.tag(sentence.split())

named_entities = nameex(tagged_sent)
named_entities_str_tag = [(" ".join([token for token, tag in ne]), ne[0][1]) for ne in named_entities]


print(named_entities_str_tag)