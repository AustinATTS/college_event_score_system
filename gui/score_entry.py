import customtkinter as ctk
from data.data_handler import insert_score


class ScoreEntry(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ctk.CTkLabel(self, text="Enter Score")

        self.participant_name_entry = ctk.CTkEntry(self, placeholder_text="Participant Name")

        self.event_name_entry = ctk.CTkEntry(self, placeholder_text="Event Name")

        self.score_entry = ctk.CTkEntry(self, placeholder_text="Score")

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_score)

    def submit_score(self):
        participant_name = self.participant_name_entry.get()
        event_name = self.event_name_entry.get()
        score = self.score_entry.get()
        if participant_name and event_name and score:
            insert_score(participant_name, event_name, int(score))
            self.participant_name_entry.delete(0, 'end')
            self.event_name_entry.delete(0, 'end')
            self.score_entry.delete(0, 'end')
            self.master.score_display.update_scores()
