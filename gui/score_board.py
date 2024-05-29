import customtkinter as ctk
from data.data_handler import fetch_scores, clear_scores


class ScoreBoard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color=("#CCCCCC", "#333333"))

        self.label = ctk.CTkLabel(self, text="Scores")
        self.label.grid(row=0, column=0)

        self.score_list = ctk.CTkTextbox(self, width=400, height=200)
        self.score_list.grid(row=1, column=1)

        self.clear_scores_button = ctk.CTkButton(self, text="Delete", command=self.clear_scores)
        self.clear_scores_button.grid(row=2, column=1)

        self.update_scores()

    def clear_scores(self):
        clear_scores()
        self.update_scores()

    def update_scores(self):
        self.score_list.delete("1.0", "end")
        scores = fetch_scores()
        for score in scores:
            self.score_list.insert("end", f"{score[1]} - {score[2]}: {score[3]}\n")
