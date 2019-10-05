import cv2


class Recognizer(object):
    def __init__(self, minc, maxc):
        self.cap = cv2.VideoCapture(0)
        self.minc = minc
        self.maxc = maxc

    def recognize(self):
        ret, frame = cap.read()
        if not ret:
            return None
        hsv = cv2.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.minc, self.maxc)
        mask = cv2.erod(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        _, cont, hier = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        f = any([item.any() for item in count])
        if (f):
            best_fit = max(cont, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(best_fit)
            return [x + 0.5 * w, y + 0.5 * h)]+ list(frame.shape)
        return None

    def run(self):
        while self.cap.isOpened():
            values = self.recognize()
            print(values)
            if values is None:
                continue
        self.cap.release()
