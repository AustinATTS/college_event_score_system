import customtkinter as ctk
from data.data_handler import insert_score


class ScoreEntry(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.participant_type = ctk.CTkTabview(self)
        self.participant_type.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.participant_type.add("Individual")
        self.participant_type.add("Team")

        self.individual_id_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                placeholder_text="Participant ID")
        self.individual_id_entry.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.individual_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                  placeholder_text="Participant Name")
        self.individual_name_entry.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.event_one_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"), placeholder_text="Event Name")
        self.event_one_name_entry.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.event_one_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"), placeholder_text="Score")
        self.event_one_rank_entry.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.event_two_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"), placeholder_text="Event Name")
        self.event_two_name_entry.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.event_two_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"), placeholder_text="Score")
        self.event_two_rank_entry.grid(row=5, column=0, padx=20, pady=(10, 20))

        self.event_three_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                   placeholder_text="Event Name")
        self.event_three_name_entry.grid(row=0, column=1, padx=20, pady=(10, 10))
        self.event_three_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"), placeholder_text="Score")
        self.event_three_rank_entry.grid(row=1, column=1, padx=20, pady=(10, 10))

        self.event_four_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                  placeholder_text="Event Name")
        self.event_four_name_entry.grid(row=2, column=1, padx=20, pady=(10, 10))
        self.event_four_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"), placeholder_text="Score")
        self.event_four_rank_entry.grid(row=3, column=1, padx=20, pady=(10, 10))

        self.event_five_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                  placeholder_text="Event Name")
        self.event_five_name_entry.grid(row=4, column=1, padx=20, pady=(10, 10))
        self.event_five_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"), placeholder_text="Score")
        self.event_five_rank_entry.grid(row=5, column=1, padx=20, pady=(10, 20))

        self.submit_button = ctk.CTkButton(self.participant_type.tab("Individual"), text="Submit",
                                           command=self.submit_score)
        self.submit_button.grid(row=6, column=0, columnspan=2, padx=20, pady=(10, 20))

    def submit_score(self):
        individual_id = self.individual_id_entry.get()
        individual_name = self.individual_name_entry.get()
        event_one_name = self.event_one_name_entry.get()
        event_one_rank = self.event_one_rank_entry.get()
        event_two_name = self.event_two_name_entry.get()
        event_two_rank = self.event_two_rank_entry.get()
        event_three_name = self.event_three_name_entry.get()
        event_three_rank = self.event_three_rank_entry.get()
        event_four_name = self.event_four_name_entry.get()
        event_four_rank = self.event_four_rank_entry.get()
        event_five_name = self.event_five_name_entry.get()
        event_five_rank = self.event_five_rank_entry.get()
        if (individual_id and individual_name and event_one_name and event_one_rank and event_two_name and event_two_rank and event_three_name and event_three_rank and event_four_name and event_four_rank and event_five_name and event_five_rank):
            insert_score(individual_id, individual_name, event_one_name, int(event_one_rank), event_two_name, int(event_two_rank), event_three_name, int(event_three_rank), event_four_name, int(event_four_rank), event_five_name, int(event_five_rank))
            self.individual_id_entry.delete(0, 'end')
            self.individual_name_entry.delete(0, 'end')
            self.event_one_name_entry.delete(0, 'end')
            self.event_one_rank_entry.delete(0, 'end')
            self.event_two_name_entry.delete(0, 'end')
            self.event_two_rank_entry.delete(0, 'end')
            self.event_three_name_entry.delete(0, 'end')
            self.event_three_rank_entry.delete(0, 'end')
            self.event_four_name_entry.delete(0, 'end')
            self.event_four_rank_entry.delete(0, 'end')
            self.event_five_name_entry.delete(0, 'end')
            self.event_five_rank_entry.delete(0, 'end')
            self.master.score_board.update_scores()
