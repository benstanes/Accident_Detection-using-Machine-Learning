
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import winsound


model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\HP\\Downloads\\accident-main\\last.pt', force_reload=True)

cap = cv2.VideoCapture("C:\\Users\\HP\\Downloads\\accident-main\\detect.mp4")
lst = []
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    df = results.pandas().xyxy[0]
    for i in df['name']:
              lst.append(i)
              print(i)
              if(i=='car crashing'):
                winsound.Beep(1000, 500)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
