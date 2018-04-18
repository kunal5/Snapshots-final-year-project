import cv2
import random
import time
#import imutils
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('template.html')

@app.route('/my-link/')
def my_link():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    def get_image():
        retval, im = cam.read()
        return im
    d = 0

    while True:
        k = cv2.waitKey(1)
        temp = get_image()
        #rotated = imutils.rotate(temp,0)
        cv2.imshow('temp',temp)
        print("taking image")

        if d == 0:
            c = str(random.randint(1,101))
            file = "C:\\Users\\user\\Desktop\\screenshot\\test_image" + c + ".png"
            time.sleep(10)
            cv2.imwrite(file, temp)
        d = d+1

    del(cam)

if __name__ == '__main__':
  app.run(debug=True)
