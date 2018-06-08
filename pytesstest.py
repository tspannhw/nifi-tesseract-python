import cv2
import sys
import pytesseract
import traceback
import math
import random, string
import base64
import uuid
import time
import sys
import datetime
import subprocess
import sys
import os
import datetime
import traceback
import math
import random, string
import base64
import json
from time import gmtime, strftime
import numpy as np
import cv2
import math
import random, string
import time
import psutil

from time import gmtime, strftime
start = time.time()
cap = cv2.VideoCapture(1)  # 0 - laptop 1 - display

packet_size=3000

# Create unique image name
id = '{0}_{1}'.format(strftime("%Y%m%d%H%M%S",gmtime()),uuid.uuid4())
ret, frame = cap.read()

filename = 'images/tesseract_image_{0}.jpg'.format(id)
cv2.imwrite(filename, frame)
config = ('-l eng --oem 1 --psm 3')

# Read image from disk
#  im = cv2.imread(imPath, cv2.IMREAD_COLOR)

# Run tesseract OCR on image
try:
     row = { }
     text = pytesseract.image_to_string(frame, config=config)
     end = time.time()
     row['text'] = text
     row['imgname'] = filename
     row['host'] = os.uname()[1]
     row['end'] = '{0}'.format( str(end ))
     row['te'] = '{0}'.format(str(end-start))
     row['battery'] = psutil.sensors_battery()[0]
     row['systemtime'] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
     row['cpu'] = psutil.cpu_percent(interval=1)
     usage = psutil.disk_usage("/")
     row['diskusage'] = "{:.1f} MB".format(float(usage.free) / 1024 / 1024)
     row['memory'] = psutil.virtual_memory().percent
     row['id'] = str(id)
     json_string = json.dumps(row)  
     print (json_string )
except:
     print("{\"message\": \"Failed to run\"}")
