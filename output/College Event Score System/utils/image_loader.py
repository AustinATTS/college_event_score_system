import customtkinter as ctk
from PIL import Image
import os


def load_image(image_path, size=(200, 200)):

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' not found.")

    return ctk.CTkImage(light_image=Image.open(image_path),
                        dark_image=Image.open(image_path),
                        size=size)

