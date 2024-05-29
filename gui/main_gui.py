import customtkinter as ctk
from utils.image_loader import load_image
from utils.custom_font import CustomFont
from utils.customisation import change_appearance_event, change_scaling_event
from gui.score_entry import ScoreEntry
from gui.score_board import ScoreBoard
from gui.event_directory import EventDirectory
from data.data_handler import clear_scores


class MainGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        body = CustomFont("assets/fonts/Selawik.ttf", size=14, weight="bold").get_ctk_font()
        header = CustomFont("assets/fonts/SelawikBold.ttf", size=14, weight="bold").get_ctk_font()

        self.geometry(f"{1100}x{580}")
        self.title("College Event Score System")
        self.iconbitmap("assets/images/logo.ico")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.navigation_frame = ctk.CTkFrame(self, width=140, corner_radius=0, fg_color=("#CCCCCC", "#333333"))
        self.navigation_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.navigation_frame.rowconfigure(4, weight=1)

        self.logo = load_image("assets/images/banner.png", size=(200, 50))
        self.logo_label = ctk.CTkLabel(self.navigation_frame, text="", image=self.logo,
                                       compound="left", font=header)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.score_entry_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                font=header, text="Score Entry", fg_color="transparent",
                                                text_color=("grey10", "grey90"), hover_color=("grey70", "grey30"),
                                                anchor="w", command=self.score_entry_button_event)
        self.score_entry_button.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        self.score_board_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                font=header, text="Score Board", fg_color="transparent",
                                                text_color=("grey10", "grey90"), hover_color=("grey70", "grey30"),
                                                anchor="w", command=self.score_board_button_event)
        self.score_board_button.grid(row=2, column=0, sticky="ew", padx=20, pady=10)

        self.event_directory_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, font=header,
                                                    border_spacing=10, text="Event Directory", fg_color="transparent",
                                                    text_color=("grey10", "grey90"), hover_color=("grey70", "grey30"),
                                                    anchor="w", command=self.event_directory_button_event)
        self.event_directory_button.grid(row=3, column=0, sticky="ew", padx=20, pady=10)

        self.appearance_label = ctk.CTkLabel(self.navigation_frame, text="Appearance Mode:", anchor="w", font=header)
        self.appearance_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance = ctk.CTkOptionMenu(self.navigation_frame, font=header, values=["Light", "Dark", "System"],
                                            command=change_appearance_event, fg_color=("#0097F7", "#F76000"), button_color=("#0068AB", "#AB4200"), button_hover_color=("#00395F", "#5F2400"))
        self.appearance.grid(row=6, column=0, padx=20, pady=(10, 10), sticky="s")
        self.scaling_label = ctk.CTkLabel(self.navigation_frame, text="UI Scaling:", font=header, anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling = ctk.CTkOptionMenu(self.navigation_frame, font=header, values=["80%", "90%", "100%", "110%", "120%"],
                                         command=change_scaling_event, fg_color=("#0097F7", "#F76000"), button_color=("#0068AB", "#AB4200"), button_hover_color=("#00395F", "#5F2400"))
        self.scaling.grid(row=8, column=0, padx=20, pady=(10, 20), sticky="s")

        self.score_entry = ScoreEntry(self)
        self.score_entry.grid_columnconfigure(0, weight=1)

        self.score_board = ScoreBoard(self)

        self.event_directory = EventDirectory(self)

        self.select_page("score_entry")
        self.appearance.set("Light")
        self.scaling.set("100%")

    def select_page(self, name):
        self.score_entry_button.configure(fg_color=("grey75", "grey25") if name == "score_entry" else "transparent")
        self.score_board_button.configure(fg_color=("grey75", "grey25") if name == "score_board" else "transparent")
        self.event_directory_button.configure(fg_color=("grey75", "grey25") if name == "event_directory"
        else "transparent")

        if name == "score_entry":
            self.score_entry.grid(row=0, rowspan=100, column=1, sticky="nsew")
        else:
            self.score_entry.grid_forget()

        if name == "score_board":
            self.score_board.grid(row=0, rowspan=100, column=1, sticky="nsew")
        else:
            self.score_board.grid_forget()

        if name == "event_directory":
            self.event_directory.grid(row=0, rowspan=100, column=1, sticky="nsew")
        else:
            self.event_directory.grid_forget()

    def score_entry_button_event(self):
        self.select_page("score_entry")

    def score_board_button_event(self):
        self.select_page("score_board")

    def event_directory_button_event(self):
        self.select_page("event_directory")
