import constants

from tk_ui_handler import TKUIHandler

from db_controller_firestore import FirebaseDB

import logging

class GameLoop():
    def __init__(self) -> None:
        self._database_controler = FirebaseDB()
        
        self._ui_handler = TKUIHandler(self)

        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename= constants.ERROR_LOG_URI, encoding='utf-8', level=logging.ERROR, filemode='w')

        self.run_unit_creator_menu()
        self._ui_handler.run()

    def run_unit_creator_menu(self):
        self._ui_handler.create_unit_creator_menu()

    def run_unit_display(self):
        self._ui_handler.create_unit_displayer()
        
    def save_unit(self, unit):
        self._database_controler.save_unit(unit)
        self.run_unit_display()

    def fetch_unit(self, unit_name, modpack_name):
        unit = self._database_controler.get_unit_by_modpack_and_name(modpack_name, unit_name)
        return unit

gameloop = GameLoop()