import cv2

with open("color.txt", "r") as fd:
	lines = fd.read().splitlines()
color = lines[0]
color = 'red'
def callback():
	pass
coordinates = []
cap = cv2.VideoCapture(0)
count = 0
while (cap.isOpened()):
	ret, frame = cap.read()
	if (ret == True):
		if (color == 'green'):
			(minb, ming, minr), (maxb, maxg, maxr) = (0, 210, 67), (255, 255, 195)
		elif (color == 'yellow'):
			(minb, ming, minr), (maxb, maxg, maxr) = (16, 67, 0), (54, 190, 255)
		elif (color == 'red'):
			(minb, ming, minr), (maxb, maxg, maxr) = (162, 123, 0), (255, 255, 255)
		elif (color == 'blue' ):
			(minb, ming, minr), (maxb, maxg, maxr) = (0, 171, 125), (255, 255, 186)
		else:
			pass
		(minb, ming, minr), (maxb, maxg, maxr) = (0, 171, 125), (255, 255, 186)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		#hsv = cv2.blur(hsv, (1,1))

		mask = cv2.inRange(hsv, (minb, ming, minr), (maxb, maxg, maxr))
		mask = cv2.erode(mask, None, iterations = 2)
		mask = cv2.dilate(mask, None, iterations = 4)
		cv2.imwrite("mask_processed.png", mask)
		_, cont, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		f = any([item.any() for item in cont])
		if (f):
			best_fit = max(cont, key=cv2.contourArea)
			cv2.drawContours(frame, best_fit, 0, (255, 0, 255), 3)
			(x, y, w, h) = cv2.boundingRect(best_fit)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
			coordinates.append((int((x+(x+w)/2)), int((y+(y+h)/2))))
			cv2.drawMarker(frame,(int((x+(x+w))/2), int((y+(y+h))/2)), (0, 255, 255))
			cv2.imwrite("image_processed.png", frame)
			count += 1
			if (count == 2):
				cv2.drawMarker(frame,(int((x+(x+w))/2), int((y+(y+h))/2)), (0, 255, 255))
				cv2.imwrite("image_processed.png", frame)
				break
	else:
		break
def return_coordinates():
	return(coordinates[2])
print(coordinates[0])
cap.release()
cv2.destroyAllWindows()
