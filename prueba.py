import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image, ImageDraw, ImageFont

mp_face_mesh = mp.solutions.face_mesh
mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

print("Librerías importadas correctamente")
print(f"OpenCV: {cv2.__version__}")
print(f"MediaPipe: {mp.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Matplotlib: {plt.matplotlib.__version__}")
print(f"Pillow: {PIL.__version__}")