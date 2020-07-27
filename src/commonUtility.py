from nltk.tag.stanford import StanfordNERTagger as st
from nltk.tokenize import word_tokenize
import re
from itertools import groupby
from flask import jsonify
import util_age

# Stanford NER 
st = st('../resources/english.conll.4class.distsim.crf.ser.gz',
                       '../resources/stanford-ner.jar',
                       encoding='utf-8')

# name extraction
def nameex(txt):
    """
    In: Classified text from StanfordNER
    Out: Name
    """
    for tag, chunk in groupby(txt, lambda x:x[1]):
        if tag != "O" and tag == 'PERSON':
            a=" ".join(w for w, t in chunk)
            return(a)

# date extraction
def dateex(output):
    """
    In: Output from the OCR
    out: Date
    """
    date = re.search("([0-9]{2}\/[0-9]{2}\/[0-9]{4}|[0-9]{2}\-[0-9]{2}\-[0-9]{4})", output)
    if date is None:
        year = re.search("(19..|20..)", output)
        if year is None:
            return None
        else:
            return(year.group(1))
    else:
        return(date.group(1))


def age(dob):
    if dob == "None":
        return "None"
    else:
        return(util_age.main(dob))

def genex(tokenized_text):
    """
    In: OCR output Tokenized
    out: Gender
    """
    for i in tokenized_text:
        male = re.search("(^MA.E$|^Ma.e$)", i)
        female = re.search("(^FEMA.E$|^Fema.e$)", i)
        if male is not None:
            return "Male"
        if female is not None:
            return "Female"


def bloodGroup(output):
    regex = r"\bB\+|\bB-|\bA\+|\bA-|\bAB\+|\bAB-|\bO\+|\bO-"
    bg = re.search(regex, output)
    if bg is None:
        return("None")
    else:
        return(bg.group(0))
