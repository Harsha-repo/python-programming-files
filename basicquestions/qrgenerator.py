import qrcode                   
from pyzbar.pyzbar import decode
from PIL import Image

my_qr = qrcode.make('https://www.youtube.com/shorts/LAS3HvwySjU')
my_qr1 = qrcode.make('https://neal.fun/size-of-space/')
my_qr.save('my_qr.png', scale = 8)
my_qr1.save('my_qr1.png',scale=7)

b = decode(Image.open('my_qr.png'))
print(b[0].data.decode('ascii'))