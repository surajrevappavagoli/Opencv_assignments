import cv2

maxScaleUp = 100
scaleFactor = 0
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

# load an image
im = cv2.imread("truth.png")

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

# Callback functions
def scaleImage(*args):
    global scaleFactor
    global scaleType
    scaleFactor = 1+ args[0]/100.0
    if scaleFactor == 0:
        scaleFactor = 1
    if scaleType == 0:
    	scaledImage = cv2.resize(im, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    else:
    	scaledImage = cv2.resize(im, None, fx=(1-(args[0]/100.0)),\
            fy =(1-(args[0]/100.0)) , interpolation = cv2.INTER_LINEAR)	
    cv2.imshow(windowName, scaledImage)


# Callback functions
def scaleTypeImage(*args):
    global scaleType
    global scaleFactor
    scaleType = args[0]

cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleTypeImage)

scaleImage(10)

while True:
    print(scaleFactor)
    c = cv2.waitKey(20)
    if c==27:
        break

cv2.destroyAllWindows()
