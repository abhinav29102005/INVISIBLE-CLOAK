import cv2
import numpy as np
import time

camera_url = 'ip-address-from-ipwebcam-app/video'
cap = cv2.VideoCapture(camera_url)

if not cap.isOpened():
    print(f"Error: Could not open video device at {camera_url}.")
    print("Please check if your mobile phone is on the same network and the URL is correct.")
    exit()

print("Setting up the camera for the background capture. Please do not move.")

background = None
for i in range(60):
    ret, frame = cap.read()
    if ret:
        background = frame
    else:
        print("Error: Failed to capture background frame during setup.")
        cap.release()
        cv2.destroyAllWindows()
        exit()

if background is None:
    print("Error: Could not capture a valid background image. Exiting.")
    cap.release()
    cv2.destroyAllWindows()
    exit()

print("Background captured! You can now use the red cloak.")
time.sleep(3)

background = cv2.resize(background, (640, 480))

cv2.namedWindow("Invisible Cloak", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Invisible Cloak", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

quit_program = False

def close_button_callback(event, x, y, flags, param):
    global quit_program
    button_x1, button_y1 = 10, 10
    button_x2, button_y2 = 100, 50
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if button_x1 <= x <= button_x2 and button_y1 <= y <= button_y2:
            quit_program = True

cv2.setMouseCallback("Invisible Cloak", close_button_callback)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        print("Error: Failed to capture live frame.")
        break
    
    img = cv2.resize(img, (640, 480))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    final_mask = mask1 + mask2

    kernel = np.ones((5, 5), np.uint8)
    final_mask = cv2.morphologyEx(final_mask, cv2.MORPH_OPEN, kernel, iterations=3)
    final_mask = cv2.dilate(final_mask, kernel, iterations=2)

    inverse_mask = cv2.bitwise_not(final_mask)

    foreground = cv2.bitwise_and(img, img, mask=inverse_mask)

    cloak_part = cv2.bitwise_and(background, background, mask=final_mask)

    result = cv2.addWeighted(foreground, 1.0, cloak_part, 1.0, 0)
    
    cv2.rectangle(result, (10, 10), (100, 50), (0, 0, 255), -1)
    cv2.putText(result, "Quit", (25, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Invisible Cloak", result)

    if quit_program or (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
