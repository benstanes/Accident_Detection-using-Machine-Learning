import torch
import numpy as np
import cv2
import winsound

# Load the model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\HP\\Downloads\\accident-main\\last.pt', force_reload=True)

# Open the video file
cap = cv2.VideoCapture("C:\\Users\\HP\\Downloads\\accident-main\\detect.mp4")
lst = []

# Loop through each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    # Display the detections
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    # Process detection results
    df = results.pandas().xyxy[0]
    car_crashing_detected = False
    for i in df['name']:
        lst.append(i)
        print(i)
        if i == 'car crashing':
            winsound.Beep(1000, 500)
            car_crashing_detected = True
    
    # If 'car crashing' is not detected, print 'car not crashing'
    if not car_crashing_detected:
        print('car not crashing')
    
    # Check for 'q' key press to quit the loop
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
