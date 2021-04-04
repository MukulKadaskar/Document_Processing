
from PIL import Image
import pytesseract
import cv2
import os

def scanForText(image,preprocess="thresh",showImgs=False):
    # Load the image and convert to grayscale
    image = cv2.imread(image)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Check the preprocessing selected, Either Threshold(thresh) or Blur(blur)
    if preprocess == "thresh":
    	gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    elif preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    # Create a temporary file of the preprocessed gray image to apply OCR
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # Load the temporary image as PILLOW image to apply OCR
    text = pytesseract.image_to_string(Image.open(filename),lang='eng+mar')
    words = text.split('\n')
    # words = [w.replace(["'",'`', '[',']','{','}','(', ')', ':', ',', '.', '!', '?', '"', ';'],"") for w in words]
    # while '' in words:
    #     words.remove('')
    words=list(filter(str.strip, words))
    # print(words)
    os.remove(filename)
    
    if showImgs:
        # Show the output images
        cv2.imshow("Image", image)
        cv2.imshow("Output", gray)
        cv2.waitKey(0)
    
    return words



if __name__ == '__main__':
    print(scanForText(image="uploads/sample.png",preprocess="blur"))
