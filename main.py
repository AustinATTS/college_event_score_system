import customtkinter as ctk
from gui.main_window import MainWindow


def main():
    app = ctk.CTk()
    main_window = MainWindow(app)
    main_window.pack(fill="both", expand=True)
    app.mainloop()


if __name__ == "__main__":
    main()
