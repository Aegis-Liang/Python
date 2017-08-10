import random
import cv2


def salt(imageIn, n):
    imageOut = imageIn.copy()
    for k in range(n):
        i = random.random() * imageOut.shape[0]
        j = random.random() * imageOut.shape[1]
        
        if imageOut.shape[2] == 1:
            imageOut[i, j] = 255
        elif imageOut.shape[2] == 3:
            imageOut[i, j][0] = 255
            imageOut[i, j][1] = 255
            imageOut[i, j][2] = 255
    return imageOut

            
if __name__ == "__main__":
    image = cv2.imread("../images/boldt.jpg")
    image2 = salt(image, 3000)
    cv2.namedWindow("My Image")
    cv2.imshow("My Image", image2)
    cv2.waitKey(0)    
        
    