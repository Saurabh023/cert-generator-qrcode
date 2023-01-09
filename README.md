# cert-generator-qrcode
Certificate Generator with QR Code in Python

My goal is to build a simple certificate generator by providing only name in a text file line by line, then certificate got generated along with a QR code with a single command. The only thing needed in this project is the template on which the name and QR code (link for QR Code verification of the certificates) is printed and the file containing names ("names.txt"). You can edit/change the QR Code link, names.txt and the certificate template in the file "main.py" itself according to your choice in this project.

Features of this projects are: it prints name of the candidate and QR code on the certificate template.

It can be run with a simple command
python3 main.py

This command will save all the certificates provided by the "names.txt" file in the "output" directory.

Sample certificates is there in the "output" directory to get a overview of how the names and QR code is printed in the certificates.
