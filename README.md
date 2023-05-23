# Game-Bot-for-Autoclicking
This project is a Python-based game bot that automates gameplay by using image recognition and mouse clicking. The bot is designed to play a specific game by detecting and clicking on certain elements within the game window.

# Prerequisites
Before running the game bot, make sure you have the following dependencies installed:

* Python 3.x
* OpenCV (cv2) library
* PyAutoGUI library
* NumPy library
* PIL (Python Imaging Library) library


You can install these dependencies using pip, the Python package manager. Run the following command:
```
pip install opencv-python pyautogui numpy pillow
```
# Getting Started
To get started with the game bot, follow these steps:

1. Clone this repository to your local machine or download the source code files.

2. Prepare the game window region:

  - Identify the region of the game window on your screen. The game_region variable in the code represents the coordinates (left, top, right, bottom) of the game window.
  - Adjust the values of game_region according to your game window's position and size.
3. Select a kross_template image:

- In the kross_templates directory, place the template images of the krosses you want the bot to detect.
- The bot will prompt you to choose a kross_template image at runtime.
- Make sure the kross_template images have a format compatible with OpenCV (e.g., PNG, JPEG).
4. Prepare additional template images:

- You may need to create additional template images for other elements you want the bot to detect and interact with (e.g., left button, right button, coins, pause button).
- Place these template images in the respective directories and update the file paths in the code accordingly.
5. Adjust the settings:

- Modify the max_runtime variable to set the maximum runtime (in seconds) for the bot. After this duration, the bot will stop running.
- Customize any other settings or parameters in the code as per your requirements.
6. Run the bot:

- Open a terminal or command prompt and navigate to the project directory.
Execute the following command to run the bot:
```
python main.py
```
