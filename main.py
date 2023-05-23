import cv2
import pyautogui
import numpy as np
from PIL import ImageGrab
import time
import os

def grab_screen(bbox=None):
    img = ImageGrab.grab(bbox=bbox)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

def click_button(button_pos):
    x, y = button_pos
    button_x, button_y, _, _ = game_region
    pyautogui.click(button_x + x, button_y + y)

# Define the region of the game window
game_region = (655, 65, 1220, 1055)

# Prompt the user to select a kross_template image
kross_templates_dir = "image/krosses"
kross_templates = os.listdir(kross_templates_dir)
print("Available kross_template images:")
for i, template in enumerate(kross_templates):
    print(f"{i+1}. {template}")
selection = int(input("Enter the number corresponding to the desired kross_template image: "))
selected_template = kross_templates[selection - 1]

# Loading process of the template image
kross_template = cv2.imread(os.path.join(kross_templates_dir, selected_template), cv2.IMREAD_COLOR)
left_template = cv2.imread('image/left.png', cv2.IMREAD_COLOR)
right_template = cv2.imread('image/right.png', cv2.IMREAD_COLOR)
coin_template = cv2.imread('image/coin.png', cv2.IMREAD_COLOR)
pause_template = cv2.imread('image/pause.png', cv2.IMREAD_COLOR)
# Delaying 5 seconds of starting the program
time.sleep(5)

# Maximum runtime to 1 minute and 5 seconds (65 seconds)
max_runtime = 65

while True:
    # Start the timer for the current iteration
    start_time = time.time()

    while True:
        # Capture the game window screen
        img = grab_screen(bbox=game_region)
        img_draw = img.copy()

        # Finding positions of the images in the game window screen
        result_left = cv2.matchTemplate(img, left_template, cv2.TM_CCOEFF_NORMED)
        _, max_val_left, _, max_loc_left = cv2.minMaxLoc(result_left)

        result_right = cv2.matchTemplate(img, right_template, cv2.TM_CCOEFF_NORMED)
        _, max_val_right, _, max_loc_right = cv2.minMaxLoc(result_right)

        result_coin = cv2.matchTemplate(img, coin_template, cv2.TM_CCOEFF_NORMED)
        _, max_val_coin, _, max_loc_coin = cv2.minMaxLoc(result_coin)

        result_kross = cv2.matchTemplate(img, kross_template, cv2.TM_CCOEFF_NORMED)
        _, max_val_kross, _, max_loc_kross = cv2.minMaxLoc(result_kross)

        result_pause = cv2.matchTemplate(img, pause_template, cv2.TM_CCOEFF_NORMED)
        _, max_val_pause, _, max_loc_pause = cv2.minMaxLoc(result_pause)

        # Calculating the distances between the coin and the kross
        coin_x, coin_y = max_loc_coin
        kross_x, kross_y = max_loc_kross
        distance_left = coin_x - kross_x
        distance_right = kross_x - coin_x

        # Showing detected images with rectangles
        cv2.rectangle(img_draw, max_loc_left, (max_loc_left[0] + left_template.shape[1], max_loc_left[1] + left_template.shape[0]), (0, 0, 255), 2)
        cv2.rectangle(img_draw, max_loc_right, (max_loc_right[0] + right_template.shape[1], max_loc_right[1] + right_template.shape[0]), (0, 0, 255), 2)
        cv2.rectangle(img_draw, max_loc_coin, (max_loc_coin[0] + coin_template.shape[1], max_loc_coin[1] + coin_template.shape[0]), (0, 255, 0), 2)
        cv2.rectangle(img_draw, max_loc_kross, (max_loc_kross[0] + kross_template.shape[1], max_loc_kross[1] + kross_template.shape[0]), (255, 0, 0), 2)
        cv2.rectangle(img_draw, max_loc_pause, (max_loc_pause[0] + pause_template.shape[1], max_loc_pause[1] + pause_template.shape[0]), (0, 255, 255), 2)


        cv2.imshow("Screen", img_draw)

        if distance_left < distance_right:
            click_button(max_loc_left)
        else:
            click_button(max_loc_right)

        if cv2.waitKey(1) == ord('q') or time.time() - start_time > max_runtime:
            click_button(max_loc_pause)
            time.sleep(2)
            click_button((100, 820))
            time.sleep(3)
            click_button((100, 895))
            break

    # Delay for 20 sec before starting the next iteration
    time.sleep(20)
    click_button((400, 750))
cv2.destroyAllWindows()
