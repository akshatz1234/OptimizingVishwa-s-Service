import commonUtility
import re        
import util_age

#date extraction
def dateex(output):
    """
    In: Output from the OCR
    out: Date
    """
    # print(output)
    try:
        date = re.findall("([0-9]{2}\/[0-9]{2}\/[0-9]{4}|[0-9]{2}\-[0-9]{2}\-[0-9]{4})", output)
        if not date:
            return(None,None)
        else:
            a = []
            for i in date:
                a.append(util_age.main(i))
            f = a.index(max(a))
            dob = date[f]
            return(max(a),dob)
    except:
        return None

#registration number 
def reg(output):
    """
    In: OCR output(specifically back)
    Out: Processed text
    """
    try:
        regex = re.compile('[^A-Za-z0-9\s\,]')
        spc = re.compile("\s\s+")
        rn = re.compile('(DO|SO|D0|S0)')
        c = regex.sub('',output)
        c1 = rn.sub('',c)
        c2 = spc.sub(" ", c1)
        c3 = re.sub('(,\s)+', ', ', c2)
        return(c3)
    except:
        return "None"

#address
def addex(c3):
    """
    In: Proccesed text
    Out: Address
    """
    # print(c3)
    try:
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
        return(add)
    except:
        return "None"

def main_ex(output):
    tokenized_text = commonUtility.word_tokenize(output)
    classified_text = commonUtility.st.tag(tokenized_text)
    data = {}
    data['docType'] = "Driving Licence"
    data['name'] = commonUtility.nameex(classified_text)
    data['age'] = dateex(output)[0]
    data['dob'] = dateex(output)[1]
    # data['address'] = addex(reg(output))
    data['bloodGroup'] = commonUtility.bloodGroup(output)
    return commonUtility.jsonify(data)