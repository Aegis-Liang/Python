import cv2
import numpy as np



if __name__ == "__main__":
    image = cv2.imread("../images/boldt.jpg")
    add = cv2.imread("../images/rain.jpg")
            
    cv2.addWeighted(image, 0.7, add, 0.9, 0, image)
    
    cv2.imshow("addWeighted", image)
    
    cv2.waitKey(0)
    