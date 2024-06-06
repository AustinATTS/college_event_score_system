import customtkinter as ctk
from data.multiple_data_handler import fetch_scores, clear_scores
from data.solo_data_handler import solo_fetch_scores, solo_clear_scores


class EventDirectory(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0, fg_color=("#CCCCCC", "#333333"))

        self.team_frame = ctk.CTkFrame(self)
        self.team_frame.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.individual_frame = ctk.CTkFrame(self)
        self.individual_frame.grid(row=0, column=1, padx=20, pady=(20, 10))

   #     self.events_list()

#    def events_list(self):
 #       solo_events = solo_fetch_scores()
  #      multiple_events = fetch_scores()
#
 #       if total_events[1] == "Team":
  #          event = ctk.CTkLabel(self.team_frame, text=f"{total_events[3]}")
   #         event.grid(row=total_events[0], column=0, padx=20, pady=(10, 10))
    #    elif total_events[1] == "Individual":
     #       event = ctk.CTkLabel(self.individual_frame, text=f"{total_events[3]}")
      #      event.grid(row=total_events[0], column=0, padx=20, pady=(10, 10))
       # else:
        #    print("What The Fuck Has Just Happened Jesus Christ This Shouldnt Be Running Oh God")
