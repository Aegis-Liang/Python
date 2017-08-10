import cv2


def colorReduce(imageIn, div=64):
    imageOut = imageIn.copy()
    rows = imageOut.shape[0]
    cols = imageOut.shape[1]
    
    for i in range(rows):
        for j in range(cols):
            imageOut[i, j] = imageOut[i, j]/div*div + div/2
            
    return imageOut
            
    
if __name__ == "__main__":
    image = cv2.imread("../images/boldt.jpg")
    image2 = colorReduce(image, 64)
    
    cv2.namedWindow("My Image")
    cv2.imshow("My Image", image)    
    
    cv2.namedWindow("My Image 2")
    cv2.imshow("My Image 2", image2)
    cv2.waitKey(0)        