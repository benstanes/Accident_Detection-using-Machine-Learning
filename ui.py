import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import cv2
import torch
import numpy as np
import winsound

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('mainwindow.ui', self)  # Load the UI file
        self.startButton.clicked.connect(self.start_detection)
        self.stopButton.clicked.connect(self.stop_detection)
        self.model = None
        self.cap = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.detect_and_display)
        
    def start_detection(self):
        if self.model is None:
            self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:\\Users\\HP\\Downloads\\accident-main\\last.pt', force_reload=True)
        if self.cap is None:
            self.cap = cv2.VideoCapture("C:\\Users\\HP\\Downloads\\accident-main\\detect.mp4")
            self.timer.start(10)  # Update every 10 milliseconds
            
    def stop_detection(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        if self.model is not None:
            self.model = None
        self.timer.stop()
        self.label.clear()  # Clear the label
        
    def detect_and_display(self):
        ret, frame = self.cap.read()
        if not ret:
            self.stop_detection()  # Stop detection if no frames left
            return
        results = self.model(frame)
        rendered_frame = np.squeeze(results.render())
        # Convert to RGB format expected by Qt
        rendered_frame = cv2.cvtColor(rendered_frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rendered_frame.shape
        bytes_per_line = ch * w
        q_img = QImage(rendered_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.label.setPixmap(pixmap)
        df = results.pandas().xyxy[0]
        for i in df['name']:
            if i == 'car crashing':
                winsound.Beep(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
