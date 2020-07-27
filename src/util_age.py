from datetime import datetime, date
from flask import Response

def calc_age(dob):
    today = date.today()
    bdate = datetime.strptime(str(dob), "%d/%m/%Y")
    age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
    return age

def clean(dob):
    if len(dob)==4:
        return "1-1-"+dob
    else:
        return(dob.replace('-','/'))


def main(dob):
    # print(dob)
    return(calc_age(clean(dob)))
