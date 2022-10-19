import string
import qrcode



addTextToQRCode = input('Add a text to qrgenerator: ')

addNameToFile = input('Please name your image name: ')

img = qrcode.make(addTextToQRCode)

img.save(addNameToFile)