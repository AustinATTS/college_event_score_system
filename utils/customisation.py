import customtkinter as ctk

def change_appearance_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str, frame):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    try:
        ctk.set_window_scaling(new_scaling_float)
        ctk.set_widget_scaling(new_scaling_float)
    except:
        for widget in frame.winfo_children():
            width =   widget.cget("width")
            height = widget.cget("height")
            widget.configure(width=(width*new_scaling_float), height=(height*new_scaling_float))
