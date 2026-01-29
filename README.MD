Project Overview
This project is a complete, real-time vehicle detection and traffic analytics system built with Python. It uses computer vision to detect, track, and analyze vehicles in traffic videos or webcam feeds. The system provides:

Vehicle detection (car, bus, truck, bike)
Vehicle tracking with unique IDs
Speed estimation and over-speeding flagging
Real-time display of analytics
Logging and visualization of results
Tech Stack
Python 3.9+
OpenCV
NumPy
YOLOv8 (Ultralytics)
SORT (Simple Online and Realtime Tracking)
Matplotlib
Pandas
Features
Load traffic video or webcam feed
Detect vehicles (car, bus, truck, bike) using YOLOv8
Track vehicles with SORT (unique IDs)
Count vehicles (no double-counting)
Estimate speed (distance/frame, FPS, pixel-to-meter calibration)
Flag over-speeding vehicles
Display bounding boxes, IDs, class, speed
Log all data to CSV
Generate bar graph of vehicle counts
Robust to multiple vehicles and occlusion