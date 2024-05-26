import pyglet


class FontLoader:
    @staticmethod
    def load_font(font_path):
        pyglet.font.add_file(font_path)
        font_name = pyglet.font.load(font_path).name
        return font_name
