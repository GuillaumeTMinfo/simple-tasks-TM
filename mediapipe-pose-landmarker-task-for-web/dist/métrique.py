import math
import random
import cv2
import mediapipe as mp
from mediapipe.python.solutions.drawing_utils import _normalized_to_pixel_coordinates

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
    
def angle_to_percentage(angle):
# angle to percentage converter

    if angle < 0 or angle > 180:
        raise ValueError("L'angle doit être compris entre 0 et 180 degrés.")

    # Calculer le pourcentage en utilisant une relation linéaire
    percentage = (angle / 180) * 100

    return percentage

