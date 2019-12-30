import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output.avi", fourcc, 30, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        output.write(frame)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
output.release()
cv2.destroyAllWindows()