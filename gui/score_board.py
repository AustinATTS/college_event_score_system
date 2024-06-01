import customtkinter as ctk
from data.multiple_data_handler import fetch_scores, clear_scores
from data.solo_data_handler import solo_fetch_scores, solo_clear_scores


class ScoreBoard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color=("#CCCCCC", "#333333"))

        self.multiple_events = ctk.CTkFrame(self, width=240, height=450)
        self.multiple_events.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.score_list = ctk.CTkTextbox(self.multiple_events, width=400, height=200)
        self.score_list.grid(row=1, column=1)

        self.clear_scores_button = ctk.CTkButton(self.multiple_events, text="Delete", command=self.multiple_clear_scores)
        self.clear_scores_button.grid(row=2, column=1)

        self.solo_events = ctk.CTkFrame(self, width=240, height=450)
        self.solo_events.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.solo_score_list = ctk.CTkTextbox(self.solo_events, width=400, height=200)
        self.solo_score_list.grid(row=1, column=1)

        self.solo_clear_Score_button = ctk.CTkButton(self.solo_events, text="Delete", command=self.solo_clear_scores)
        self.solo_clear_Score_button.grid(row=2, column=1)

        self.multiple_update_scores()
        self.solo_update_scores()

    def multiple_clear_scores(self):
        clear_scores()
        self.multiple_update_scores()


    def solo_clear_scores(self):
        solo_clear_scores()
        self.solo_update_scores()

    def multiple_update_scores(self):
        self.score_list.delete("1.0", "end")
        scores = fetch_scores()
        for score in scores:
            if score[1] == "Individual":
                self.score_list.insert("end", f"{score[1]} - {score[2]}: {score[3]}\n")
            elif score[1] == "Team":
                self.score_list.insert("end", f"{score[1]} - {score[2]}: {score[3]}\n")
            else:
                print(f"What the fuck have you done")

    def solo_update_scores(self):
        self.solo_score_list.delete("1.0", "end")
        solo_scores = solo_fetch_scores()
        for solo_score in solo_scores:
            if solo_score[1] == "Individual":
                self.solo_score_list.insert("end", f"{solo_score[1]} - {solo_score[2]}: {solo_score[3]}\n")
            elif solo_score[1] == "Team":
                self.solo_score_list.insert("end", f"{solo_score[1]} - {solo_score[2]}: {solo_score[3]}\n")
            else:
                print(f"Solo What the fuck have you done")
