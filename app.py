from flask import Flask
import cv2

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route('/working/<name>')
def hello_name(name):
   cap = cv2.VideoCapture(name)
   ret, frame = cap.read()
   return 'Working %s!' % name
