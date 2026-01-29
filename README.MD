# 🚦 Automated Vehicle Detection & Traffic Flow Analysis

A real-time **computer vision–based traffic analytics system** that detects, tracks, and analyzes vehicles from live video streams or recorded traffic footage.  
The system provides **vehicle classification, speed estimation, traffic statistics, and data-driven insights** using YOLOv8 and Python.

---

## 📌 Project Overview

This project is designed to help analyze road traffic conditions by automatically detecting vehicles and generating meaningful analytics such as:
- Vehicle counts
- Speed estimation
- Date-wise traffic reports
- Visual summaries of traffic flow

It can be used for **smart city applications, traffic monitoring, and intelligent transportation systems**.

---

## ✨ Key Features

✅ Real-time vehicle detection using **YOLOv8**  
✅ Vehicle tracking with **unique IDs (SORT algorithm)**  
✅ Speed estimation (km/h) using centroid displacement  
✅ Over-speed indication  
✅ Automatic logging of vehicle data (CSV)  
✅ Date-wise traffic report generation  
✅ Traffic visualization (bar graphs)  
✅ Works with webcam or traffic videos  

---

## 🧠 Technologies Used

- **Python 3**
- **OpenCV**
- **YOLOv8 (Ultralytics)**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **SciPy**
- **SORT Tracking Algorithm**

---
## 🚗 Run Vehicle Detection
Webcam
python main.py --source 0
Video File
python main.py --source traffic.mp4
Press ESC to stop execution.
---
📊 Generate Date-Wise Traffic Report
After running detection:
python generate_date_report.py
---
📁 Output generated in:
output/date_wise_report.csv

📈 Output & Results
Live detection window with bounding boxes, IDs, and speed
CSV logs storing detailed vehicle data
Graphs showing vehicle distribution
Date-wise reports for traffic analysis

🎯 Applications
Smart traffic monitoring
Traffic flow analysis
Speed violation analysis
Smart city & ITS solutions

🚀 Future Enhancements
Lane-wise vehicle counting
Automatic speed calibration
Traffic density estimation
Web dashboard (Streamlit)
Cloud deployment

👨‍💻 Author

Surya Omar
📌 B.Tech – Computer Science & Engineering (AI & ML)
📫 GitHub: surya323-ma

⭐ Acknowledgements
Ultralytics YOLOv8
OpenCV community
SORT tracking algorithm
