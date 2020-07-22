import commonUtility
import re        
def reg(output):
    """
    In: OCR output(specifically back)
    Out: Processed text
    """
    regex = re.compile('[^A-Za-z0-9\s\,]')
    spc = re.compile("\s\s+")
    rn = re.compile('(DO|SO|D0|S0)')
    c = regex.sub('',output)
    c1 = rn.sub('',c)
    c2 = spc.sub(" ", c1)
    c3 = re.sub('(,\s)+', ', ', c2)
    return(c3)

def addex(c3):
    """
    In: Proccesed text
    Out: Address
    """
    tkn_add = commonUtility.word_tokenize(reg(c3))
    add = " "
    y = 0
    pin = re.compile('^\d{6}$')
    for i in tkn_add:
        p = pin.search(i)
        if y == 1:
            add += i + ' '
        if i == 'ADDRESS' or i == 'Add':
            y = 1
        elif p is not None:
            y = 0
    return(add)

        
def main_ex(output):
    tokenized_text = commonUtility.word_tokenize(output)
    classified_text = commonUtility.st.tag(tokenized_text)
    data = {}
    data['name'] = commonUtility.nameex(classified_text)
    data['dob'] = commonUtility.dateex(output)[1]
    data['age'] = commonUtility.age(dateex(output)[0])
    data['docType'] = "Driving Licence"
    data['address'] = addex(reg(output))
    data['bloodGroup'] = commonUtility.bloodGroup(output)
    return commonUtility.jsonify(data)