This repository contains the model,sourcecode and confusion matrix for detecting car accident.

instructions to be followed to run this model:
   1)open command prompt and clone this repository
   2)provide the following commands sequentially:1)'cd accident'
                                                 
                                                 2)'pip install -r req.txt'
                                                 
                                                 3)open 'money.py' in notepad which is prresent in this repository and define the path to last.pt which is present in this repository by modifying the folloing part of the code
                                                   'model = torch.hub.load('ultralytics/yolov5', 'custom', path='path to last.pt', force_reload=True)' and use double back-slashes(\\) to seperate the paths.
                                                   
                                                 4)The code in 'money.py' is meant to detect accident in realtime by obtaining video input from webcam,if the model is reuired to detect accident in a video 'ap = cv2.VideoCapture(0)' has to be replaced with 
                                                   'ap = cv2.VideoCapture('path to video seperated by double back slashes(\\))'.
                                                   
                                                 5)Finally run the program with the following command 'python money.py'.
