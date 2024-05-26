import customtkinter as ctk
from utils.custom_font import CustomFont
from gui.score_entry import ScoreEntry
from gui.score_display import ScoreDisplay
from data.data_handler import clear_scores


class MainWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Define the custom font
        custom_font = CustomFont("assets/fonts/Selawik.ttf", size=14, weight='bold').get_ctk_font()

        self.label = ctk.CTkLabel(self, text="College Event Score System", font=custom_font)
        self.label.pack(pady=10)

        self.score_entry = ScoreEntry(self)
        self.score_entry.pack(pady=10)

        self.score_display = ScoreDisplay(self)
        self.score_display.pack(pady=10)

        self.clear_button = ctk.CTkButton(self, text="Clear Scores", command=self.clear_scores)
        self.clear_button.pack(pady=10)

        self.load_data()

    def load_data(self):
        self.score_display.update_scores()

    def clear_scores(self):
        clear_scores()
        self.load_data()
