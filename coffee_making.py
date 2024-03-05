import mediapipe as mp
import cv2
import numpy as np
import os
import numpy as np
from PIL import Image

from pygame import mixer

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

# overlay = cv2.imread('full_portafilter-removebg-preview.png', cv2.IMREAD_UNCHANGED)
overlay = Image.open("full_portafilter-removebg-preview.png")
coffee_machine = Image.open("coffeemachine.png")
coffee_machine = coffee_machine.transpose(Image.FLIP_LEFT_RIGHT)


def remove_background(frame, bg_subtractor):
    fg_mask = bg_subtractor.apply(frame)
    result = cv2.bitwise_and(frame, frame, mask=fg_mask)
    return result

bg_subtractor = cv2.createBackgroundSubtractorMOG2()

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()
        
        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip on horizontal
        image = cv2.flip(image, 1)

        # image = remove_background(image, bg_subtractor)
        
        # Set flag
        image.flags.writeable = False
        
        # Detections
        results = hands.process(image)
        
        # Set flag to true
        image.flags.writeable = True
        
        # RGB 2 BGR
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )

                # Render images
                y_offset = int(hand.landmark[5].y * image.shape[0])
                x_offset = int(hand.landmark[5].x * image.shape[1])

            # image[y_offset:y_offset + overlay.shape[0], x_offset:x_offset + overlay.shape[1]] = overlay
            # image[y_offset:y_offset + overlay.shape[0], x_offset:x_offset + int(overlay.shape[1] / 2)] = overlay[:, :int(overlay.shape[1] / 2), :]

            # Open with PILLOW
            image = Image.fromarray(image)
            
            # Paste image on top
            image.paste(overlay, (x_offset - overlay.size[0], y_offset), overlay)

            image_np = np.array(image)

            image = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(image)
        image.paste(coffee_machine, (0, int(image.size[1] - coffee_machine.size[1])), coffee_machine)
        image_np = np.array(image)
        image = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow("Let's brew some coffee", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()