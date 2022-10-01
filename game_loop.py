import constants

from tk_ui_handler import TKUIHandler

from db_controller_firestore import FirebaseDB

from sign_in_handler import SignInHandler

from google.oauth2.credentials import Credentials

import logging

class GameLoop():
    def __init__(self) -> None:
        
        
        self._ui_handler = TKUIHandler(self)

        self._sign_in_handler = SignInHandler()

        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename= constants.ERROR_LOG_URI, encoding='utf-8', level=logging.ERROR, filemode='w')

        self.run_sign_in_prompt()
        self._ui_handler.run()

    def sign_in(self, email, password):
        #Credit to Bob Thomas

        response = self._sign_in_handler.sign_in_email_pass(email, password)
        
        if 'error' in response:
            self.run_sign_in_prompt(error = response['error']['message'])
        else:
            self._user_email = email
            #TODO use this where it previously asked for emails
            
            # Use google.oauth2.credentials and the response object to create the correct user credentials
            credentials = Credentials(response['idToken'], response['refreshToken'])

            self._database_controler = FirebaseDB(credentials)

            self.run_unit_creator_menu()

    def run_sign_in_prompt(self, error = None):
        self._ui_handler.create_sign_in_menu(error)

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