import _tkinter
import customtkinter as ctk

def change_appearance_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    try:
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        ctk.set_window_scaling(new_scaling_float)
    except _tkinter.TclError as e:
        print(f"Error changing scaling: {e}")
    except ValueError as e:
        print(f"Invalid scaling value provided: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
