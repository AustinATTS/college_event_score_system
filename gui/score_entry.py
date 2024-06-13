import customtkinter as ctk
#from utils.custom_font import CustomFont
import gui.main_gui
from data.multiple_data_handler import insert_score
from data.solo_data_handler import solo_insert_score
from config.config import SCREEN_SIZE


class ScoreEntry(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        #header = CustomFont("assets/fonts/SelawikBold.ttf", size=14, weight="bold").get_ctk_font()
        #body = CustomFont("assets/fonts/Selawik.ttf", size=14, weight="normal").get_ctk_font()
        #submit = CustomFont("assets/fonts/SelawikBold.ttf", size=14, weight="bold").get_ctk_font()
        header = ctk.CTkFont(size=14)
        body = ctk.CTkFont(size=14)
        submit = ctk.CTkFont(size=14)



        self.configure(corner_radius=0, fg_color=("#CCCCCC", "#333333"))

        self.participant_type = ctk.CTkTabview(self, width=250, command=self.update_screen_event,
                                               segmented_button_selected_color=("#0097F7", "#F76000"),
                                               segmented_button_selected_hover_color=("#0068AB", "#AB4200"),
                                               segmented_button_unselected_color=("#CCCCCC", "#333333"),
                                               segmented_button_unselected_hover_color=("#A6A6A6", "#0D0D0D"),
                                               segmented_button_fg_color=("#CCCCCC", "#333333"),
                                               text_color=("#333333", "#CCCCCC"))
        self.participant_type.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.participant_type.add("Individual")
        self.participant_type.add("Team")

        self.individual_id_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                placeholder_text="Participant ID", font=body)
        self.individual_id_entry.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.individual_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                  placeholder_text="Participant Name", font=body)
        self.individual_name_entry.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.individual_event_one_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                            placeholder_text="Event Name", font=body)
        self.individual_event_one_name_entry.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.individual_event_one_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Individual"),
                                                       values=["Academic", "Sporting"],
                                                       button_color=("#A6A6A6", "#0D0D0D"),
                                                       button_hover_color=("#808080", "#000000"), font=body)
        self.individual_event_one_type_combobox.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.individual_event_one_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                            placeholder_text="Score", font=body)
        self.individual_event_one_rank_entry.grid(row=5, column=0, padx=20, pady=(10, 20))

        self.individual_event_two_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                            placeholder_text="Event Name", font=body)
        self.individual_event_two_name_entry.grid(row=0, column=1, padx=20, pady=(20, 10))
        self.individual_event_two_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Individual"),
                                                       values=["Academic", "Sporting"],
                                                       button_color=("#A6A6A6", "#0D0D0D"),
                                                       button_hover_color=("#808080", "#000000"), font=body)
        self.individual_event_two_type_combobox.grid(row=1, column=1, padx=20, pady=(10, 10))
        self.individual_event_two_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                            placeholder_text="Score", font=body)
        self.individual_event_two_rank_entry.grid(row=2, column=1, padx=20, pady=(10, 10))

        self.individual_event_three_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                   placeholder_text="Event Name", font=body)
        self.individual_event_three_name_entry.grid(row=3, column=1, padx=20, pady=(10, 10))
        self.individual_event_three_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Individual"),
                                                         values=["Academic", "Sporting"],
                                                         button_color=("#A6A6A6", "#0D0D0D"),
                                                         button_hover_color=("#808080", "#000000"), font=body)
        self.individual_event_three_type_combobox.grid(row=4, column=1, padx=20, pady=(10, 10))
        self.individual_event_three_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                              placeholder_text="Score", font=body)
        self.individual_event_three_rank_entry.grid(row=5, column=1, padx=20, pady=(10, 20))

        self.individual_event_four_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                  placeholder_text="Event Name", font=body)
        self.individual_event_four_name_entry.grid(row=0, column=2, padx=20, pady=(20, 10))
        self.individual_event_four_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Individual"),
                                                        values=["Academic", "Sporting"],
                                                        button_color=("#A6A6A6", "#0D0D0D"),
                                                        button_hover_color=("#808080", "#000000"), font=body)
        self.individual_event_four_type_combobox.grid(row=1, column=2, padx=20, pady=(10, 10))
        self.individual_event_four_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                  placeholder_text="Score", font=body)
        self.individual_event_four_rank_entry.grid(row=2, column=2, padx=20, pady=(10, 10))

        self.individual_event_five_name_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                  placeholder_text="Event Name", font=body)
        self.individual_event_five_name_entry.grid(row=3, column=2, padx=20, pady=(10, 10))
        self.individual_event_five_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Individual"),
                                                        values=["Academic", "Sporting"],
                                                        button_color=("#A6A6A6", "#0D0D0D"),
                                                        button_hover_color=("#808080", "#000000"), font=body)
        self.individual_event_five_type_combobox.grid(row=4, column=2, padx=20, pady=(10, 10))
        self.individual_event_five_rank_entry = ctk.CTkEntry(self.participant_type.tab("Individual"),
                                                             placeholder_text="Score", font=body)
        self.individual_event_five_rank_entry.grid(row=5, column=2, padx=20, pady=(10, 20))

        self.submit_button = ctk.CTkButton(self.participant_type.tab("Individual"), text="Submit",
                                           command=self.submit_score, fg_color=("#0097F7", "#F76000"),
                                           hover_color=("#0068AB", "#AB4200"), font=submit, height=68, width=499)
        self.submit_button.grid(row=6, column=0, columnspan=3, padx=20, pady=(10, 20))

        self.team_id_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Team ID", font=body)
        self.team_id_entry.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.team_name_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Team Name", font=body)
        self.team_name_entry.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.team_member_one_entry = ctk.CTkEntry(self.participant_type.tab("Team"),
                                                  placeholder_text="Team Member Name", font=body)
        self.team_member_one_entry.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.team_member_two_entry = ctk.CTkEntry(self.participant_type.tab("Team"),
                                                  placeholder_text="Team Member Name", font=body)
        self.team_member_two_entry.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.team_member_three_entry = ctk.CTkEntry(self.participant_type.tab("Team"),
                                                    placeholder_text="Team Member Name", font=body)
        self.team_member_three_entry.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.team_member_four_entry = ctk.CTkEntry(self.participant_type.tab("Team"),
                                                   placeholder_text="Team Member Name", font=body)
        self.team_member_four_entry.grid(row=5, column=0, padx=20, pady=(10, 10))
        self.team_member_five_entry = ctk.CTkEntry(self.participant_type.tab("Team"),
                                                   placeholder_text="Team Member Name", font=body)
        self.team_member_five_entry.grid(row=6, column=0, padx=20, pady=(10, 20))

        self.team_event_one_name_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Event Name",
                                                 font=body)
        self.team_event_one_name_entry.grid(row=0, column=1, padx=20, pady=(20, 10))
        self.team_event_one_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Team"),
                                                       values=["Academic", "Sporting"],
                                                       button_color=("#A6A6A6", "#0D0D0D"),
                                                       button_hover_color=("#808080", "#000000"), font=body)
        self.team_event_one_type_combobox.grid(row=1, column=1, padx=20, pady=(10, 10))
        self.team_event_one_rank_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Score",
                                                      font=body)
        self.team_event_one_rank_entry.grid(row=2, column=1, padx=20, pady=(10, 10))

        self.team_event_two_name_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Event Name",
                                                 font=body)
        self.team_event_two_name_entry.grid(row=3, column=1, padx=20, pady=(10, 10))
        self.team_event_two_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Team"),
                                                       values=["Academic", "Sporting"],
                                                       button_color=("#A6A6A6", "#0D0D0D"),
                                                       button_hover_color=("#808080", "#000000"), font=body)
        self.team_event_two_type_combobox.grid(row=4, column=1, padx=20, pady=(10, 10))
        self.team_event_two_rank_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Score",
                                                      font=body)
        self.team_event_two_rank_entry.grid(row=5, column=1, padx=20, pady=(10, 10))

        self.team_event_three_name_entry = ctk.CTkEntry(self.participant_type.tab("Team"),
                                                        placeholder_text="Event Name", font=body)
        self.team_event_three_name_entry.grid(row=0, column=2, padx=20, pady=(20, 10))
        self.team_event_three_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Team"),
                                                         values=["Academic", "Sporting"],
                                                         button_color=("#A6A6A6", "#0D0D0D"),
                                                         button_hover_color=("#808080", "#000000"), font=body)
        self.team_event_three_type_combobox.grid(row=1, column=2, padx=20, pady=(10, 10))
        self.team_event_three_rank_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Score",
                                                   font=body)
        self.team_event_three_rank_entry.grid(row=2, column=2, padx=20, pady=(10, 10))

        self.team_event_four_name_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Event Name",
                                                  font=body)
        self.team_event_four_name_entry.grid(row=3, column=2, padx=20, pady=(10, 10))
        self.team_event_four_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Team"),
                                                        values=["Academic", "Sporting"],
                                                        button_color=("#A6A6A6", "#0D0D0D"),
                                                        button_hover_color=("#808080", "#000000"), font=body)
        self.team_event_four_type_combobox.grid(row=4, column=2, padx=20, pady=(10, 10))
        self.team_event_four_rank_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Score",
                                                  font=body)
        self.team_event_four_rank_entry.grid(row=5, column=2, padx=20, pady=(10, 10))

        self.team_event_five_name_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Event Name",
                                                  font=body)
        self.team_event_five_name_entry.grid(row=0, column=3, padx=20, pady=(20, 10))
        self.team_event_five_type_combobox = ctk.CTkComboBox(self.participant_type.tab("Team"),
                                                        values=["Academic", "Sporting"],
                                                        button_color=("#A6A6A6", "#0D0D0D"),
                                                        button_hover_color=("#808080", "#000000"), font=body)
        self.team_event_five_type_combobox.grid(row=1, column=3, padx=20, pady=(10, 10))
        self.team_event_five_rank_entry = ctk.CTkEntry(self.participant_type.tab("Team"), placeholder_text="Score",
                                                  font=body)
        self.team_event_five_rank_entry.grid(row=2, column=3, padx=20, pady=(10, 10))

        self.submit_button = ctk.CTkButton(self.participant_type.tab("Team"), text="Submit", command=self.submit_score,
                                           fg_color=("#0097F7", "#F76000"), hover_color=("#0068AB", "#AB4200"),
                                           font=submit, height=174)
        self.submit_button.grid(row=3, column=3, rowspan=4, padx=20, pady=(10, 20))

        self.solo_participant_type = ctk.CTkTabview(self, width=250, command=self.update_screen_event,
                                                    segmented_button_selected_color=("#0097F7", "#F76000"),
                                                    segmented_button_selected_hover_color=("#0068AB", "#AB4200"),
                                                    segmented_button_unselected_color=("#CCCCCC", "#333333"),
                                                    segmented_button_unselected_hover_color=("#A6A6A6", "#0D0D0D"),
                                                    segmented_button_fg_color=("#CCCCCC", "#333333"),
                                                    text_color=("#333333", "#CCCCCC"))
        self.solo_participant_type.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.solo_participant_type.add("Individual")
        self.solo_participant_type.add("Team")

        self.solo_individual_id_entry = ctk.CTkEntry(self.solo_participant_type.tab("Individual"),
                                                     placeholder_text="Participant ID", font=body)
        self.solo_individual_id_entry.grid(row=0, column=0, padx=(20, 0), pady=(20, 10))

        self.solo_individual_name_entry = ctk.CTkEntry(self.solo_participant_type.tab("Individual"),
                                                       placeholder_text="Participant Name", font=body)
        self.solo_individual_name_entry.grid(row=1, column=0, padx=(20, 0), pady=(10, 10))

        self.solo_placeholder_label = ctk.CTkLabel(self.solo_participant_type.tab("Individual"), text="",
                                                   state="disabled")
        self.solo_placeholder_label.grid(row=2, column=0, padx=(20, 0), pady=(10, 10))

        self.solo_individual_event_name_entry = ctk.CTkEntry(self.solo_participant_type.tab("Individual"),
                                                  placeholder_text="Event Name", font=body)
        self.solo_individual_event_name_entry.grid(row=3, column=0, padx=(20, 0), pady=(10, 10))
        self.solo_individual_event_type_combobox = ctk.CTkComboBox(self.solo_participant_type.tab("Individual"),
                                                        values=["Academic", "Sporting"],
                                                        button_color=("#A6A6A6", "#0D0D0D"),
                                                        button_hover_color=("#808080", "#000000"), font=body)
        self.solo_individual_event_type_combobox.grid(row=4, column=0, padx=(20, 0), pady=(10, 10))
        self.solo_individual_event_rank_entry = ctk.CTkEntry(self.solo_participant_type.tab("Individual"),
                                                  placeholder_text="Score", font=body)
        self.solo_individual_event_rank_entry.grid(row=5, column=0, padx=(20, 0), pady=(10, 20))

        self.solo_submit_button = ctk.CTkButton(self.solo_participant_type.tab("Individual"), text="Submit",
                                                command=self.solo_submit_score, fg_color=("#0097F7", "#F76000"),
                                                hover_color=("#0068AB", "#AB4200"), font=submit, width=194, height=72)
        self.solo_submit_button.grid(row=7, column=0, columnspan=2, padx=20, pady=(10, 20))

        self.solo_team_id_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"), placeholder_text="Team ID",
                                               font=body)
        self.solo_team_id_entry.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.solo_team_name_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"), placeholder_text="Team Name",
                                                 font=body)
        self.solo_team_name_entry.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.solo_team_member_one_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"),
                                                       placeholder_text="Team Member Name", font=body)
        self.solo_team_member_one_entry.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.solo_team_member_two_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"),
                                                       placeholder_text="Team Member Name", font=body)
        self.solo_team_member_two_entry.grid(row=3, column=0, padx=20, pady=(10, 10))
        self.solo_team_member_three_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"),
                                                         placeholder_text="Team Member Name", font=body)
        self.solo_team_member_three_entry.grid(row=4, column=0, padx=20, pady=(10, 10))
        self.solo_team_member_four_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"),
                                                        placeholder_text="Team Member Name", font=body)
        self.solo_team_member_four_entry.grid(row=5, column=0, padx=20, pady=(10, 10))
        self.solo_team_member_five_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"),
                                                        placeholder_text="Team Member Name", font=body)
        self.solo_team_member_five_entry.grid(row=6, column=0, padx=20, pady=(10, 20))

        self.solo_team_event_name_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"),
                                                      placeholder_text="Event Name", font=body)
        self.solo_team_event_name_entry.grid(row=0, column=1, padx=20, pady=(20, 10))
        self.solo_team_event_type_combobox = ctk.CTkComboBox(self.solo_participant_type.tab("Team"),
                                                        values=["Academic", "Sporting"],
                                                        button_color=("#A6A6A6", "#0D0D0D"),
                                                        button_hover_color=("#808080", "#000000"), font=body)
        self.solo_team_event_type_combobox.grid(row=1, column=1, padx=20, pady=(10, 10))
        self.solo_team_event_rank_entry = ctk.CTkEntry(self.solo_participant_type.tab("Team"), placeholder_text="Score",
                                                      font=body)
        self.solo_team_event_rank_entry.grid(row=2, column=1, padx=20, pady=(10, 10))

        self.solo_submit_button = ctk.CTkButton(self.solo_participant_type.tab("Team"), text="Submit",
                                                command=self.solo_submit_score, fg_color=("#0097F7", "#F76000"),
                                                hover_color=("#0068AB", "#ab4200"), font=submit, height=174)
        self.solo_submit_button.grid(row=3, column=1, rowspan=4, padx=20, pady=(10, 20))

    def solo_submit_score(self):
        participant_type = self.solo_participant_type.get()
        individual_id = self.solo_individual_id_entry.get()
        individual_name = self.solo_individual_name_entry.get()
        team_id = self.solo_team_id_entry.get()
        team_name = self.solo_team_name_entry.get()
        team_member_one = self.solo_team_member_one_entry.get()
        team_member_two = self.solo_team_member_two_entry.get()
        team_member_three = self.solo_team_member_three_entry.get()
        team_member_four = self.solo_team_member_four_entry.get()
        team_member_five = self.solo_team_member_five_entry.get()
        solo_individual_event_name = self.solo_individual_event_name_entry.get()
        solo_individual_event_type = self.solo_individual_event_type_combobox.get()
        solo_individual_event_rank = self.solo_individual_event_rank_entry.get()
        solo_team_event_name = self.solo_team_event_name_entry.get()
        solo_team_event_type = self.solo_team_event_type_combobox.get()
        solo_team_event_rank = self.solo_team_event_rank_entry.get()

        if individual_id and individual_name and solo_individual_event_name and solo_individual_event_type and solo_individual_event_rank:
            solo_insert_score(participant_type, individual_id, individual_name, team_id, team_name, team_member_one, team_member_two, team_member_three, team_member_four, team_member_five, solo_individual_event_name, solo_individual_event_type, solo_individual_event_rank)

            self.solo_individual_id_entry.delete(0, 'end')
            self.solo_individual_name_entry.delete(0, 'end')
            self.solo_individual_event_name_entry.delete(0, 'end')
            self.solo_individual_event_type_combobox.set('Academic')
            self.solo_individual_event_rank_entry.delete(0, 'end')
            self.master.score_board.solo_update_scores()

        if team_id and team_name and team_member_one and team_member_two and team_member_three and team_member_four and team_member_five and solo_team_event_name and solo_team_event_type and solo_team_event_rank:
            solo_insert_score(participant_type,
                              individual_id,
                              individual_name,
                              team_id,
                              team_name,
                              team_member_one,
                              team_member_two,
                              team_member_three,
                              team_member_four,
                              team_member_five,
                              solo_team_event_name,
                              solo_team_event_type,
                              solo_team_event_rank)

            self.solo_team_id_entry.delete(0, 'end')
            self.solo_team_name_entry.delete(0, 'end')
            self.solo_team_member_one_entry.delete(0, 'end')
            self.solo_team_member_two_entry.delete(0, 'end')
            self.solo_team_member_three_entry.delete(0, 'end')
            self.solo_team_member_four_entry.delete(0, 'end')
            self.solo_team_member_five_entry.delete(0, 'end')
            self.solo_team_event_name_entry.delete(0, 'end')
            self.solo_team_event_type_combobox.set('Academic')
            self.solo_team_event_rank_entry.delete(0, 'end')
            self.master.score_board.solo_update_scores()

    def submit_score(self):
        participant_type = self.participant_type.get()
        individual_id = self.individual_id_entry.get()
        individual_name = self.individual_name_entry.get()
        team_id = self.team_id_entry.get()
        team_name = self.team_name_entry.get()
        team_member_one = self.team_member_one_entry.get()
        team_member_two = self.team_member_two_entry.get()
        team_member_three = self.team_member_three_entry.get()
        team_member_four = self.team_member_four_entry.get()
        team_member_five = self.team_member_five_entry.get()
        individual_event_one_name = self.individual_event_one_name_entry.get()
        individual_event_one_type = self.individual_event_one_type_combobox.get()
        individual_event_one_rank = self.individual_event_one_rank_entry.get()
        individual_event_two_name = self.individual_event_two_name_entry.get()
        individual_event_two_type = self.individual_event_two_type_combobox.get()
        individual_event_two_rank = self.individual_event_two_rank_entry.get()
        individual_event_three_name = self.individual_event_three_name_entry.get()
        individual_event_three_type = self.individual_event_three_type_combobox.get()
        individual_event_three_rank = self.individual_event_three_rank_entry.get()
        individual_event_four_name = self.individual_event_four_name_entry.get()
        individual_event_four_type = self.individual_event_four_type_combobox.get()
        individual_event_four_rank = self.individual_event_four_rank_entry.get()
        individual_event_five_name = self.individual_event_five_name_entry.get()
        individual_event_five_type = self.individual_event_five_type_combobox.get()
        individual_event_five_rank = self.individual_event_five_rank_entry.get()
        team_event_one_name = self.team_event_one_name_entry.get()
        team_event_one_type = self.team_event_one_type_combobox.get()
        team_event_one_rank = self.team_event_one_rank_entry.get()
        team_event_two_name = self.team_event_two_name_entry.get()
        team_event_two_type = self.team_event_two_type_combobox.get()
        team_event_two_rank = self.team_event_two_rank_entry.get()
        team_event_three_name = self.team_event_three_name_entry.get()
        team_event_three_type = self.team_event_three_type_combobox.get()
        team_event_three_rank = self.team_event_three_rank_entry.get()
        team_event_four_name = self.team_event_four_name_entry.get()
        team_event_four_type = self.team_event_four_type_combobox.get()
        team_event_four_rank = self.team_event_four_rank_entry.get()
        team_event_five_name = self.team_event_five_name_entry.get()
        team_event_five_type = self.team_event_five_type_combobox.get()
        team_event_five_rank = self.team_event_five_rank_entry.get()

        if (individual_id and individual_name and individual_event_one_name and individual_event_one_type and individual_event_one_rank and individual_event_two_name
                and individual_event_two_type and individual_event_two_rank and individual_event_three_name and individual_event_three_type and individual_event_three_rank
                and individual_event_four_name and individual_event_four_type and individual_event_four_rank and individual_event_five_name and individual_event_five_type
                and individual_event_five_rank):

            insert_score(participant_type,
                         individual_id,
                         individual_name,
                         team_id,
                         team_name,
                         team_member_one,
                         team_member_two,
                         team_member_three,
                         team_member_four,
                         team_member_five,
                         individual_event_one_name,
                         individual_event_one_type,
                         int(individual_event_one_rank),
                         individual_event_two_name,
                         individual_event_two_type,
                         int(individual_event_two_rank),
                         individual_event_three_name,
                         individual_event_three_type,
                         int(individual_event_three_rank),
                         individual_event_four_name,
                         individual_event_four_type,
                         int(individual_event_four_rank),
                         individual_event_five_name,
                         individual_event_five_type,
                         int(individual_event_five_rank))

            self.individual_id_entry.delete(0, 'end')
            self.individual_name_entry.delete(0, 'end')
            self.individual_event_one_name_entry.delete(0, 'end')
            self.individual_event_one_type_combobox.set('Academic')
            self.individual_event_one_rank_entry.delete(0, 'end')
            self.individual_event_two_name_entry.delete(0, 'end')
            self.individual_event_two_type_combobox.set('Academic')
            self.individual_event_two_rank_entry.delete(0, 'end')
            self.individual_event_three_name_entry.delete(0, 'end')
            self.individual_event_three_type_combobox.set('Academic')
            self.individual_event_three_rank_entry.delete(0, 'end')
            self.individual_event_four_name_entry.delete(0, 'end')
            self.individual_event_four_type_combobox.set('Academic')
            self.individual_event_four_rank_entry.delete(0, 'end')
            self.individual_event_five_name_entry.delete(0, 'end')
            self.individual_event_five_type_combobox.set('Academic')
            self.individual_event_five_rank_entry.delete(0, 'end')
            self.master.score_board.multiple_update_scores()

        if (team_id and team_name and team_member_one and team_member_two and team_member_three and team_member_four
                and team_member_five and team_event_one_name and team_event_one_type and team_event_one_rank and team_event_two_name
                and team_event_two_type and team_event_two_rank and team_event_three_name and team_event_three_type and team_event_three_rank
                and team_event_four_name and team_event_four_type and team_event_four_rank and team_event_five_name and team_event_five_type
                and team_event_five_rank):

            insert_score(participant_type,
                         individual_id,
                         individual_name,
                         team_id,
                         team_name,
                         team_member_one,
                         team_member_two,
                         team_member_three,
                         team_member_four,
                         team_member_five,
                         team_event_one_name,
                         team_event_one_type,
                         int(team_event_one_rank),
                         team_event_two_name,
                         team_event_two_type,
                         int(team_event_two_rank),
                         team_event_three_name,
                         team_event_three_type,
                         int(team_event_three_rank),
                         team_event_four_name,
                         team_event_four_type,
                         int(team_event_four_rank),
                         team_event_five_name,
                         team_event_five_type,
                         int(team_event_five_rank))

            self.team_id_entry.delete(0, 'end')
            self.team_name_entry.delete(0, 'end')
            self.team_member_one_entry.delete(0, 'end')
            self.team_member_two_entry.delete(0, 'end')
            self.team_member_three_entry.delete(0, 'end')
            self.team_member_four_entry.delete(0, 'end')
            self.team_member_four_entry.delete(0, 'end')
            self.team_member_five_entry.delete(0, 'end')
            self.team_event_one_name_entry.delete(0, 'end')
            self.team_event_one_type_combobox.set('Academic')
            self.team_event_one_rank_entry.delete(0, 'end')
            self.team_event_two_name_entry.delete(0, 'end')
            self.team_event_two_type_combobox.set('Academic')
            self.team_event_two_rank_entry.delete(0, 'end')
            self.team_event_three_name_entry.delete(0, 'end')
            self.team_event_three_type_combobox.set('Academic')
            self.team_event_three_rank_entry.delete(0, 'end')
            self.team_event_four_name_entry.delete(0, 'end')
            self.team_event_four_type_combobox.set('Academic')
            self.team_event_four_rank_entry.delete(0, 'end')
            self.team_event_five_name_entry.delete(0, 'end')
            self.team_event_five_type_combobox.set('Academic')
            self.team_event_five_rank_entry.delete(0, 'end')
            self.master.score_board.multiple_update_scores()

    def update_screen_event(self):
        participant_tab = self.participant_type.get()
        solo_particpant_tab = self.solo_participant_type.get()

        if participant_tab == "Individual" and solo_particpant_tab == "Individual":
            SCREEN_SIZE = f"{1100}x{500}"

        if participant_tab == "Individual" and solo_particpant_tab == "Team":
            SCREEN_SIZE = f"{1230}x{500}"

        if participant_tab == "Team" and solo_particpant_tab == "Individual":
            SCREEN_SIZE = f"{1280}x{500}"

        if participant_tab == "Team" and solo_particpant_tab == "Team":
            SCREEN_SIZE = f"{1400}x{450}"

        gui.main_gui.MainGUI.screen_update(self.master, SCREEN_SIZE)
