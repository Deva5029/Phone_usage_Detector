# 📱 Phone Usage Detector  

This project detects handheld phone usage in videos (in hand, on lap, near face) using OpenCV. It outputs an annotated video with bounding boxes and confidence labels, while preserving audio, resolution, and FPS.  

---

## 🚀 Features
- Accepts `.mp4`, `.avi`, `.mov` input videos  
- Detects phones even with partial occlusion  
- Ignores static phones lying on a table  
- Outputs annotated video with bounding boxes  
- Optional: Logs timestamps of phone usage and generates a summary report  

---

## 🛠️ Setup (MacBook with VS Code)

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/phone_usage_detector_project.git
cd phone_usage_detector_project
```

### 2. Create & activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> ⚠️ If you get `ModuleNotFoundError: No module named 'cv2'` when running, make sure you’re using the `.venv` Python interpreter.  

### 4. Verify Python interpreter
Check which Python is active:
```bash
which python
```
It should point to:
```
.../phone_usage_detector_project/.venv/bin/python
```

If not, in VS Code:  
- Press **Cmd + Shift + P** → **Python: Select Interpreter**  
- Pick `.venv/bin/python (3.11)`  

---

## ▶️ Running the Detector

### 1. Put your test videos  
Save input videos in the `examples/` folder:  
```
examples/Test_1.mov
examples/Test_2.mp4
```

### 2. Run the script
```bash
.venv/bin/python phone_usage_detector.py --input examples/Test_1.mov --output outputs/annotated.mp4
```

This will:
- Read `examples/Test_1.mov`  
- Save annotated output to `outputs/annotated.mp4`  

### 3. Quick test (check cv2)
```bash
python -c "import cv2; print(cv2.__version__)"
```

---

## 📂 Project Structure
```
phone_usage_detector_project/
│── phone_usage_detector.py   # Main script
│── requirements.txt          # Dependencies
│── README.md                 # Documentation
│── examples/                 # Place your input videos here
│── outputs/                  # Annotated output videos
│── .venv/                    # Virtual environment
```

---

## 📤 Submitting
- Push the repo to GitHub:  
  ```bash
  git add .
  git commit -m "Initial commit - phone usage detector"
  git push origin main
  ```
- Share your GitHub repo link  
- Record a short demo video showing input → output  
