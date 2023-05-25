import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=12,border=3) 
qr.add_data("youtube.com") 
qr.make(fit=True)
img=qr.make_image(fill_color="grey",back_color="purple")   
img.save("detailed_qrcode.png")