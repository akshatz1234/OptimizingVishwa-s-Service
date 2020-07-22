from datetime import datetime

def calc_age(dob):
    date = datetime.strptime(dob, "%d-%m-%Y")
    today = date.today()
    return today.year - date.year - ((today.month, today.day) < (date.month, date.day))

def clean(dob):
    if len(dob)==4:
        return "1-1-"+dob
    return(dob.replace('/','-'))

def main(dob):
    return(calc_age(clean(dob)))
