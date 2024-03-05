import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
from pygame import mixer
from time import perf_counter

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic 
mp_hands = mp.solutions.hands

mixer.init()
low = mixer.Sound(os.path.join("trumpet_sounds", "low.wav"))
middle = mixer.Sound(os.path.join("trumpet_sounds", "middle.wav"))
high = mixer.Sound(os.path.join("trumpet_sounds", "high.wav"))

# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

global just_played_high 
global just_played_middle 
global just_played_low 

## Setup mediapipe instance
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic, \
     mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

# results = face_mesh.process(image)

# if results.multi_face_landmarks:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

         # Flip on horizontal
        image = cv2.flip(image, 1)
        
        image.flags.writeable = False
      
        # Make detection
        results = holistic.process(image)
        # Detections
        hand_results = hands.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
            mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
            mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
        )        

        # Rendering hand results
        if hand_results.multi_hand_landmarks:
            for num, hand in enumerate(hand_results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                    mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                )   

            if results.face_landmarks and len(hand_results.multi_hand_landmarks) > 1:
                mouth_distance = results.face_landmarks.landmark[15].y - results.face_landmarks.landmark[13].y
                print("MOUTH: ", mouth_distance)

                hand_distance = abs(hand_results.multi_hand_landmarks[1].landmark[3].x - hand_results.multi_hand_landmarks[0].landmark[3].x)
                print("HANDS: ", hand_distance)
            
                image = cv2.rectangle(image, (int(image.shape[1]* hand_results.multi_hand_landmarks[1].landmark[3].x), int(image.shape[0]* hand_results.multi_hand_landmarks[1].landmark[3].y)), (int(image.shape[1]* hand_results.multi_hand_landmarks[0].landmark[3].x), int(image.shape[0]* hand_results.multi_hand_landmarks[0].landmark[3].y)), (34,177,218), -1)

                if mouth_distance < 0.02:
                    print("JUST PLAYED", (just_played_low - perf_counter()))
                    if hand_distance > 0.4 and (just_played_low - perf_counter()) > 0.75:
                        low.play()
                        just_played_low = perf_counter()
                    elif hand_distance < 0.4 and hand_distance > 0.15 :
                        middle.play()
                        just_played_middle = perf_counter()
                    elif hand_distance < 0.15 :
                        high.play()
                        just_played_high = perf_counter()

                if mouth_distance > 0.02:
                    # just_played_high 
                    # just_played_middle
                    # just_played_low 
                    pass

        # if results.face_landmarks != None:
        #     print(results.face_landmarks.landmark[15])
        #     image = cv2.rectangle(image, (int(image.shape[1]* results.face_landmarks.landmark[15].x), int(image.shape[0]* results.face_landmarks.landmark[15].y)), (image.shape[1]* int(results.face_landmarks.landmark[15].x +10), int(image.shape[0]* results.face_landmarks.landmark[15].y +100)), (218, 226, 226), -1)   # C A

        #     image = cv2.rectangle(image, (int(image.shape[1]* results.face_landmarks.landmark[13].x), int(image.shape[0]* results.face_landmarks.landmark[13].y)), (image.shape[1]* int(results.face_landmarks.landmark[13].x +10), int(image.shape[0]* results.face_landmarks.landmark[13].y +100)), (218, 226, 226), -1)   # C A

        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
#     while cap.isOpened():
#         ret, frame = cap.read()
        
#         # BGR 2 RGB
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
#         # Flip on horizontal
#         image = cv2.flip(image, 1)
        
#         # Set flag
#         image.flags.writeable = False
        
#         # Detections
#         results = hands.process(image)
        
#         # Set flag to true
#         image.flags.writeable = True
        
#         # RGB 2 BGR
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         # Rendering resultsd
#         if results.multi_hand_landmarks:
#             for num, hand in enumerate(results.multi_hand_landmarks):
#                 mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
#                                         mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
#                                         mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
#                                          )
                
#         cv2.imshow('Hand Tracking', image)

#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break

    cap.release()
    cv2.destroyAllWindows()