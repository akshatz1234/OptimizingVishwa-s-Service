from datetime import datetime
from flask import Response

def calc_age(dob):
    try:
        date = datetime.strptime(dob, "%d-%m-%Y")
        today = date.today()
        return today.year - date.year - ((today.month, today.day) < (date.month, date.day))
    except:
        return None

def clean(dob):
    if len(dob)==4:
        return "1-1-"+dob
    return(dob.replace('/','-'))

def main(dob):
    return(calc_age(clean(dob)))
