Harry Potter's Invisible Cloak Project


This project implements a real-time "invisibility cloak" effect inspired by the one from the Harry Potter series, using Python and the OpenCV library. The concept is similar to a green screen, where a specific color (by default, a red object) is replaced with a pre-recorded background image. This creates the magical illusion that the object is transparent or invisible.

Features

Real-time video processing: The script processes video frames live from a camera.
Background capture: Automatically captures a static background image at startup for a seamless effect.
Customizable color detection: Easily switch the target color (e.g., from a deep red to a dark purple) by adjusting the HSV color values.
Full-screen display: The output window can be viewed in full-screen mode for an immersive experience.
Quit button: A simulated "Quit" button is included in the window to close the application with a mouse click.

Prerequisites

To run this project, you need to have Python and the following libraries installed:
opencv-python
numpy
You can install them using pip:
pip install opencv-python numpy


How to Use

Set up your camera:
The script is configured to use a mobile phone as an IP webcam.
Install an IP webcam app on your phone (e.g., "IP Webcam" on Android).
Connect your computer and your phone to the same Wi-Fi network.
Run the app and note the URL it provides (e.g., http://192.168.1.100:8080/video).

Update the code:
Open the invisible_cloak.py script.
Change the camera_url variable to the URL from your IP webcam app.

Run the script:

Execute the script from your terminal:
python invisible_cloak.py
When the script starts, it will capture the background for a few seconds. Step out of the camera's view during this time.
Once the background is captured, you can move back into the frame with your red cloak.

Quit the application:

Click the "Quit" button in the top-left corner of the window.
Alternatively, press the 'q' key on your keyboard.

Troubleshooting
Error: Could not open video device: Ensure your phone's camera app is running and your devices are on the same Wi-Fi network. Verify the URL is correct.

Color detection issues: If your cloak is not being replaced correctly, the HSV values might not match your lighting. Use a separate HSV color picker tool to find the optimal values for your specific cloak and lighting conditions.
