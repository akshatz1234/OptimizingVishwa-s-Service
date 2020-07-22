import pytesseract
from flask import Flask, request
import numpy as np
from PIL import Image, ImageEnhance
import cv2
import re
import imutils
import util_aadhar
import util_pan
import util_dl
import util_vi
import util_pass
import util_other

# allowed filenames
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

# function to denote allowed file formats-jpg, jpeg and png
def allowed_file(file):
    return ('.' in file and file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS)

# main Function
app = Flask(__name__)
# @app.route("/card", methods=['GET', 'POST'])
def rear():
    # file- input image
    f = request.files['file']
    try: 
        allowed_file(f)
        f.save("/home/akshatz/Documents/project/temp1.jpg")
        img = Image.open(f)
        img.load()
        text = pytesseract.image_to_string(img)
        return cat(text)
    except: 
        return ("Cannot read image, Please enter valid image type-jpg,jpeg and png ")

# categorization
def cat(out):
    num = re.search("([0-9]{4}\ [0-9]{4}\ [0-9]{4})", out)#aadhaar card
    if num is None:
        num = re.search("([A-Z]{5}[0-9]{4}[A-Z]{1})", out)#Pan card
        if num is None:
            num = re.search("^(?!^0+$)[a-zA-Z0-9]{3,20}$", out)#passport
            if num is None:
                num = re.search("ELECTION", out)#voter id
                if num is None:
                    num = re.search("([A-Z]{2}[0-9]{2} [0-9]{10})", out)#driving license
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
