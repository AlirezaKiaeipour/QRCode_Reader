import cv2
from pyzbar.pyzbar import decode

cam = cv2.VideoCapture(0)
while True:
    _,frame = cam.read()

    for qr in decode(frame):
        cv2.putText(frame,qr.data.decode("utf-8"),(qr.rect[0],qr.rect[1]) , cv2.FONT_HERSHEY_PLAIN,1.5, (0,0,255), 2,cv2.LINE_AA)

    cv2.imshow("",frame)
    if cv2.waitKey(1) & 0xFF==ord("0"):
        break