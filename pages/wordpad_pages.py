from assets import Item
from pages import paint_pages as paint
from utils import *


class MainPage:
    paint_btn = Item(path=os.path.join(os.getcwd(), 'assets', 'wp_paint_btn.png'),
                     area=((660, 50), (746, 160)),
                     title='wp_paint_btn')

    file_btn = Item(path=os.path.join(os.getcwd(), 'assets', 'wp_file_btn.png'),
                    area=((0, 20), (80, 64)),
                    title='wp_file_btn')

    file_save_as_btn = Item(path=os.path.join(os.getcwd(), 'assets', 'wp_file_save_as_btn.png'),
                            area=((0, 196), (250, 290)),
                            title='wp_file_save_as_btn')

    file_name_input = Item(path=os.path.join(os.getcwd(), 'assets', 'wp_file_name_input.png'),
                           offset=(75, 0),
                           title='wp_file_name_input')

    paint_created_image = Item(path=os.path.join(os.getcwd(), 'assets', 'wp_paint_btn.png'),
                               area=((0, 20), (60, 50)),
                               offset=(120, 170))

    def paste_paint_image(self):
        paint_btn_coords = try_find_on_screen(template=self.paint_btn.Image,
                                              area=self.paint_btn.Area,
                                              element_name=self.paint_btn.Title)

        if paint_btn_coords is None:
            return

        click_to_the_center(paint_btn_coords)
        return paint.MainPage()

    def count_to(self, to: int = 1):
        pyautogui.press('enter')
        indexes = [f"{x}. " for x in range(1, to + 1)]
        pyautogui.write('\n'.join(indexes))
        return self

    def remove_image(self):
        pyautogui.press('pgup', presses=3)
        pyautogui.press('del', presses=2)
        return self

    def save_file(self, path: str = 'document.txt'):
        file_btn_coords = try_find_on_screen(template=self.file_btn.Image,
                                             area=self.file_btn.Area,
                                             element_name=self.file_btn.Title)

        if file_btn_coords is None:
            return

        click_to_the_center(file_btn_coords)

        file_save_as_btn_coords = try_find_on_screen(template=self.file_save_as_btn.Image,
                                                     area=self.file_save_as_btn.Area,
                                                     element_name=self.file_save_as_btn.Title)

        if file_save_as_btn_coords is None:
            return

        click_to_the_center(file_save_as_btn_coords)
        clear_input()
        pyautogui.write(path)
        pyautogui.press('enter')
        return self
