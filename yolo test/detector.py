# Part A — starter code — isko complete karo
import cv2
cap = cv2.VideoCapture('traffic.mp4') # Video file load karo
while True:
 ret, frame = cap.read()
 if not ret:
    break
 # === TUMHARA CODE YAHAN ===
 # Frame dikhao — window ka naam 'Traffic Detector' rakho
 # 'q' press pe band karo
cap.release()
cv2.destroyAllWindows()