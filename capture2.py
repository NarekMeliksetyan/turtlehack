import cv2

def callback():
	pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('result')

cv2.createTrackbar('minb', 'result', 0, 315, callback)
cv2.createTrackbar('ming', 'result', 0, 255, callback)
cv2.createTrackbar('minr', 'result', 0, 255, callback)

cv2.createTrackbar('maxb', 'result', 0, 255, callback)
cv2.createTrackbar('maxg', 'result', 0, 255, callback)
cv2.createTrackbar('maxr', 'result', 0, 255, callback)

while (cap.isOpened()):
	ret, frame = cap.read()
	if (ret == True):

		cv2.imshow('frame', frame)
		frameCopy = frame.copy()
		minb = cv2.getTrackbarPos('minb', 'result')
		ming = cv2.getTrackbarPos('ming', 'result')
		minr = cv2.getTrackbarPos('minr', 'result')

		maxb = cv2.getTrackbarPos('maxb', 'result')
		maxg = cv2.getTrackbarPos('maxg', 'result')
		maxr = cv2.getTrackbarPos('maxr', 'result')
		min_col = (85, 110, 0)
		max_col = (255, 255, 255)

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		#hsv = cv2.blur(hsv, (1,1))
		mask = cv2.inRange(hsv, (minb, ming, minr), (maxb, maxg, maxr))

		mask = cv2.erode(mask, None, iterations = 2)
		mask = cv2.dilate(mask, None, iterations = 4)

		cont = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		cont = cont[0]
		if (cont):
			sorted(cont, key = cv2.contourArea, reverse = True)
			cv2.drawContours(frame, cont, 0, (255, 0, 255), 3)
			cv2.imshow("Contours", frame)
			for i in range(len(cont)):
				(x, y, w, h) = cv2.boundingRect(cont[i])
				print(w)
				if ((w < 20 or h > 100) or (h < 20 or w > 100)):
					cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
					cv2.imshow('frame', frame)

		if (cv2.waitKey(1) & 0xFF == ord('q')):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()
