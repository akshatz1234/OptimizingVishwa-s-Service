import pytesseract
from flask import Flask, request, Response
import numpy as np
from PIL import Image, ImageEnhance
import cv2 as cv
import re
import imutils
import util_aadhar
import util_pan
import util_dl
import util_vi
import util_pass
import util_other

#preprocess
def preprocess(path):
    try:
        img = cv.imread(path,0)
        blurred = cv.blur(img, (5,5))
        canny = cv.Canny(blurred, 50, 200)
        pts = np.argwhere(canny>0)#edges of document
        y1,x1 = pts.min(axis=0)
        y2,x2 = pts.max(axis=0)
        cropped = img[y1:y2, x1:x2]# cropping 
        imS = imutils.resize(cropped, width=950)# resizing
        cv.imwrite('../project/temp1.jpg',imS)#rewrite image
        image = Image.open('../project/temp1.jpg')# open image
        enhancer = ImageEnhance.Brightness(image)#brightness
        enhanced_im = enhancer.enhance(1.7)#enhance image
        con = ImageEnhance.Contrast(enhanced_im)#contrast 
        con1 = con.enhance(1.3)# enhance
        enhancer_object = ImageEnhance.Sharpness(con1)#sharpness
        out = enhancer_object.enhance(3)#enhance
        out.save("../project/t2.jpg")
        i = cv.imread("../project/t2.jpg",0)
        text = pytesseract.image_to_string(i, lang='eng')
        if text == "":
            text = pytesseract.image_to_string(img, lang='eng')
            return text
        else:
            text = pytesseract.image_to_string(i, lang='eng')
            return(text)
    except:
        return "Cannot preprocess the file"

# categorization
def cat(out):
    try:
        if re.search("[0-9]{4}\ [0-9]{4}\ [0-9]{4}", out): # Aadhaar card
            return(util_aadhar.main_ex(out))
        elif re.search("[A-Z]{5}[0-9]{4}[A-Z]{1}", out) or re.search("Permanent", out): # pan card
            return util_pan.main_ex(out)
        elif re.search("ELECTION", out): # Election ID
            return(util_vi.main_ex(out))
        elif re.search("[A-Z]{2}[0-9]{2} [0-9]{11}", out): #driving license
            return(util_dl.main_ex(out))
        elif re.search("\b[A-Z]{1}[0-9]{6}\b", out):# passport
            return(util_pass.main_ex(out))
        else:
            return(util_other.main_ex(out))
    except:
        return "No Matching regex"

# allowed filenames
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

# function to denote allowed file formats-jpg, jpeg and png
def allowed_file(file):
    return ('.' in file and file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS)

# main Function
app = Flask(__name__)
def rear():
    f = request.files['file']
    f.save("../project/temp1.jpg")
    try:
        allowed_file(f)
        img = Image.open(f)
        img.load()
        return cat(preprocess('../project/temp1.jpg')) 
    except:
        return "Cannot read file"
    