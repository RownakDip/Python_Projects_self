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
            img = cv2.imread(image_location, 0)


            pixels_to_um = 0.3  # (1 px = 0.3 meters)

            # No need for any denoising or smoothing as the image looks good.
            # plt.hist(img.flat, bins=100, range=(0,255))

            # Change the grey image to binary by thresholding.
            ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

            # View the thresh image. Some boundaries are ambiguous / faint.

            # Step 3: Clean up image,
            kernel = np.ones((3, 3), np.uint8)
            eroded = cv2.erode(thresh, kernel, iterations=1)
            dilated = cv2.dilate(eroded, kernel, iterations=1)

            # Now, we need to apply threshold, meaning convert uint8 image to boolean.
            mask = dilated == 255  # Sets TRUE for all 255 valued pixels and FALSE for 0


            # use 8-connectivity, diagonal pixels will be included as part of a structure
            # this is ImageJ default but we have to specify this for Python, or 4-connectivity will be used
            # 4 connectivity would be [[0,1,0],[1,1,1],[0,1,0]]
            s = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            # label_im, nb_labels = ndimage.label(mask)
            labeled_mask, num_labels = ndimage.label(mask, structure=s)

            # Step 5: Measure the properties of each building (object)

            # regionprops function in skimage measure module calculates useful parameters for each object.

            # send in original image for Intensity measurements
            clusters = measure.regionprops(labeled_mask, img)
            # print(clusters[0].perimeter)
            count = 0
            for prop in clusters:
                count = count+1
                print('Label: {} Area: {}'.format(prop.label, prop.area*pixels_to_um**2))  #Convert pixel square to um square
            print(count)
            

            navne = []
            for prop in clusters:
                navne=['Label: {} Area: {} sqr meters'.format(prop.label, prop.area*pixels_to_um**2)]
                print(navne)

            return render_template("index.html", prediction=count,produkter = clusters, image_location=image_location)




    return render_template("index.html", prediction=0, image_location="")

if __name__ == "__main__":
    app.run(port=12000,debug=True)



    



