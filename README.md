# nifi-tesseract-python
Using Python Tesseract 4 with Apache NiFi

Using the deep learning edition

brew unlink tesseract

brew install tesseract --HEAD

pip install pytesseract

tesseract --version

tesseract tesseract.png -psm 3 -l eng stdout

For this version NiFi runs run.sh

we create an images directory to store new scans

You could point at a directory of faxes or scanned documents
 
Example Run:


 ./run.sh
{"text": "Pra eed Pract ai diartunity\ncient py ; Pett\n\nApache NiFi is an easy to use. powerful, and reliable system to process Pa)\n\nstribute data. It provides an end-to-end platform that can collect, curate,\nRE ell\n\ndrag-and-drop visual interface. This book offers you an overview of NiFi o bs\nete Tot et]\neran\n\n \n \n  \n\n \n\nee ue oe r\nFaas ATG Reet\nere ae a)\nPeet ay ae\nOe ed Pan ad a\nBy ou Sn Pores\n\nip NFito\nIT oy fon ne age sey", "imgname": "images/tesseract_image_20180608205642_682c7902-67c1-4c83-8f4f-6ae8b390c26a.jpg", "host": "HW13125.local", "end": "1528491417.212745", "te": "16.390816926956177", "battery": 100, "systemtime": "06/08/2018 16:56:57", "cpu": 63.4, "diskusage": "116437.1 MB", "memory": 62.2, "id": "20180608205642_682c7902-67c1-4c83-8f4f-6ae8b390c26a"}

