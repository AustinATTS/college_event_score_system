import pyglet
import os
import customtkinter as ctk


class CustomFont:
    def __init__(self, font_path, size=12, weight='normal'):
        self.font_path = font_path
        self.size = size
        self.weight = weight
        self.font_name = self.load_font()

    def load_font(self):
        # Register the font with pyglet
        font_name = os.path.basename(self.font_path).split('.')[0]
        pyglet.font.add_file(self.font_path)
        return font_name

    def get_ctk_font(self):
        # Map weight to tkinter acceptable values
        weight_map = {
            'normal': 'normal',
            'bold': 'bold'
        }
        return ctk.CTkFont(family=self.font_name, size=self.size, weight=weight_map.get(self.weight, 'normal'))
