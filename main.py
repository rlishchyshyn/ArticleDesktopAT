from dotenv import load_dotenv

from pages.wordpad_pages import MainPage
from utils import *

load_dotenv()

APP_PATH = os.getenv('APP_PATH')
APP_NAME = os.getenv('APP_NAME')

if __name__ == '__main__':
    start_process(APP_PATH, APP_NAME)
    time.sleep(1)

    wp = MainPage()

    wp.paste_paint_image() \
        .change_image_size() \
        .change_brush('brush_type_4') \
        .change_color('red') \
        .draw() \
        .save_and_go_back() \
        .count_to(42) \
        .remove_image() \
        .save_file(r'C:\Users\Admin\Desktop\DesktopAT\my_file')

    time.sleep(1)
    stop_process(APP_NAME)
