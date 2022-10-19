import string
import qrcode



addTextToQRCode = input('Add a text to qrgenerator: ')


img = qrcode.make(addTextToQRCode)

img.save("testing.png")