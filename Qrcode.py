import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #15 means the version of the qrcode (highter the number bigger the code image size)
    box_size = 10, #10 means the sizw of the box where qr code will be displayed
    border = 5 #5 it is the white part of the image -- border in all 4 sides with white color
)

data = "https://www.youtube.com/adityaankur"
# this is the path of my youtube channel


qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save('youtube_qr.png')