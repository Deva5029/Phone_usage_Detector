import cv2
import torch
import numpy as np
import mediapipe as mp
import argparse
import os
import subprocess
from pathlib import Path
from ultralytics import YOLO

def parse_args():
    parser = argparse.ArgumentParser(description="Phone Usage Detector")
    parser.add_argument("--input", type=str, required=True, help="Path to input video")
    parser.add_argument("--output", type=str, required=True, help="Path to save annotated video")
    parser.add_argument("--log_csv", type=str, help="Optional: save detection log as CSV")
    parser.add_argument("--summary_json", type=str, help="Optional: save summary report as JSON")
    parser.add_argument("--conf", type=float, default=0.25, help="YOLO confidence threshold")
    parser.add_argument("--stride", type=int, default=1, help="Process every Nth frame")
    parser.add_argument("--device", type=str, default="cpu", help="Device: 'cpu', 'cuda:0', or 'mps'")
    return parser.parse_args()

def main():
    args = parse_args()
    cap = cv2.VideoCapture(args.input)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    temp_out = str(Path(args.output).with_suffix(".noaudio.mp4"))
    out = cv2.VideoWriter(temp_out, fourcc, fps, (width, height))

    # Load YOLOv8
    model = YOLO("yolov8n.pt")
    model.to(args.device)

    # Mediapipe face/hand landmarks
    mp_face = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
    mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % args.stride != 0:
            frame_idx += 1
            continue

        # YOLO detections
        results = model(frame, conf=args.conf)
        for det in results[0].boxes.data.cpu().numpy():
            x1, y1, x2, y2, score, cls = det
            if int(cls) == 67:  # class 67 = cell phone in COCO
                label = f"Phone {score:.2f}"
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
                cv2.putText(frame, label, (int(x1), int(y1)-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        out.write(frame)
        frame_idx += 1

    cap.release()
    out.release()

    # Add audio back
    try:
        cmd = [
            "ffmpeg", "-y", "-i", temp_out, "-i", args.input, "-c", "copy",
            "-map", "0:v:0", "-map", "1:a:0?", args.output
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(temp_out)
    except Exception as e:
        print("FFmpeg audio muxing failed:", e)

if __name__ == "__main__":
    main()
