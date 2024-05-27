import customtkinter as ctk
from data.data_handler import fetch_scores


class ScoreBoard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ctk.CTkLabel(self, text="Scores")

        self.score_list = ctk.CTkTextbox(self, width=400, height=200)

        self.update_scores()

    def update_scores(self):
        self.score_list.delete("1.0", "end")
        scores = fetch_scores()
        for score in scores:
            self.score_list.insert("end", f"{score[1]} - {score[2]}: {score[3]}\n")
