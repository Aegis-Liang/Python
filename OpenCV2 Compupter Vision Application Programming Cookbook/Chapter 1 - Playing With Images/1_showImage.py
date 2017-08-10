import cv2

def showImage():
    image = cv2.imread("../images/boldt.jpg")
    cv2.namedWindow("My Image")
    cv2.imshow("My Image", image)
    cv2.waitKey(0)
 
showImage()
