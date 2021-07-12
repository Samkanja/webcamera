import numpy as np
import  cv2

cap = cv2.VideoCapture(0)

camp2 = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter('output.avi', camp2,20.0, (648,480))

while (cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)

        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
