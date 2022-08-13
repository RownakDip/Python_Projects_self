import os
from flask import Flask
from flask import request
from flask import render_template
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure, color, io


app = Flask(__name__)
UPLOAD_FOLDER = "D:\PHYTHON code\Model load\static"


@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join(UPLOAD_FOLDER, image_file.filename)
            image_file.save(image_location)

            # STEP1 - Read image and define pixel size
            print(image_location)
            file="static/area.png"
            image = cv2.imread(image_location)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
            cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            total = 0

            for c in cnts:
                x,y,w,h = cv2.boundingRect(c)
                mask = np.zeros(image.shape, dtype=np.uint8)
                cv2.fillPoly(mask, [c], [255,255,255])
                mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
                pixels = cv2.countNonZero(mask)
                pixels = pixels*.09
                total += pixels
                cv2.putText(image, '{:.1f}'.format(pixels), (x,y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

            print(total)

            #cv2.imshow('thresh', thresh)
            #cv2.imshow('image', image)
            
            cv2.imwrite(file, image)
            cv2.waitKey(0)

            

          

            return render_template("label.html", prediction=file, image_location=image_location)




    return render_template("label.html", prediction=0, image_location="")

if __name__ == "__main__":
    app.run(port=12000,debug=True)



    



