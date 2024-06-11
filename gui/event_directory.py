import customtkinter as ctk
from data.multiple_data_handler import fetch_scores
from data.solo_data_handler import solo_fetch_scores
from services.event_manager import add_event, clear_events, get_events
from config.config import SCREEN_SIZE


class EventDirectory(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color=("#CCCCCC", "#333333"))

        self.event_frame = ctk.CTkScrollableFrame(self)
        self.event_frame.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.get_events()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def get_events(self):
        self.clear_frame(self.event_frame)
        clear_events()
        multiple_events = fetch_scores()
        solo_events = solo_fetch_scores()

        for multiple_event in multiple_events:
            add_event(multiple_event[5])
            add_event(multiple_event[5])
            add_event(multiple_event[5])
            add_event(multiple_event[5])
            add_event(multiple_event[5])

        for solo_event in solo_events:
            add_event(solo_event[5])

        events = get_events()

        for event in events:
            entry = ctk.CTkLabel(self.event_frame, text=event)
            entry.grid(row=0, column=0, padx=20, pady=(20, 10))

