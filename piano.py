import mediapipe as mp
import cv2
import numpy as np
import os
import numpy as np

from pygame import mixer

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

mixer.init()
a0 = mixer.Sound(os.path.join("piano_sounds", "a0.wav"))
h0 = mixer.Sound(os.path.join("piano_sounds", "h0.wav"))
c1 = mixer.Sound(os.path.join("piano_sounds", "c1.wav"))
d1 = mixer.Sound(os.path.join("piano_sounds", "d1.wav"))
e1 = mixer.Sound(os.path.join("piano_sounds", "e1.wav"))
f1 = mixer.Sound(os.path.join("piano_sounds", "f1.wav"))
g1 = mixer.Sound(os.path.join("piano_sounds", "g1.wav"))
a1 = mixer.Sound(os.path.join("piano_sounds", "a1.wav"))
h1 = mixer.Sound(os.path.join("piano_sounds", "h1.wav"))
c2 = mixer.Sound(os.path.join("piano_sounds", "c2.wav"))
d2 = mixer.Sound(os.path.join("piano_sounds", "d2.wav"))

cap = cv2.VideoCapture(0)

a0_played = False
h0_played = False
c1_played = False
d1_played = False
e1_played = False
f1_played = False
g1_played = False
a1_played = False
h1_played = False
c2_played = False
d2_played = False

a0_played_pinky = False
h0_played_pinky = False
c1_played_pinky = False
d1_played_pinky = False
e1_played_pinky = False
f1_played_pinky = False
g1_played_pinky = False
a1_played_pinky = False
h1_played_pinky = False
c2_played_pinky = False
d2_played_pinky = False

a0_played_hand = -10
h0_played_hand = -10
c1_played_hand = -10
d1_played_hand = -10
e1_played_hand = -10
f1_played_hand = -10
g1_played_hand = -10
a1_played_hand = -10
h1_played_hand = -10
c2_played_hand = -10
d2_played_hand = -10

played_color = (193, 217, 222)

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

        image = cv2.rectangle(image, (int(image.shape[1] * 0.0), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.1), int(image.shape[0] * 0.2)), (218, 226, 226), -1)   # C A
        image = cv2.rectangle(image, (int(image.shape[1] * 0.11), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.21), int(image.shape[0] * 0.2)), (218, 226, 226), -1) # D H
        image = cv2.rectangle(image, (int(image.shape[1] * 0.22), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.32), int(image.shape[0] * 0.2)), (218, 226, 226), -1) # E C
        image = cv2.rectangle(image, (int(image.shape[1] * 0.33), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.43), int(image.shape[0] * 0.2)), (218, 226, 226), -1) # F D
        image = cv2.rectangle(image, (int(image.shape[1] * 0.44), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.54), int(image.shape[0] * 0.2)), (218, 226, 226), -1) # G E 
        image = cv2.rectangle(image, (int(image.shape[1] * 0.55), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.65), int(image.shape[0] * 0.2)), (218, 226, 226), -1) # A F
        image = cv2.rectangle(image, (int(image.shape[1] * 0.66), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.76), int(image.shape[0] * 0.2)), (218, 226, 226), -1) # H G
        image = cv2.rectangle(image, (int(image.shape[1] * 0.77), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.87), int(image.shape[0] * 0.2)), (218, 226, 226), -1) # C A
        image = cv2.rectangle(image, (int(image.shape[1] * 0.88), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.98), int(image.shape[0] * 0.2)), (218, 226, 226), -1) # D H

        # Rendering resultsd
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
                # Initial z threshold -0.08
                print(hand.landmark[8].z, hand.landmark[20].z)

                "************************* index finger ********************************"
                # A0
                if a0_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.0 and hand.landmark[8].x < 0.1 and hand.landmark[8].y < 0.2:
                    a0.play()
                    a0_played = True
                    a0_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.0), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.1), int(image.shape[0] * 0.2)), played_color, -1)   # C A

                # H0  
                if h0_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.11 and hand.landmark[8].x < 0.21 and hand.landmark[8].y < 0.2:
                    h0.play()
                    h0_played = True
                    h0_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.11), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.21), int(image.shape[0] * 0.2)), played_color, -1) # D H

                # C1  
                if c1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.22 and hand.landmark[8].x < 0.32 and hand.landmark[8].y < 0.2:
                    c1.play()
                    c1_played = True
                    c1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.22), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.32), int(image.shape[0] * 0.2)), played_color, -1) # E C
                
                # D1  
                if d1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.33 and hand.landmark[8].x < 0.43 and hand.landmark[8].y < 0.2:
                    d1.play()
                    d1_played = True
                    d1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.33), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.43), int(image.shape[0] * 0.2)), played_color, -1) # F D
                
                # E1  
                if e1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.44 and hand.landmark[8].x < 0.54 and hand.landmark[8].y < 0.2:
                    e1.play()
                    e1_played = True
                    e1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.44), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.54), int(image.shape[0] * 0.2)), played_color, -1) # G E 
                
                # F1  
                if f1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.55 and hand.landmark[8].x < 0.65 and hand.landmark[8].y < 0.2:
                    f1.play()
                    f1_played = True
                    f1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.55), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.65), int(image.shape[0] * 0.2)), played_color, -1) # A F
                
                # G1  
                if g1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.66 and hand.landmark[8].x < 0.76 and hand.landmark[8].y < 0.2:
                    g1.play()
                    g1_played = True
                    g1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.66), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.76), int(image.shape[0] * 0.2)), played_color, -1) # H G
                
                # A1  
                if a1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.77 and hand.landmark[8].x < 0.87 and hand.landmark[8].y < 0.2:
                    a1.play()
                    a1_played = True
                    a1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.77), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.87), int(image.shape[0] * 0.2)), played_color, -1) # C A
                
                # H1  
                if h1_played == False and hand.landmark[8].z < -0.08 and hand.landmark[8].x > 0.88 and hand.landmark[8].x < 0.98 and hand.landmark[8].y < 0.2:
                    h1.play()
                    h1_played = True
                    h1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.88), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.98), int(image.shape[0] * 0.2)), played_color, -1) # D H
                
                # A0 released
                if a0_played == True and hand.landmark[8].z > -0.08 and a0_played_hand == num:
                    a0_played = False
                
                # H0 released
                if h0_played == True and hand.landmark[8].z > -0.08 and h0_played_hand == num:
                    h0_played = False
                
                # C1 released    
                if c1_played == True and hand.landmark[8].z > -0.08 and c1_played_hand == num:
                    c1_played = False
                
                # D1 released    
                if d1_played == True and hand.landmark[8].z > -0.08 and d1_played_hand == num:
                    d1_played = False
                
                # E1 released    
                if e1_played == True and hand.landmark[8].z > -0.08 and e1_played_hand == num:
                    e1_played = False
                
                # F1 released    
                if f1_played == True and hand.landmark[8].z > -0.08 and f1_played_hand == num:
                    f1_played = False
                
                # G1 released    
                if g1_played == True and hand.landmark[8].z > -0.08 and g1_played_hand == num:
                    g1_played = False
                
                # A1 released    
                if a1_played == True and hand.landmark[8].z > -0.08 and a1_played_hand == num:
                    a1_played = False
                
                # A1 released    
                if h1_played == True and hand.landmark[8].z > -0.08 and h1_played_hand == num:
                    h1_played = False


                "************************* pinky finger ********************************"
                # A0
                if a0_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.0 and hand.landmark[20].x < 0.1 and hand.landmark[20].y < 0.2:
                    a0.play()
                    a0_played_pinky = True
                    a0_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.0), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.1), int(image.shape[0] * 0.2)), played_color, -1)   # C A

                # H0  
                if h0_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.11 and hand.landmark[20].x < 0.21 and hand.landmark[20].y < 0.2:
                    h0.play()
                    h0_played_pinky = True
                    h0_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.11), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.21), int(image.shape[0] * 0.2)), played_color, -1) # D H

                # C1  
                if c1_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.22 and hand.landmark[20].x < 0.32 and hand.landmark[20].y < 0.2:
                    c1.play()
                    c1_played_pinky = True
                    c1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.22), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.32), int(image.shape[0] * 0.2)), played_color, -1) # E C
                
                # D1  
                if d1_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.33 and hand.landmark[20].x < 0.43 and hand.landmark[20].y < 0.2:
                    d1.play()
                    d1_played_pinky = True
                    d1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.33), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.43), int(image.shape[0] * 0.2)), played_color, -1) # F D
                
                # E1  
                if e1_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.44 and hand.landmark[20].x < 0.54 and hand.landmark[20].y < 0.2:
                    e1.play()
                    e1_played_pinky = True
                    e1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.44), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.54), int(image.shape[0] * 0.2)), played_color, -1) # G E 
                
                # F1  
                if f1_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.55 and hand.landmark[20].x < 0.65 and hand.landmark[20].y < 0.2:
                    f1.play()
                    f1_played_pinky = True
                    f1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.55), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.65), int(image.shape[0] * 0.2)), played_color, -1) # A F
                
                # G1  
                if g1_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.66 and hand.landmark[20].x < 0.76 and hand.landmark[20].y < 0.2:
                    g1.play()
                    g1_played_pinky = True
                    g1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.66), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.76), int(image.shape[0] * 0.2)), played_color, -1) # H G
                
                # A1  
                if a1_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.77 and hand.landmark[20].x < 0.87 and hand.landmark[20].y < 0.2:
                    a1.play()
                    a1_played_pinky = True
                    a1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.77), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.87), int(image.shape[0] * 0.2)), played_color, -1) # C A
                
                # H1  
                if h1_played_pinky == False and hand.landmark[20].z < -0.08 and hand.landmark[20].x > 0.88 and hand.landmark[20].x < 0.98 and hand.landmark[20].y < 0.2:
                    h1.play()
                    h1_played_pinky = True
                    h1_played_hand = num
                    image = cv2.rectangle(image, (int(image.shape[1] * 0.88), int(image.shape[0] * 0.0)), (int(image.shape[1] * 0.98), int(image.shape[0] * 0.2)), played_color, -1) # D H

                
                # A0 released
                if a0_played_pinky == True and hand.landmark[20].z > -0.08 and a0_played_hand == num:
                    a0_played_pinky = False
                
                # H0 released
                if h0_played_pinky == True and hand.landmark[20].z > -0.08 and h0_played_hand == num:
                    h0_played_pinky = False
                
                # C1 released    
                if c1_played_pinky == True and hand.landmark[20].z > -0.08 and c1_played_hand == num:
                    c1_played_pinky = False
                
                # D1 released    
                if d1_played_pinky == True and hand.landmark[20].z > -0.08 and d1_played_hand == num:
                    d1_played_pinky = False
                
                # E1 released    
                if e1_played_pinky == True and hand.landmark[20].z > -0.08 and e1_played_hand == num:
                    e1_played_pinky = False
                
                # F1 released    
                if f1_played_pinky == True and hand.landmark[20].z > -0.08 and f1_played_hand == num:
                    f1_played_pinky = False
                
                # G1 released
                if g1_played_pinky == True and hand.landmark[20].z > -0.08 and g1_played_hand == num:
                    g1_played_pinky = False
                
                # A1 released    
                if a1_played_pinky == True and hand.landmark[20].z > -0.08 and a1_played_hand == num:
                    a1_played_pinky = False
                
                # H1 released    
                if h1_played_pinky == True and hand.landmark[20].z > -0.08 and h1_played_hand == num:
                    h1_played_pinky = False

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()