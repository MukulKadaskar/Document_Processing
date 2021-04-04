# from cv2 import cv2
import cv2
# from PIL import Image
# from matplotlib import image
from cv2 import imread
from cv2 import imwrite
from cv2 import imshow
from cv2 import CascadeClassifier
from cv2 import rectangle
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
# from google.colab.patches import cv2_imshow


def extract_face(img):
    # Establishing paths to the model data files
    # base_dir = os.path.dirname(__file__)
    # prototxt_path = os.path.join(base_dir + '/model_data/deploy.prototxt')
    # caffemodel_path = os.path.join(base_dir + '/model_data/weights.caffemodel')

    # face_model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

    # image = cv2.imread('uploads/prathamesh.jpg')

    # (h, w) = image.shape[:2]
    # blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    # face_model.setInput(blob)
    # detections = face_model.forward()
    # # Identify each face
    # for i in range(0, detections.shape[2]):
    # 	box=detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    # 	(startX, startY, endX, endY) = box.astype("int")
    # 	confidence = detections[0, 0, i, 2]

    # 	if confidence > 0.5:
    # 		frame = image[startY:endY, startX:endX]
    # 		cv2.imwrite(base_dir+'/static/prathamesh.jpg', frame)
    # 		# cv2.imshow("frame",frame)
    # 		# cv2.waitKey(0)
    # 		# cv2.destroyAllWindows()

    pixels = imread('uploads/upload.png')
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    bboxes = classifier.detectMultiScale(pixels, 1.1, 15)
    for box in bboxes:
        x, y, width, height = box
        x2, y2 = x+width, y+height
        w = int(width*0.3)
        h = int(height*0.5)
        rectangle(pixels, (x-w, y-h), (x2+w, y2+h), (0, 0, 255), 1)
        cv2.imwrite('static/faces/output.jpg', pixels[y-h:y2+h, x-w:x2+w])
        # cv2.imshow("pixels", pixels)
        # print(box)

def extract_facemtcnn():
    pixels = pyplot.imread('uploads/prathamesh.jpg')
    # ax = pyplot.gca()
    # ax = pyplot.gca()
    # pyplot.imshow(pixels)
    detector = MTCNN()
    faces = detector.detect_faces(pixels)
    print(faces)
    for box in faces:
        x, y, width, height = box['box']
        x2,y2 = x+width, y+height
        w = int(width*0.3)
        h = int(height*0.3)
        pyplot.imshow(pixels[y-h:y2+h,x-w:x2+w])
        pyplot.savefig('static/faces/output1.jpg')


if __name__ == '__main__':
    # extract_face('uploads/prathamesh.jpg')
    extract_facemtcnn()
