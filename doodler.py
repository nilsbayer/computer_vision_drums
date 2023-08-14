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

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

# Video Writer 
video_writer = cv2.VideoWriter(os.path.join('output','output1.avi'), cv2.VideoWriter_fourcc('P','I','M','1'), fps, (width, height), isColor=True)                                                                                         

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

                tilt = hand.landmark[4].x - hand.landmark[1].x

                if tilt < -0.05:
                    pyautogui.keyUp("right")
                    pyautogui.keyDown("left")
                    # pyautogui.press("left")

                if tilt > 0.05:
                    pyautogui.keyUp("left")
                    pyautogui.keyDown("right")
                    # pyautogui.press("right")
                    pass

                if tilt > -0.05 and tilt < 0.05:
                    # pyautogui.keyUp("right")
                    # pyautogui.keyUp("left")
                    pass


        else:
            image = cv2.rectangle(image, (int(image.shape[1] * 0.35), int(image.shape[0] * 0.75)), (int(image.shape[1] * 0.60), int(image.shape[0] * 1)), (0, 0, 0), 4)
    
        cv2.imshow('Hand Tracking', image)

        video_writer.write(image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
video_writer.release()