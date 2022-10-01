import tkinter as tk

from unit_creator_menu import UnitCreatorMenu
from unit_displayer import UnitDispalyer
from sign_in_menu import SignInMenu

class TKUIHandler:
    def __init__(self, game_loop) -> None:
        self._game_loop = game_loop
        
        self.create_top_level()   

    def create_top_level(self):
        if not hasattr(self, "top_level"):

            self.top_level = tk.Tk()
            self.top_level.configure(height=800, width=800)

    def clear_screen(self):
        if hasattr(self, "_sign_in_menu"):
            self._sign_in_menu.destroy()

        if hasattr(self, "_unit_creator_menu"):
            self._unit_creator_menu.destroy()

        if hasattr(self, "_unit_displayer"):
            self._unit_displayer.destroy()

    def create_sign_in_menu(self, error_message):
        self.clear_screen()

        self._sign_in_menu = SignInMenu(self, error_message)

    def create_unit_creator_menu(self):
        self.clear_screen()

        self._unit_creator_menu = UnitCreatorMenu(self)

    def create_unit_displayer(self):
        self.clear_screen()

        self._unit_displayer = UnitDispalyer(self)

    def exit_game(self):
        self.top_level.destroy()

    def run(self):
        self.top_level.mainloop()