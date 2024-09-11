import math
import random
import cv2
import argparse
import mediapipe as mp
import numpy as np
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates

import numpy as np
import cv2
import math
from dist.constant import POSE

cap = cv2.VideoCapture('video_bad_mobility_TMinfo.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()


print(angle_to_percentage(0))



# angle between two lines with one common point
def angle(self, point1, point2, point3):

    if(point1==(0,0) or point2==(0,0) or point3==(0,0)):
        return 0
    numerator = point2[1] * (point1[0] - point3[0]) + point1[1] * \
                (point3[0] - point2[0]) + point3[1] * (point2[0] - point1[0])
    denominator = (point2[0] - point1[0]) * (point1[0] - point3[0]) + \
                (point2[1] - point1[1]) * (point1[1] - point3[1])
    try:
        ang = math.atan(numerator/denominator)
        ang = ang * 180 / math.pi
        if ang < 0:
            ang = 180 + ang
        return ang
    except:
        return 90.0
    
def angle_to_percentage(ang):
# angle to percentage converter

    if ang < 0 or ang > 180:
        raise ValueError("L'angle doit être compris entre 0 et 180 degrés.")

    # Calculer le pourcentage en utilisant une relation linéaire
    percentage = (ang / 180) * 100

    return percentage

def get_keypoints(self, image, pose_result):
# get keypoints
    key_points = {}
    image_rows, image_cols, _ = image.shape
    for idx, landmark in enumerate(pose_result.pose_landmarks.landmark):
        if ((landmark.HasField('visibility') and landmark.visibility < VISIBILITY_THRESHOLD) or
            (landmark.HasField('presence') and landmark.presence < PRESENCE_THRESHOLD)):
            continue
        landmark_px = _normalized_to_pixel_coordinates(landmark.x, landmark.y,
                                                        image_cols, image_rows)
        if landmark_px:
            key_points[idx] = landmark_px
    return key_points
def get_point(self, str_point):
        
    #get point from keypoints
    return self.key_points[POSE[str_point]] if self.is_point_in_keypoints(str_point) else None

