import commonUtility
import re

#docType
def docType(output):
    if re.search("ELECTION", output):
        return "VoterID"
    else: 
        return "None"


def main_ex(output):
    tokenized_text = commonUtility.word_tokenize(output)
    classified_text = commonUtility.st.tag(tokenized_text)
    data = {}
    data['docType'] = docType(output)
    data['name'] = commonUtility.nameex(classified_text)
    data['dob'] = commonUtility.dateex(output)
    data['age'] = commonUtility.age(data['dob'])
    data["gender"] = commonUtility.genex(tokenized_text)
    data['bloodGroup'] = ""
    data['address'] = ""    
    return commonUtility.jsonify(data)