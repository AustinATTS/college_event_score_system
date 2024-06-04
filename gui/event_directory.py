import customtkinter as ctk
from data.multiple_data_handler import fetch_scores, clear_scores
from data.solo_data_handler import solo_fetch_scores, solo_clear_scores


class EventDirectory(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color=("#CCCCCC", "#333333"))

        self.team_frame = ctk.CTkFrame(self)
        self.team_frame.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.individual_frame = ctk.CTkFrame(self)
        self.individual_frame.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.team_update_list()
        self.individual_update_list()

    def team_clear_list(self):
        clear_scores()
        solo_clear_scores()
        self.team_update_list()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def individual_clear_list(self):
        clear_scores()
        solo_clear_scores()
        self.individual_update_list()

    def team_update_list(self):
        self.clear_frame(self.team_frame)
        self.team_title = ctk.CTkLabel(self.team_frame, text="Team Events")
        self.team_title.grid(row=0, column=0, padx=20, pady=(20, 10))
        events = fetch_scores()
        solo_events = solo_fetch_scores()
        for event in events:
            if event[1] == "Team":
                values = []
                self.entries = ctk.CTkOptionMenu(self.team_frame, values=values,
                                                 button_hover_color=("#0097F7", "#F76000"),
                                                 button_color=("#0097F7", "#F76000"), fg_color=("#0097F7", "#F76000"))
                self.entries.grid(row=event[0], column=0, padx=20, pady=(10, 10))
        for solo_event in solo_events:
            if solo_event[1] == "Team":
                values = []
                self.entries = ctk.CTkOptionMenu(self.team_frame, values=values,
                                                 button_hover_color=("#0097F7", "#F76000"),
                                                 button_color=("#0097F7", "#F76000"), fg_color=("#0097F7", "#F76000"))
                self.entries.grid(row=solo_event[0], column=0, padx=20, pady=(10, 10))

    def individual_update_list(self):
        self.clear_frame(self.individual_frame)
        self.individual_title = ctk.CTkLabel(self.individual_frame, text="Individual Events")
        self.individual_title.grid(row=0, column=0, padx=20, pady=(20, 10))
        events = fetch_scores()
        solo_events = solo_fetch_scores()
        for event in events:
            if event[1] == "Individual":
                values = []
                self.entries = ctk.CTkOptionMenu(self.individual_frame, values=values,
                                                 button_hover_color=("#0097F7", "#F76000"),
                                                 button_color=("#0097F7", "#F76000"),
                                                 fg_color=("#0097F7", "#F76000"))
                self.entries.grid(row=event[0], column=0, padx=20, pady=(10, 10))
            else:
                print("By God What The Fuck Have You Done No God No")
        for solo_event in solo_events:
            if solo_event[1] == "Individual":
                values = []
                self.entries = ctk.CTkOptionMenu(self.individual_frame, values=values,
                                                 button_hover_color=("#0097F7", "#F76000"),
                                                 button_color=("#0097F7", "#F76000"),
                                                 fg_color=("#0097F7", "#F76000"))
                self.entries.grid(row=solo_event[0], column=0, padx=20, pady=(10, 10))
            else:
                print("By God What The Fuck Have You Done No God No")
