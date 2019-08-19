

# import the necessary packages

import cv2

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
ref_point = []
cropping = False



def shape_selection(event, x, y, flags, param):
	# grab references to the global variables
	global ref_point, cropping
        
       

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		ref_point = [(x, y)]
		cropping = True

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		ref_point.append((x, y))
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
		cv2.imshow("window", image)
                



# load the image, clone it, and setup the mouse callback function

image = cv2.imread("sample.jpg")
clone = image.copy()
cv2.namedWindow("window")
cv2.setMouseCallback("window", shape_selection)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("window", image)
        	
	cv2.waitKey(1)
        #cv2.waitKey(1) & 0xFF
        
	cv2.putText(image,'''Choose top left corner, and drag.?''' ,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255), 2 );
# if there are two reference points, then crop the region of interest
# from teh image and display it
	if len(ref_point) == 2:
		crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
		cv2.imwrite("face.png", crop_img)
		break	
	
# close all open windows
cv2.destroyAllWindows()
