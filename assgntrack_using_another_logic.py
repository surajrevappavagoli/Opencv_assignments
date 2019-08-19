import cv2


def nothing(x):
    pass

maxScaleUp = 50
scaleFactor = 0
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"



# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)


"""syntax
cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
"""
# Create Trackbar to choose percentage of scaling
cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, nothing)

# Create Trackbar to choose type of scaling ( Up or down )
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, nothing)

#scaleImage(25)

while True:
# Read image
    im = cv2.imread("truth.png")
#To get trackbar positions
    scaleImage = cv2.getTrackbarPos(trackbarValue, windowName)
    scaleTypeImage = cv2.getTrackbarPos(trackbarType, windowName)
    print("scaleImage:",scaleImage)
    print("scaleTypeImage:",scaleTypeImage)
    print("1+(scaleImage/100.0):",1+(scaleImage/100.0))
    print("1-(scaleImage/100.0):",1-(scaleImage/100.0))
    if scaleTypeImage == 0:

        im = cv2.resize(im, None, fx=(1+(scaleImage/100.0)),\
            fy =(1+(scaleImage/100.0)) , interpolation = cv2.INTER_LINEAR)
    else:
    	im = cv2.resize(im, None, fx=(1-(scaleImage/100.0)),\
            fy =(1-(scaleImage/100.0)) , interpolation = cv2.INTER_LINEAR)

    cv2.imshow(windowName,im)
    c = cv2.waitKey(20)
    if c==27:
        break


cv2.destroyAllWindows()
