import cv2
import numpy as np




if __name__ == "__main__":
    image = cv2.imread("../images/boldt.jpg")
    
    kernel_sharpen = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    imageOut = cv2.filter2D(image, -1, kernel_sharpen)
    cv2.imshow('Sharpening', imageOut)
    
    cv2.waitKey(0)