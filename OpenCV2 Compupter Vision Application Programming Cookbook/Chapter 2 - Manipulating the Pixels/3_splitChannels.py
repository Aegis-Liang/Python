import cv2
import numpy as np


            
    
if __name__ == "__main__":
    image = cv2.imread("../images/boldt.jpg")
    
    
    b0 = np.zeros((image.shape[0],image.shape[1]), dtype=image.dtype)  
    g0 = np.zeros((image.shape[0],image.shape[1]), dtype=image.dtype)  
    r0 = np.zeros((image.shape[0],image.shape[1]), dtype=image.dtype)  
    
    b,g,r = cv2.split(image)
    
    imageb = cv2.merge([b, g0, r0])
    cv2.namedWindow("My Image b")
    cv2.imshow("My Image b", imageb)
    
    imageg = cv2.merge([b0, g, r0])
    cv2.namedWindow("My Image g")
    cv2.imshow("My Image g", imageg)    
    
    imager = cv2.merge([b0, g0, r])
    cv2.namedWindow("My Image r")
    cv2.imshow("My Image r", imager)        
    
  
    
    cv2.waitKey(0)           
    