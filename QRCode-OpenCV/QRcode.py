import cv2
import numpy as np
import sys
import time


imgPath = "/home/surajvagoli/QRCode-OpenCV/IDCard-Satya.png"
img = cv2.imread(imgPath)


# Create a qrCodeDetector Object
qrDecoder = cv2.QRCodeDetector()
opencvData,bbox,rectifiedImage = qrDecoder.detectAndDecode(img)

if opencvData != None:
    print("QR Code Detected")
else:
    print("QR Code NOT Detected")



# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)

    # Display results
    


# Detect and decode the qrcode


print("QR Code Detected!")
print("Decoded Data : {}".format(opencvData))
display(img, bbox)


     
resultImagePath = "QRCode-Output.png"   
cv2.imwrite(resultImagePath,img)
cv2.imshow("Results", img)


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", img)    

    
cv2.waitKey(0)
cv2.destroyAllWindows()
