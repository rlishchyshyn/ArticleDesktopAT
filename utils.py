import os
import subprocess
import threading
import time

import cv2
import numpy as np
import pyautogui
import win32api
import win32con
from pynput.keyboard import Key, Controller

from logs import logger


def find_coords(image, template, threshold=0.9, method=cv2.TM_CCOEFF_NORMED, mask=None):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, method, mask)

    loc = np.where(res >= threshold)
    if np.any(loc):
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            y, x = np.amin(loc[0]), np.amin(loc[1])
        else:
            y, x = np.amax(loc[0]), np.amax(loc[1])

        return (x, y), (x + w, y + h)


def try_find_on_screen(template, area=None, mask=None, threshold=0.9, method=cv2.TM_CCOEFF_NORMED, attempts=3,
                       element_name=""):
    image = None
    coords = None

    for attempt in range(0, attempts):
        image = get_screen_image()

        if area is not None:
            image = image[area[0][1]:area[1][1], area[0][0]:area[1][0]]

        coords = find_coords(image, template, threshold, method, mask)
        if coords is None:
            time.sleep(0.5 * (attempt + 1))
        else:
            break

    debug_env = os.getenv("DEBUG") if os.getenv("DEBUG") is not None else ""
    debug = True if debug_env.lower() in ["true", "t", "1"] else False

    if debug:
        th = threading.Thread(target=record_logs, args=(image, coords, element_name))
        th.start()
        th.join()

    if coords is not None and area is not None:
        coords = ((coords[0][0] + area[0][0], coords[0][1] + area[0][1]),
                  (coords[1][0] + area[0][0], coords[1][1] + area[0][1]))

    return coords


def record_logs(image, coords, element_name):
    ts = time.time()

    if coords is not None:
        cv2.rectangle(image, coords[0], coords[1], (0, 0, 255), 2)

    if coords is not None:
        cv2.imwrite(f"logs/INFO_{element_name}_{ts}.png", image)
        logger.info(
            f"Template '{element_name}' found on screen. "
            f"Screen image - '{os.path.join(os.path.dirname(os.path.abspath('__file__')), 'logs', f'INFO_{element_name}_{ts}.png')}'")
    else:
        cv2.imwrite(f"logs/ERROR_{element_name}_{ts}.png", image)
        logger.error(
            f"Template '{element_name}' not found on screen. "
            f"Screen image - '{os.path.join(os.path.dirname(os.path.abspath('__file__')), 'logs', f'ERROR_{element_name}_{ts}.png')}'")


def find_center(coords):
    x_center = (coords[0][0] + coords[1][0]) // 2
    y_center = (coords[0][1] + coords[1][1]) // 2
    return x_center, y_center


def get_screen_image():
    frame = pyautogui.screenshot()
    return cv2.cvtColor(np.uint8(frame), cv2.COLOR_RGB2BGR)


def click(x, y, right=False, timeout=0.3):
    pyautogui.moveTo(x, y)
    if right:
        pyautogui.click(x, y, button="right")
    else:
        pyautogui.click(x, y)
    time.sleep(timeout)
    pyautogui.moveTo(1, 1)


def click_to_the_center(coords, right=False, timeout=0.3, offset=(0, 0)):
    x_center, y_center = find_center(coords)
    click(x_center + offset[0], y_center + offset[1], right, timeout)


def scroll(clicks=0, delta_x=0, delta_y=0, delay_between_ticks=0.0):
    if clicks > 0:
        increment = win32con.WHEEL_DELTA
    else:
        increment = win32con.WHEEL_DELTA * -1

    for _ in range(abs(clicks)):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, delta_x, delta_y, increment, 0)
        time.sleep(delay_between_ticks)


def move_to_center(coords, offset=(0, 0), timeout=0.2, tween=pyautogui.easeInQuad):
    x_center, y_center = find_center(coords)
    pyautogui.moveTo(x_center + offset[0], y_center + offset[1], timeout, tween)


def clear_input():
    keyboard = Controller()
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)


def start_process(current_dir, name):
    subprocess.Popen(os.path.join(current_dir, name))


def stop_process(name):
    os.system(f"taskkill /f /im {name}")
