import commonUtility
import re

def docType(output):
    emp = re.search("Employee|EMPLOYEE", output)
    if emp:
        return("Employee_id")
    else:
        return(None)


def main_ex(output):
    tokenized_text = commonUtility.word_tokenize(output)
    classified_text = commonUtility.st.tag(tokenized_text)
    data = {}
    data['name'] = commonUtility.nameex(classified_text)
    data['dob'] = commonUtility.dateex(output)
    data['age'] = commonUtility.age(data['dob'])
    data['docType'] = docType(output)
    data['gender'] = commonUtility.genex(tokenized_text)
    data['bloodGroup'] = commonUtility.bloodGroup(output)
    data['address'] = ""
    return commonUtility.jsonify(data)
