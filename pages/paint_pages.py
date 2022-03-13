from assets import Item
from pages import wordpad_pages as wordpad
from utils import *


class MainPage:
    brushes_list = Item(path=os.path.join(os.getcwd(), 'assets', 'p_brushes_list.png'),
                        offset=(0, 20),
                        title='p_brushes_list',
                        children=[
                            Item(offset=(0, 80), title='brush_type_0'),
                            Item(offset=(54, 80), title='brush_type_1'),
                            Item(offset=(108, 80), title='brush_type_2'),
                            Item(offset=(162, 80), title='brush_type_3'),
                            Item(offset=(0, 124), title='brush_type_4'),
                            Item(offset=(54, 124), title='brush_type_5'),
                            Item(offset=(108, 124), title='brush_type_6'),
                            Item(offset=(162, 124), title='brush_type_7'),
                            Item(offset=(0, 174), title='brush_type_8'),
                        ])

    colors_list = Item(path=os.path.join(os.getcwd(), 'assets', 'p_colors_list.png'),
                       title='p_colors_list',
                       children=[
                           Item(offset=(-64, -30), title='black'),
                           Item(offset=(-44, -30), title='gray'),
                           Item(offset=(-17, -30), title='dark_brown'),
                           Item(offset=(8, -30), title='red'),
                       ])

    change_size_btn = Item(path=os.path.join(os.getcwd(), 'assets', 'p_change_size_btn.png'),
                           title='p_change_size_btn')

    pixels_size_checkbox = Item(path=os.path.join(os.getcwd(), 'assets', 'p_pixel_size_btn.png'),
                                offset=(64, 15),
                                title='p_pixel_size_btn')

    change_width_input = Item(path=os.path.join(os.getcwd(), 'assets', 'p_width_size_input.png'),
                              offset=(75, 0),
                              title='p_width_size_input')

    file_btn = Item(path=os.path.join(os.getcwd(), 'assets', 'p_file_btn.png'),
                    offset=(0, 10),
                    title='p_file_btn')

    save_and_go_back_btn = Item(
        path=os.path.join(os.getcwd(), 'assets', 'p_save_and_go_back_btn.png'),
        title='p_save_and_go_back_btn')

    image2draw_start_position = (270, 410)
    figure_coords = [(30, 20), (40, -50)]

    def change_image_size(self, width: int = 100):
        change_size_btn_coords = try_find_on_screen(template=self.change_size_btn.Image,
                                                    area=self.change_size_btn.Area,
                                                    element_name=self.change_size_btn.Title)

        if change_size_btn_coords is None:
            return
        click_to_the_center(change_size_btn_coords)

        pixels_size_checkbox_coords = try_find_on_screen(template=self.pixels_size_checkbox.Image,
                                                         area=self.pixels_size_checkbox.Area,
                                                         element_name=self.pixels_size_checkbox.Title)

        if pixels_size_checkbox_coords is None:
            return

        click_to_the_center(pixels_size_checkbox_coords, offset=self.pixels_size_checkbox.Offset)

        change_width_input_coords = try_find_on_screen(template=self.change_width_input.Image,
                                                       area=self.change_width_input.Area,
                                                       element_name=self.change_width_input.Title)

        if change_width_input_coords is None:
            return

        click_to_the_center(change_width_input_coords, offset=self.change_width_input.Offset)

        clear_input()
        pyautogui.write(str(width))
        pyautogui.press('enter')

        return self

    def change_brush(self, brash_type='brush_type_0'):
        brushes_list_coords = try_find_on_screen(template=self.brushes_list.Image,
                                                 area=self.brushes_list.Area,
                                                 element_name=self.brushes_list.Title)

        if brushes_list_coords is None:
            return

        click_to_the_center(brushes_list_coords, offset=self.brushes_list.Offset)

        brash_item = self.brushes_list.get_children(brash_type)
        click_to_the_center(brushes_list_coords, offset=brash_item.Offset)

        return self

    def change_color(self, color='black'):
        colors_list_coords = try_find_on_screen(template=self.colors_list.Image,
                                                area=self.colors_list.Area,
                                                element_name=self.colors_list.Title)

        if colors_list_coords is None:
            return

        color_item = self.colors_list.get_children(color)
        click_to_the_center(colors_list_coords, offset=color_item.Offset)

        return self

    def draw(self):
        x, y = self.image2draw_start_position
        pyautogui.moveTo(x, y)
        for pos in self.figure_coords:
            pyautogui.drag(pos[0], pos[1], 0.1, button='left')
        return self

    def save_and_go_back(self):
        file_btn_coords = try_find_on_screen(template=self.file_btn.Image,
                                             area=self.file_btn.Area,
                                             element_name=self.file_btn.Title)

        if file_btn_coords is None:
            return

        click_to_the_center(file_btn_coords, offset=self.file_btn.Offset)

        save_and_go_back_btn_coords = try_find_on_screen(template=self.save_and_go_back_btn.Image,
                                                         area=self.save_and_go_back_btn.Area,
                                                         element_name=self.save_and_go_back_btn.Title)

        if save_and_go_back_btn_coords is None:
            return

        click_to_the_center(save_and_go_back_btn_coords)

        return wordpad.MainPage()
