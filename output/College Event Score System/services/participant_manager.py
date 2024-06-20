import customtkinter as ctk
from data.multiple_data_handler import fetch_scores
from data.solo_data_handler import solo_fetch_scores

teams = []
individuals = []

class ParticipantHandler:
    def get_participants(self):
        print("Hello World")
        self.clear_teams()
        self.clear_individuals()
        multiple_events = fetch_scores()
        solo_events = solo_fetch_scores()

        for multiple_event in multiple_events:
            if multiple_event[1] == "Individual":
                self.add_individual(multiple_event[2], multiple_event[3])
            elif multiple_event[1] == "Team":
                self.add_team(multiple_event[4], multiple_event[5], multiple_event[6], multiple_event[7], multiple_event[8], multiple_event[9], multiple_event[10])

        for solo_event in solo_events:
            if solo_event[1] == "Individual":
                self.add_individual(solo_event[2], solo_event[3])
            elif solo_event[1] == "Team":
                self.add_team(solo_event[4], solo_event[5], solo_event[6], solo_event[7], solo_event[8], solo_event[9], solo_event[10])

        team_list = self.return_teams()
        individual_list = self.return_individuals()

        team_count = len(team_list)
        individual_count = len(individual_list)

        print(f"{team_count} - {individual_count}")

        if team_count >= 4:
            self.show_notice("You have entered the max amount of teams")
            return False

        if individual_count >= 20:
            self.show_notice("You have entered the max amount of individuals")
            return False

        return True

    def show_notice(self, message):
        print("Showing notice:", message)
        message_box = ctk.CTkToplevel()
        message_box.title("Notice")
        message_box.geometry(f"{400}x{200}")
        message_box.resizable(False, False)
        notice = ctk.CTkLabel(message_box, text=message)
        notice.grid(row=0, column=0, padx=20, pady=(20, 10))
        close_button = ctk.CTkButton(message_box, text="Close", command=message_box.destroy)
        close_button.grid(row=1, column=0, padx=20, pady=(10, 20))

    def add_team(self, team_id, team_name, team_member_one, team_member_two, team_member_three, team_member_four, team_member_five):
        teams.append(f"{team_id} - {team_name} : {team_member_one}, {team_member_two}, {team_member_three}, {team_member_four}, {team_member_five}")

    def add_individual(self, individual_id, individual_name):
        individuals.append(f"{individual_id} - {individual_name}")

    def return_teams(self):
        return teams

    def return_individuals(self):
        return individuals

    def clear_teams(self):
        teams.clear()

    def clear_individuals(self):
        individuals.clear()
