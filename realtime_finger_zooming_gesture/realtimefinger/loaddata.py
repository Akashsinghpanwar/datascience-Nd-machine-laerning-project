import cv2
import os

# Path to Hand folder
IMG_DIR = "Hand"
VID_DIR = "Handvid"

images = []

# Load images
for img in os.listdir(IMG_DIR):
    img_path = os.path.join(IMG_DIR, img)
    image = cv2.imread(img_path)
    if image is not None:
        images.append(image)

videos = []

# Load frames from videos
for vid in os.listdir(VID_DIR):
    vid_path = os.path.join(VID_DIR, vid)
    cap = cv2.VideoCapture(vid_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Add check for valid frame
        if frame is not None:
            videos.append(frame)
    cap.release()

print(f"Loaded {len(videos)} frames")
print(f"Loaded {len(images)} images")

# Placeholder values for width and height (replace with actual values)
width = 224
height = 224
