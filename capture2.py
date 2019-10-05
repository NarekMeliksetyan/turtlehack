import cv2
def callback():
	pass
coordinates = []
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
	ret, frame = cap.read()
	if (ret == True):
		(minb, ming, minr), (maxb, maxg, maxr) = (56, 234, 81), (255, 255, 255)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		#hsv = cv2.blur(hsv, (1,1))

		mask = cv2.inRange(hsv, (minb, ming, minr), (maxb, maxg, maxr))
		mask = cv2.erode(mask, None, iterations = 2)
		mask = cv2.dilate(mask, None, iterations = 4)

		cont = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		cont = cont[0]
		if (cont):
			best_fit = max(cont, key=cv2.contourArea)
			cv2.drawContours(frame, best_fit, 0, (255, 0, 255), 3)
			(x, y, w, h) = cv2.boundingRect(best_fit)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
			coordinates.append(((x-(x+w)/2), (y-(y+h)/2)))
			break
	else:
		break
def return_coordinates():
	return(coordinates[0])
print(coordinates[0])
cap.release()
cv2.destroyAllWindows()
