import pyqrcode
qr = pyqrcode.create("Rabia")
qr.png("qrcode.png", scale = 14)
qr.svg("qrcode.svg", scale = 14)
qr.eps("qrcode.eps", scale = 14)