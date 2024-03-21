import cv2
from loaddata import images, videos

# Placeholder values for width and height (replace with actual values)
width = 224
height = 224

def preprocess_images(images, width, height):
    processed_images = []
    for image in images:
        # Resize image to (width, height)
        resized_image = cv2.resize(image, (width, height))
        # Optionally, you can perform additional preprocessing steps here
        processed_images.append(resized_image)
    return processed_images

def preprocess_videos(videos, width, height):
    processed_videos = []
    for video in videos:
        frames = []
        for frame in video:
            # Resize frame to (width, height)
            resized_frame = cv2.resize(frame, (width, height))
            # Optionally, you can perform additional preprocessing steps here
            frames.append(resized_frame)
        processed_videos.append(frames)
    return processed_videos

# Load data from loaddata.py
from loaddata import images, videos

# Preprocess images
processed_images = preprocess_images(images, width, height)

# Preprocess videos
processed_videos = preprocess_videos(videos, width, height)
