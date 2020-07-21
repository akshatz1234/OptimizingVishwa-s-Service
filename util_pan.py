import commonUtility
        
def main_ex(output):
    tokenized_text = commonUtility.word_tokenize(output)
    classified_text = commonUtility.st.tag(tokenized_text)
    data = {}
    data['name'] = commonUtility.nameex(classified_text)
    data['dob'] = commonUtility.dateex(output)
    data['age'] = commonUtility.age(data['dob'])
    data['docType'] = "PAN_card"
    data['gender'] = ""
    data['bloodGroup'] = ""
    data['address'] = ""
    return commonUtility.jsonify(data)