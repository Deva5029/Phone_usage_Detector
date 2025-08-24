# 📱 Phone Usage Detector

This project detects handheld phone usage in videos using computer vision (OpenCV + YOLO).  
It highlights phones with bounding boxes and outputs an annotated video.

---

## 📂 Project Structure

```
phone_usage_detector_project/
│── phone_usage_detector.py   # Main script
│── requirements.txt          # Dependencies
│── README.md                 # Documentation
│── examples/                 # Place your test input videos here
│    └── Test_1.mov
│── outputs/                  # Processed annotated videos will be saved here
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Deva5029/phone_usage_detector_project.git
cd phone_usage_detector_project
```

### 2. Create a Virtual Environment (Recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows (PowerShell)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Detector

1. Put your test videos in the `examples/` folder (e.g., `examples/Test_1.mov`).
2. Run the script:

```bash
python phone_usage_detector.py --input examples/Test_1.mov --output outputs/annotated.mp4
```

- The **input** video comes from the `examples/` folder.
- The **output** annotated video will be saved in the `outputs/` folder.
- The output keeps the same resolution, FPS, and audio as the input.

---

## ✅ Features
- Detects phones in hand, on lap, or near face.
- Ignores static phones (e.g., on a table).
- Handles partial occlusions.
- Maintains video resolution, FPS, and audio.
- Near real-time performance.

---

## 🔥 Optional Enhancements
- Log timestamps of phone usage.
- Generate a summary usage report.

---

## 📧 Contact
For questions or submissions: **vlad@plexor.ai**
