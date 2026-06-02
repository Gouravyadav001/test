#BUG1
vehicle_count = 15
green_time = 10 + vehicle_count * 2
print('Green time:', green_time)

#BUG2
signal_state = 'GREEN'
if signal_state == 'GREEN':
 print('Gaadiyaan chal sakti hain!')
else:
 print('Ruko!')

 #BUG3
lanes = ['North', 'South', 'East', 'West']
for lane in lanes:
 print('Lane:', lane)

 #BUG4
import cv2
img = cv2.imread('traffic.jpg')
cv2.imshow('Traffic', img)
cv2.destroyAllWindows()

#BUG5
# from ultralytics import YOLO
# import cv2
# model = YOLO('yolov8n.pt')
# img = cv2.imread('traffic.jpg')
# results = model(img)
# for box in results.boxes: # <-- yahan dhyan do
#  class_id = int(box.cls[0])
#  print(model.names[class_id])

from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
img = cv2.imread('traffic.jpg')
results = model(img)
for box in results[0].boxes: 
    class_id = int(box.cls[0].item())
    print(model.names[class_id])