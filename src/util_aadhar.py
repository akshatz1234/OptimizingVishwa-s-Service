import commonUtility
import re 

# name extraction
def nameex(txt):
    """
    In: Classified text from StanfordNER
    Out: Name
    """
    try:
        continuous_chunk = []
        current_chunk = []
        for token, tag in txt:
            if tag == "PERSON": 
                current_chunk.append(token)
            else:
                if current_chunk: 
                    continuous_chunk.append(current_chunk)
        if current_chunk:
            current_chunk = " ".join(str(x) for x in current_chunk)
            return current_chunk
    except:
        return "None"


def main_ex(output):
    tokenized_text = commonUtility.word_tokenize(output)
    classified_text = commonUtility.st.tag(tokenized_text)
    data = {}
    data['docType'] = "AadhaarCard"
    data['name'] = nameex(classified_text)
    data['dob'] = commonUtility.dateex(output)
    data['age'] = commonUtility.age(data['dob'])
    data['gender'] = commonUtility.genex(tokenized_text)
    data['bloodGroup'] = ""
    data['address'] = ""
    return commonUtility.jsonify(data)