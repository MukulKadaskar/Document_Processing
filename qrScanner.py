from pyzbar import pyzbar
from PIL import Image
import xmltodict

def scanQR(file_name):
    #Decode data from QR of given image file_name
    image = Image.open('uploads/'+file_name)
    decodedList = pyzbar.decode(image)

    #Decoded data is a list which has a nested list at position 0
    #Accessing the data attribute of to get the data contained in the QR Code
    barcodeData = decodedList[0].data

    #Using only the xml data in the QR Code of Aadhar Card for parsing to a dict
    xmlData = str(barcodeData)[42:-1]
    return xmltodict.parse(xmlData,attr_prefix='')


if __name__ == '__main__':
    print(scanQR('prathamesh.jpg'))
