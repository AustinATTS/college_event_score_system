import customtkinter as ctk
import tkinter as tk
from data.multiple_data_handler import fetch_scores
from data.solo_data_handler import solo_fetch_scores
from services.event_manager import add_event, clear_events, return_events
from config.config import SCREEN_SIZE

class EventDirectory(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Make the frame fill the parent widget
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.event_frame = ctk.CTkScrollableFrame(self, width=811, height=425)
        self.event_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        self.get_events()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def get_events(self):
        self.clear_frame(self.event_frame)
        clear_events()
        multiple_events = fetch_scores()
        solo_events = solo_fetch_scores()

        try:
            for multiple_event in multiple_events:
                if multiple_event[1] == "Individual":
                    add_event(multiple_event[11], multiple_event[12], multiple_event[3], multiple_event[13])
                    add_event(multiple_event[14], multiple_event[15], multiple_event[3], multiple_event[16])
                    add_event(multiple_event[17], multiple_event[18], multiple_event[3], multiple_event[19])
                    add_event(multiple_event[20], multiple_event[21], multiple_event[3], multiple_event[22])
                    add_event(multiple_event[23], multiple_event[24], multiple_event[3], multiple_event[25])

                elif multiple_event[1] == "Team":
                    add_event(multiple_event[11], multiple_event[12], multiple_event[5], multiple_event[13])
                    add_event(multiple_event[14], multiple_event[15], multiple_event[5], multiple_event[16])
                    add_event(multiple_event[17], multiple_event[18], multiple_event[5], multiple_event[19])
                    add_event(multiple_event[20], multiple_event[21], multiple_event[5], multiple_event[22])
                    add_event(multiple_event[23], multiple_event[24], multiple_event[5], multiple_event[25])

            for solo_event in solo_events:
                if solo_event[1] == "Individual":
                    add_event(solo_event[11], solo_event[12], solo_event[3], solo_event[13])

                elif solo_event[1] == "Team":
                    add_event(solo_event[11], solo_event[12], solo_event[5], solo_event[13])

            events = return_events()

            event_dict = {}
            for event in events:
                event_name, event_data = event.split(" - ", 1)
                event_type, participant_score = event_data.split(" : ", 1)
                if event_name not in event_dict:
                    event_dict[event_name] = [f"{event_name} - {event_type}"]

                event_dict[event_name].append(participant_score)

            position_id = 0

            max_width = 0

            for event_name, event_values in event_dict.items():
                try:
                    width = ctk.CTkOptionMenu(self.event_frame, values=event_values).winfo_reqwidth()
                    if width > max_width:
                        max_width = width
                except tk.TclError as e:
                    print(f"Error creating option menu for {event_name}: {e}")
                    continue

            for event_name, event_values in event_dict.items():
                try:
                    entry = ctk.CTkOptionMenu(self.event_frame, values=event_values, width=max_width)
                    row = position_id // 3
                    column = position_id % 3
                    entry.grid(row=row, column=column, padx=20, pady=(20, 10), sticky="nsew")
                    position_id += 1
                except tk.TclError as e:
                    print(f"Error placing option menu for {event_name}: {e}")
                    continue

        except Exception as e:
            print(f"An error occurred while fetching or displaying events: {e}")
