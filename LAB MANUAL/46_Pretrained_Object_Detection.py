# 36. Pretrained object detection
# Requires: pip install ultralytics
from ultralytics import YOLO
model=YOLO('yolo11n.pt')
# results=model('image.jpg')
print('Pretrained YOLO model loaded successfully.')
# Output: Pretrained YOLO model loaded successfully.