import mediapipe as mp
import cv2
import numpy as np
import uuid
import os

from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer

import time

# song = AudioSegment.from_mp3("drum.mp3")
mixer.init()
beat = mixer.Sound('beat.wav')
hihat_closed = mixer.Sound('hihat_closed.wav')
hihat_opened = mixer.Sound('hihat_opened.wav')

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

beat_just_played = False
hihat_closed_just_played = False
hihat_opened_just_played = False

beat_just_played_hand = 10
hihat_closed_just_played_hand = 10
hihat_opened_just_played_hand = 10

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

        print(image.shape[0])
        image = cv2.rectangle(image, (int(image.shape[1] * 0.0), int(image.shape[0] * 0.75)), (int(image.shape[1] * 0.25), int(image.shape[0] * 1)), (255, 0, 0), 4)
        image = cv2.rectangle(image, (int(image.shape[1] * 0.35), int(image.shape[0] * 0.75)), (int(image.shape[1] * 0.60), int(image.shape[0] * 1)), (0, 255, 0), 4)
        image = cv2.rectangle(image, (int(image.shape[1] * 0.75), int(image.shape[0] * 0.75)), (int(image.shape[1] * 1), int(image.shape[0] * 1)), (0, 0, 255), 4)

        # Rendering resultsd
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
                # print(hand.landmark[0].x)

                # Beat
                if hand.landmark[8].y > 0.75 and hand.landmark[8].x > 0 and hand.landmark[8].x < 0.25 and beat_just_played == False:
                    beat.play()
                    beat_just_played = True
                    beat_just_played_hand = num

                if hand.landmark[8].y > 0.75 and hand.landmark[8].x > .35 and hand.landmark[8].x < 0.60 and hihat_closed_just_played == False:
                    hihat_closed.play()
                    hihat_closed_just_played = True
                    hihat_closed_just_played_hand = num

                if hand.landmark[8].y > 0.75 and hand.landmark[8].x > .75 and hand.landmark[8].x < 1 and hihat_opened_just_played == False:
                    hihat_opened.play()
                    hihat_opened_just_played = True
                    hihat_opened_just_played_hand = num

                if hand.landmark[8].y < 0.75 and beat_just_played_hand == num: 
                    beat_just_played = False

                if hand.landmark[8].y < 0.75 and hihat_closed_just_played_hand == num: 
                    hihat_closed_just_played = False

                if hand.landmark[8].y < 0.75 and hihat_opened_just_played_hand == num: 
                    hihat_opened_just_played = False
    
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()