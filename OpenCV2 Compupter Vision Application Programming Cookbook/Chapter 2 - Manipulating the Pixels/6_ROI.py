import cv2
import numpy as np



if __name__ == "__main__":
    image = cv2.imread("../images/boldt.jpg")
    logo = cv2.imread("../images/logo.bmp")
    image_logo = image.copy()
    
    print image.shape
    
    for i in range(logo.shape[1]):
        for j in range(logo.shape[0]):
            image_logo[270 + j, 385 + i] = image_logo[270 + j, 385 + i] + 0.3 * logo[j, i] 
            
            # if use addWeigfhted function, we must add the source image, otherwise the logo is not trasparent.
            #image_logo[270 + j, 385 + i] = image_logo[270 + j, 385 + i] + logo[j, i]
    

            
    #cv2.addWeighted(image, 1.0, image_logo, 0.3, 0, image_logo)
    
    cv2.imshow("ROI", image_logo)
    
    cv2.waitKey(0)
    
    