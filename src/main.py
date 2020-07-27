import time
startTime=time.time()
endTime = time.time()
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

def preprocess(path):
    img = cv.imread(path,0)
    blurred = cv.blur(img, (3,3))
    canny = cv.Canny(blurred, 50, 200)
    pts = np.argwhere(canny>0)
    y1,x1 = pts.min(axis=0)
    y2,x2 = pts.max(axis=0)
    cropped = img[y1:y2, x1:x2]
    imS = imutils.resize(cropped, width=950)
    cv.imwrite('../project/temp1.jpg',imS);
    image = Image.open('../project/temp1.jpg')
    enhancer = ImageEnhance.Brightness(image)
    enhanced_im = enhancer.enhance(1.7)
    con = ImageEnhance.Contrast(enhanced_im)
    con1 = con.enhance(1.3)
    enhancer_object = ImageEnhance.Sharpness(con1)
    out = enhancer_object.enhance(3)
    out.save("../project/t2.jpg")
    i = cv.imread("../project/t2.jpg",0)
    text = pytesseract.image_to_string(i, lang='eng')
    # print(text)
    return(text)


# categorization
def cat(out):
    num = re.search("([0-9]{4}\ [0-9]{4}\ [0-9]{4})", out)#aadhaar card
    if num is None:
        num = re.search("([A-Z]{5}[0-9]{4}[A-Z]{1})", out)#Pan card
        if num is None:
            num = re.search("^[A-PR-WYa-pr-wy][1-9]\\d \\s?\\d{4}[1-9]$", out)# passport
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

# main Function
app = Flask(__name__)
def rear():
    f = request.files['file']
    f.save("../project/temp1.jpg")
    # try:
    startTime
    allowed_file(f)
    img = Image.open(f)
    img.load()
    return cat(preprocess('../project/temp1.jpg')) 
    # except:
    #     return "Cannot read file"
    