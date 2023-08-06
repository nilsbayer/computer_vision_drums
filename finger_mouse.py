import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import numpy as np

import pyautogui

import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

just_clicked = False
just_scrolled = False

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()
        
        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip on horizontal
        image = cv2.flip(image, 1)
        
        # Set flag
        image.flags.writeable = False
        
        # Detections
        results = hands.process(image)
        
        # Set flag to true
        image.flags.writeable = True
        
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        screen_width, screen_height = pyautogui.size()
        mouse_x, mouse_y = pyautogui.position() 

        # Rendering resultsd
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
                # print(hand.landmark[0].x)

                # Move mouse by finger movements
                pyautogui.moveTo(hand.landmark[8].x * screen_width, hand.landmark[8].y * screen_height)

                index_finger = np.array((hand.landmark[8].x, hand.landmark[8].y))
                middle_finger = np.array((hand.landmark[12].x, hand.landmark[12].y))
                dis_fingers = np.linalg.norm(index_finger - middle_finger)

                index_finger = np.array((hand.landmark[8].x, hand.landmark[8].y))
                middle_finger = np.array((hand.landmark[20].x, hand.landmark[20].y))
                dis_fingers_scroll = np.linalg.norm(index_finger - middle_finger)

                if dis_fingers < .1 and just_clicked == False:
                    pyautogui.click()
                    just_clicked = True

                if dis_fingers > .1:
                    just_clicked = False

                if dis_fingers_scroll < .2 and just_scrolled == False:
                    pyautogui.scroll(-10)
                    just_scrolled = True

                if dis_fingers_scroll > .2:
                    just_scrolled = False

        if just_clicked == True:
            image = cv2.rectangle(image, (int(image.shape[1] * 0.35), int(image.shape[0] * 0.75)), (int(image.shape[1] * 0.60), int(image.shape[0] * 1)), (0, 255, 0), 4)

        else:
            image = cv2.rectangle(image, (int(image.shape[1] * 0.35), int(image.shape[0] * 0.75)), (int(image.shape[1] * 0.60), int(image.shape[0] * 1)), (0, 0, 0), 4)
    
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()