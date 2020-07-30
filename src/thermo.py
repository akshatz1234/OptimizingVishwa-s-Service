import pytesseract
import cv2 as cv
import os
import numpy as np
from PIL import Image
from flask import Flask, request, Response

# categorization
def cat(out):
    num = re.search("([0-9]{4}\ [0-9]{4}\ [0-9]{4})", out)#aadhaar card
    if num is None:
        num = re.search("([A-Z]{5}[0-9]{4}[A-Z]{1})", out)#Pan card
        if num is None:
            num = re.search("IND", out)# passport
            if num is None:
                num = re.search("ELECTION", out)# Voter ID
                if num is None:
                    num = re.search("([A-Z]{2}[0-9]{2} [0-9]{11})", out)#driving license
                    if num is None:
                        word = re.search("Permanent",out)# PAN card
                        if word is None:
                            return(util_other.main_ex(out))
                        else:
                            return(util_pan.main_ex(out))
                    else:
                        return(util_dl.main_ex(out))
                else:
                    return(util_vi.main_ex(out))
            else:
                return(util_pass.main_ex(out))
        else:
            return(util_pan.main_ex(out))
    else:
        return(util_aadhar.main_ex(out))

# allowed filenames
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

# function to denote allowed file formats-jpg, jpeg and png
def allowed_file(file):
    return ('.' in file and file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS)

app = Flask(__name__)
@app.route('/temperature',methods = ['GET', 'POST'])
def therm():
    try:
        f = request.files['file']
        while allowed_file(f):
            f.save('../project/tem.jpg')
            img = Image.open(f)
            img.load()
            text = pytesseract.image_to_string('../project/tem.jpg')
            if text == "":
                return "No text"
            else:
                return text
            break
    except:
        return "Not readable"
if __name__ == "__main__":
    app.debug = True
    app.run(host = '127.0.0.1',port=5000, threaded = False)
