# import re
# import nltk
# from nltk.corpus import stopwords
# from nltk.corpus import wordnet
# stop = stopwords.words('english')

# string = 'Ravana was killed in a war'

# sentences = nltk.sent_tokenize(string)
# tokens = []
# for sent in sentences:
#     tokens.append(nltk.word_tokenize(sent)) 
# wordList = [nltk.pos_tag(token) for token in tokens]

# nounList = []

# print("HI")
# for word in nltk.pos_tag(wordList):
#     if re.match('[NN.*]', word[1]):
#         nounList.append(word[0])

# names = []
# for nouns in nounsList:
#     if not wordnet.synsets(nouns):
#         names.append(nouns)
#         print(names)
import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet

String = 'Ravana was killed in a war'

Sentences = nltk.sent_tokenize(String)
Tokens = []
for Sent in Sentences:
    Tokens.append(nltk.word_tokenize(Sent)) 
Words_List = [nltk.pos_tag(Token) for Token in Tokens]

Nouns_List = []

for List in Words_List:
    for Word in List:
        if re.match('[NN.*]', Word[1]):
             Nouns_List.append(Word[0])

Names = []
for Nouns in Nouns_List:
    if not wordnet.synsets(Nouns):
        Names.append(Nouns)

print(Names)