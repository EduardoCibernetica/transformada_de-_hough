import cv2
import numpy as np

img = cv2.imread('fichas/46.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img, (x1,y1), (x2,y2), (0, 0, 255), 8, cv2.LINE_AA)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=20, maxRadius=30)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)

cv2.imshow('detected circles', img)
cv2.waitKey()