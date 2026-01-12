

#################################################################################

# STATUS CHARACTER LOGIC



#"1": "good", bueno
#"2": "medium", normal
#"3": "bad", tension
#"4": "angry", enojo
#"5": "sad", triste
#"6": "demon", demon
#"7": "happy", feliz
#"8": "hot", luj###
#"9": "boring" aburrida
#"10": "borracha" borracha







init python:

    @renpy.pure
    class Health(object):
        def __init__(self, name, scale, status, image_p):
            self.name = name
            self.scale = scale
            self.status = status
            self.image_p = image_p
            self.STATUS_MAP = JSON_("data_library_json/Health_value.json")
            self.IMAGE_MAP = JSON_("data_library_json/Health_image.json")
            # self._temp_cache = 0  # se reconstruye con valor default
            self.reload_health()
            
        def status_def(self, value: str) -> str:
            """
            Esta función proviene de (Health) se encarga de cambiar el dígito
            de la emoción también afecta varias funciones como check_valid_scale
            $ value.status_def = del 1 al 10
            colocar un dígito como >=11 o <=0 puede provocar error ya que no existe esas emociones
            """
            self.scale = str(value)
            #self.reload_health()
            self.reload_health()

        def config(self, value: str) -> str:
            """
            Esta funcion se encarga de configurar directamente el valor de self.scale
            aunque status_def haga lo mismo este configurar con un valor bruto por lo que es
            mas eficaz el cambio.
            """
            if self.scale != str(value):
                self.scale = str(value)
                self.reload_health()
        def repare_status(self, select_status="bad"):
            """
            Reinicia al detectar un defecto que se puede quitar
            digamos que esta aburrida, y quieres quitarlo, esta funciona hace eso
            """
            ############################################
            if self.scale == "3":
                self.reload_health()
                return print(f"No hacer nada")
            ############################################
            if select_status == "bad":
                if self.scale in ["9", "5", "4"]:
                    self.config(1)
            elif select_status == "good":
                if self.scale in ["7", "2", "10"]:                
                    self.config(1)
            else:
                print(f"Se eligio de forma aleatoria")
                self.config(renpy.random.choice(["1", "5", "9", "4"]))     

            Action_effect_category() # verifica si afecta alguna habilidad de personalidad           
            self.reload_health()

        def get_scale(self):
            """
            Se usa normalmente para condiciones que necesiten el valor de self.scale
            """
            return str(self.scale)

        def reload_health(self):
            self.status = self.STATUS_MAP.get(str(self.scale), "Invalid")
            self.image_p = self.IMAGE_MAP.get(str(self.scale), "Invalid")            
            self.check_valid_scale()

        def __getstate__(self):
            return {
                "name": self.name,
                "scale": str(self.scale),
                "status": self.status,
                "image_p": self.image_p
            }

        # Método para deserializar (cargar)
        def __setstate__(self, state):
            self.name = state.get("name", _("Estado"))
            self.scale = state.get("scale", "1")
            self.status = state.get("status", "")
            self.image_p = state.get("image_p", "")
            self.STATUS_MAP = JSON_("data_library_json/Health_value.json")
            self.IMAGE_MAP = JSON_("data_library_json/Health_image.json")
            # self._temp_cache = 0  # se reconstruye con valor default
            


        def check_valid_scale(self):
            """
            Esta funcion es automatico es la raiz menor de status_def, se encarga de verificar que existen las emociones
            que ingresas cuando cambias.
            """
            if self.status == "Invalid":
                raise ValueError(f"Invalid scale {self.scale}. Valid options are {list(self.STATUS_MAP.keys())}")
            if self.image_p == "Invalid":
                raise ValueError(f"Invalid scale {self.scale}. Valid options are {list(self.IMAGE_MAP.keys())}")
            #print(f"🎭Status>>> {self.scale}: {self.status}")

        def __str__(self):
            return f"{self.name}"




default str_status = {
    "eat": "{image=status_active_n}",
    "tele": "{image=status_active_n}",
    "bath": "{image=status_active_n}",
    "sleep": "{image=status_active_n}"
}

image status_active_y = Transform("resource/point_ubication_bot.png", size=(30, 30))
image status_active_n = Transform("resource/point_ubication_bot.png", matrixcolor=SaturationMatrix(0), size=(30, 30))

image status_eat_small = "gui/button_status_screen/eat_status.png"
image status_tv_small = "gui/button_config_screen/button_tv_hover.png"
image status_bath_small = "gui/button_config_screen/button_fish_hover.png"
image status_zzz_small = "gui/button_status_screen/zzz_status.png"

image status_eat_small_icon = Transform("gui/button_status_screen/eat_status.png", size=(30, 30))
image status_tv_small_icon = Transform("gui/button_config_screen/button_tv_hover.png", size=(30, 30))
image status_bath_small_icon = Transform("gui/button_config_screen/button_fish_hover.png", size=(30, 30))
image status_zzz_small_icon = Transform("gui/button_status_screen/zzz_status.png", size=(30, 30))



init python:
    def str_verify_name():
        global eat_character, tele_character, bath_character, sleep_character

        character_states = {
            "eat": eat_character,
            "tele": tele_character,
            "bath": bath_character,
            "sleep": sleep_character
        }

        for key, state in character_states.items():
            str_status[key] = "{image=status_active_y}" if state else "{image=status_active_n}"

    def translate_status_key(key):
        return {
            "eat": "{image=status_eat_small}",
            "tele": "{image=status_tv_small}",
            "bath": "{image=status_bath_small}",
            "sleep": "{image=status_zzz_small}"
        }.get(key, key)
    

#############################################