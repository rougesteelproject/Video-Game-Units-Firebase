import logging

class Unit:
    def __init__(self, name: str, base_health: int, min_attack: int, ai_types: list = ['basic'], game_version:float = 3, attack_verb:str = "attacked") -> None:

        self._name = name

        self._game_version = int(game_version)

        self._base_health = int(base_health)
        
        self._min_attack = int(min_attack)
        self._max_attack = self._min_attack
        

        self._attack_verb = attack_verb

        self._ai_types = ai_types

    @staticmethod
    def from_dict(source):

        unit = Unit(name = source[u'_name'], base_health = source[u'_base_health'],  min_attack = source[u'_min_attack'], ai_types= source[u'_ai_types'], game_version= source[u'_game_version'], attack_verb= source[u'_attack_verb'])
        
        if u'max_attack' in source:
            unit._max_attack = source[u'_max_attack']

        if u'min_initiative' in source:
            unit._min_initiative = source[u'_min_initiative']
            if u'max_initiative' in source:
                unit._max_initiative = source[u'_max_initiative']
            else:
                unit._max_initiative = unit._min_initiative

        if u'raw_power_v3' in source:
            unit.raw_power_v3 = source[u'_raw_power_v3']
        
            
        if u'raw_power_v2' in source:
            unit.raw_power_v2 = source[u'_raw_power_v2']
        
        if u'raw_power_v1' in source:
            unit.raw_power_v1 = source[u'_raw_power_v1']

        if u'modpack' in source:
            unit.modpack = source[u'_modpack']

        if u'creator_email' in source:
            unit.creator_email = source[u'_creator_email']
            
        return unit

    def to_dict(self):
        return self.__dict__

        if self._game_version >= game_version and not hasattr(self, f'raw_power_v{game_version}'):
            self._set_raw_powers()

        if game_version == 3:
            raw_power = self._raw_power_v3
        elif game_version == 2:
            raw_power = self._raw_power_v2
        elif game_version == 1:
            raw_power = self._raw_power_v1

        if raw_power == None:
            logging.error("Tried to get raw_power from a unit with invalid stats.")
        return raw_power