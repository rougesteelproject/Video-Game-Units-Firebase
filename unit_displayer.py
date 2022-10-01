import tkinter as tk

class UnitDispalyer(tk.Frame):
    def __init__(self, callback_handler) -> None:
        super().__init__(callback_handler.top_level)

        self._callback_handler = callback_handler
        self._game_loop = self._callback_handler._game_loop

        self._unit_dict_holder = tk.StringVar(self)
        self._unit_dict_label = tk.Label(self)
        self._unit_dict_label.configure(textvariable=self._unit_dict_holder)
        self._unit_dict_label.pack(side="top")

        self.entry_unit_name = tk.Entry(self)
        _text_ = "Unit Name"
        self.entry_unit_name.delete("0", "end")
        self.entry_unit_name.insert("0", _text_)
        self.entry_unit_name.pack(side="top")

        self.entry_modpack = tk.Entry(self)
        _text_ = "Modpack Name"
        self.entry_modpack.delete("0", "end")
        self.entry_modpack.insert("0", _text_)
        self.entry_modpack.pack(side="top")

        self._button_fetch_unit = tk.Button(self)
        self._button_fetch_unit.configure(text="Fetch the Unit", command = lambda: self._fetch_unit())
        self._button_fetch_unit.pack(side='top')

        self._button_create_unit = tk.Button(self)
        self._button_create_unit.configure(text="Create Another Unit", command=lambda :self._create_unit())
        self._button_create_unit.pack(side="top")

        self.pack(side="top")

    def _fetch_unit(self):
        modpack = self.entry_modpack.get()
        unit_name = self.entry_unit_name.get()
        self._unit_dict_holder.set(self._game_loop.fetch_unit(unit_name, modpack).to_dict())

    def _create_unit(self):
        self._game_loop.run_unit_creator_menu()