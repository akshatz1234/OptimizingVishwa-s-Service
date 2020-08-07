import commonUtility
import re

# date extraction
def dateex(output):
    """
    In: Output from the OCR
    out: Date
    """
    try:
        date = re.findall("([0-9]{2}\/[0-9]{2}\/[0-9]{4}|[0-9]{2}\-[0-9]{2}\-[0-9]{4})", output)
        if not date:
           return(None,None) 
        else:
            a = []
            for i in date:
                a.append(util_age.main(i))
            f = a.index(min(a))
            dob = date[f]
            if max(a) == None:
                return dob
            else:
                return(max(a),dob)
    except:
        return "None"

def main_ex(output):
    tokenized_text = commonUtility.word_tokenize(output)
    classified_text = commonUtility.st.tag(tokenized_text)
    data = {}
    # print("HI")
    data['docType'] = "Passport"
    data['name'] = commonUtility.nameex(classified_text)
    data['dob'] = dateex(output)[0]
    data['age'] = dateex(output)[1]
    data['gender'] = ""
    data['bloodGroup'] = ""
    data['address'] = ""    
    return commonUtility.jsonify(data)