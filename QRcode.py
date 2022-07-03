import pyqrcode
import png 

link = "https://www.google.com"
qr_code = pyqrcode.create(link)
qr_code.png("google.png", scale=5)