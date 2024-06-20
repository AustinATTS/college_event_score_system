import customtkinter as ctk
from data.multiple_data_handler import fetch_scores, clear_scores
from data.solo_data_handler import solo_fetch_scores, solo_clear_scores
from services.score_calculator import multiple_calculate_score, solo_calculate_score
from services.score_calculator import multiple_display_score, solo_display_score
from config.config import SCREEN_SIZE


class ScoreBoard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color=("#CCCCCC", "#333333"))

        self.multiple_events = ctk.CTkScrollableFrame(self, width=360, height=425)
        self.multiple_events.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.solo_events = ctk.CTkScrollableFrame(self, width=360, height=425)
        self.solo_events.grid(row=0, column=1, padx=20, pady=(20, 10))

        self.multiple_update_scores()
        self.solo_update_scores()

    def multiple_clear_scores(self):
        clear_scores()
        self.multiple_update_scores()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def solo_clear_scores(self):
        solo_clear_scores()
        self.solo_update_scores()

    def multiple_update_scores(self):
        self.clear_frame(self.multiple_events)
        self.multiple_title = ctk.CTkLabel(self.multiple_events, text="ScoreBoard For Multiple Events")
        self.multiple_title.grid(row=0, column=0, padx=20, pady=(20, 10))
        scores = fetch_scores()
        for score in scores:
            if score[1] == "Individual":
                values = [f"{str(score[2])} - {score[5]}: {multiple_calculate_score(int(score[13]), int(score[16]), int(score[19]), int(score[22]), int(score[25]))}",
                          f"{score[11]} - {score[12]}; {str(score[13])}",
                          f"{score[14]} - {score[15]}; {str(score[16])}",
                          f"{score[17]} - {score[18]}; {str(score[19])}",
                          f"{score[20]} - {score[21]}; {str(score[22])}",
                          f"{score[23]} - {score[24]}; {str(score[25])}"]
                self.entries = ctk.CTkOptionMenu(self.multiple_events, values=values,
                                                 button_hover_color=("#0097F7", "#F76000"),
                                                 button_color=("#0097F7", "#F76000"), fg_color=("#0097F7", "#F76000"))
                position = 0
                for i in range(20):
                    widgets = self.multiple_events.grid_slaves(row=(
                            multiple_display_score(int(score[13]), int(score[16]), int(score[19]), int(score[22]), int(score[25])) + position), column=0)
                    if widgets:
                        position += 1

                entries.grid(row=(multiple_display_score(int(score[13]), int(score[16]), int(score[19]), int(score[22]), int(score[25])) + position), column=0, padx=20, pady=(10, 10))

            elif score[1] == "Team":
                values = [f"{str(score[4])} - {score[5]}: {multiple_calculate_score(int(score[13]), int(score[16]), int(score[19]), int(score[22]), int(score[25]))}",
                          f"{score[6]} - {score[7]} - {score[8]} - {score[9]} - {score[10]}",
                          f"{score[11]} - {score[12]}; {str(score[13])}",
                          f"{score[14]} - {score[15]}; {str(score[16])}",
                          f"{score[17]} - {score[18]}; {str(score[19])}",
                          f"{score[20]} - {score[21]}; {str(score[22])}",
                          f"{score[23]} - {score[24]}; {str(score[25])}"]
                entries = ctk.CTkOptionMenu(self.multiple_events, values=values, fg_color=("#0097F7", "#F76000"),
                                            hover_color=("#0068AB", "#AB4200"))
                position = 0
                for i in range(20):
                    widgets = self.multiple_events.grid_slaves(row=(multiple_display_score(int(score[13]), int(score[16]), int(score[19]), int(score[22]), int(score[25])) + position), column=0)
                    if widgets:
                        position += 1

                entries.grid(row=(multiple_display_score(int(score[13]), int(score[16]), int(score[19]), int(score[22]), int(score[25])) + position), column=0, padx=20, pady=(10, 10))
            else:
                print(f"What the fuck have you done")

        self.clear_scores_button = ctk.CTkButton(self.multiple_events, text="Delete",
                                                 command=self.multiple_clear_scores, fg_color=("#0097F7", "#F76000"),
                                                 hover_color=("#0068AB", "#AB4200"))
        self.clear_scores_button.grid(row=2, column=1)

    def solo_update_scores(self):
        self.clear_frame(self.solo_events)
        self.solo_title = ctk.CTkLabel(self.solo_events, text="ScoreBoard For Solo Events")
        self.solo_title.grid(row=0, column=0, padx=20, pady=(20, 10))
        solo_scores = solo_fetch_scores()
        for solo_score in solo_scores:
            if solo_score[1] == "Individual":
                values = [f"{str(solo_score[2])} - {solo_score[5]}: {solo_calculate_score(int(solo_score[13]))}",
                          f"{solo_score[11]} - {solo_score[12]}; {str(solo_score[13])}"]
                entries = ctk.CTkOptionMenu(self.solo_events, values=values, button_hover_color=("#0097F7", "#F76000"),
                                            button_color=("#0097F7", "#F76000"), fg_color=("#0097F7", "#F76000"))
                position = 0
                for i in range(20):
                    widgets = self.solo_events.grid_slaves(row=(solo_display_score(int(solo_score[13])) + position), column=0)
                    if widgets:
                        position += 1

                entries.grid(row=(solo_display_score(int(solo_score[13])) + position), column=0, padx=20, pady=(10, 10))

            elif solo_score[1] == "Team":
                values = [f"{str(solo_score[4])} - {solo_score[5]}: {solo_calculate_score(int(solo_score[13]))}",
                          f"{solo_score[6]} - {solo_score[7]} - {solo_score[8]} - {solo_score[9]} - {solo_score[10]}",
                          f"{solo_score[11]} - {solo_score[12]}; {str(solo_score[13])}"]
                entries = ctk.CTkOptionMenu(self.solo_events, values=values, button_hover_color=("#0097F7", "#F76000"),
                                            button_color=("#0097F7", "#F76000"), fg_color=("#0097F7", "#F76000"))
                position = 0
                for i in range(20):
                    widgets = self.solo_events.grid_slaves(row=(solo_display_score(int(solo_score[13])) + position), column=0)
                    if widgets:
                        position += 1

                entries.grid(row=(solo_display_score(int(solo_score[13])) + position), column=0, padx=20, pady=(10, 10))

            else:
                print(f"Solo What the fuck have you done")

        self.solo_clear_Score_button = ctk.CTkButton(self.solo_events, text="Delete", command=self.solo_clear_scores,
                                                     fg_color=("#0097F7", "#F76000"),
                                                     hover_color=("#0068AB", "#AB4200"))
        self.solo_clear_Score_button.grid(row=2, column=1)
