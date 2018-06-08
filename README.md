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
 
