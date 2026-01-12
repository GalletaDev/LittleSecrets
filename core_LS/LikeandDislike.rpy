


init python:
    # CHARACTER PREFERENCES SYSTEM
    class CharacterPreferences(object):
        def __init__(self):
            self.preferences = self.LS_character()

        def LS_character(self):
            """Carga las preferencias desde un archivo JSON."""
            try:
                with renpy.open_file("data_library_json/CHARACTER_LIKE.json") as file:
                    data = json.load(file)
                    return data
            except FileNotFoundError:
                return {}
            except json.JSONDecodeError:
                return {}

        def check_preference(self, character):
            global inv_object
            if character in self.preferences:
                for gift_name in inv_object.gf.keys():
                    if gift_name in self.preferences[character]["likes"]:
                        return "like", gift_name
                    elif gift_name in self.preferences[character]["dislikes"]:
                        return "dislike", gift_name
                    elif gift_name in self.preferences[character]["morelike"]:
                        return "morelike", gift_name
                    elif gift_name in self.preferences[character]["bad"]:
                        return "bad", gift_name
            return "neutral", None

        # 🔄 --- Guardado y restaurado seguro ---
        def __getstate__(self):
            return {}  # no guardamos nada, se recarga siempre

        def __setstate__(self, state):
            self.preferences = self.LS_character()
