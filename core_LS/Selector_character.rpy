################################################################


# SELECTOR CHARACTER ACTION


########################################

default chr2_game = Single_chr_selection() # La variable mas importante del juego
# ya que verifica que personaje se esta jugando.

#######################################
    # num_chr = (codec)
    # Azuli 1
    # Vacio 2
    # Cristal 3
    # Inosuki 4


init python:

    data_value = LS_data("LS_archive/value_init.csv")

    @renpy.pure
    class Single_chr_selection(object):
        def __init__(self, main=False):
            # Cargar los JSON usando el sistema de caché solo una vez
            # --- JSONs globales ---

            self.VAR_CHARA = JSON_("data_library_json/CHARACTER_DECRIPTION.json") # data base de descripciones
            self.character_dict = JSON_("data_library_json/CHARACTER_DICT.json") # data base de datos de personajes como nombre, cultura...
            self.character_name_pack = JSON_("data_library_json/CHARACTER_NAME_PACK.json") # nombre personalizado
            self.NUMER = JSON_("data_library_json/CHARACTER_IMAGE_SELECT.json") # Imagenes de presentacion ubicacion de ellos

            # --- Estado del personaje ---
            self.s_chr = "" # codigo general de personaje = azuli_
            self.culture_chr = "" # cultura de personaje
            self.g_name = "" # nombre de personaje dinamico
            self.clothe_use = "" # ropa a usar de personaje
            self.code = "" # codigo comun = azuli, funciona como id

            # --- Flags de control ---
            self.if_logo_choice = 1 # efecto de imagen
            self.image_dict = None # imagen por usar a presentacion
            self.character_description_ = "" # descripcion de personaje
            self.language_description_ = str("spanish")
            self.select_ok = True # ¿seleccionado?, esto se reinicia al comenzar a False

            # --- Valores de selección ---
            self.num_chr = str(data_value["value_chr_select"]) # identificador global de personaje 1, 2, 3...
            self.num_pag = data_value["character_pag"] # numero de pagina de personaje
            self.num_pag_max = data_value["max_chr_select"] # maximo de paginas del selector

            self.Pack_reset(c_all=True)



        def refresh_json(self):
            self.VAR_CHARA = JSON_("data_library_json/CHARACTER_DECRIPTION.json")
            self.character_dict = JSON_("data_library_json/CHARACTER_DICT.json")
            self.character_name_pack = JSON_("data_library_json/CHARACTER_NAME_PACK.json")
            self.NUMER = JSON_("data_library_json/CHARACTER_IMAGE_SELECT.json")

        # 🔄 Guardado/restauración seguro
        def __getstate__(self):
            # Guardamos solo el estado que debe persistir
            return {
                "s_chr": self.s_chr,
                "culture_chr": self.culture_chr,
                "g_name": self.g_name,
                "clothe_use": self.clothe_use,
                "code": self.code,
                "if_logo_choice": self.if_logo_choice,
                "image_dict": self.image_dict,
                "character_description_": self.character_description_,
                "language_description_": self.language_description_,
                "select_ok": self.select_ok,
                "num_chr": self.num_chr,
                "num_pag": self.num_pag,
                "num_pag_max": self.num_pag_max,
            }

        def __setstate__(self, state):
            # Restaurar valores persistentes
            self.s_chr = state.get("s_chr", "")
            self.culture_chr = state.get("culture_chr", "")
            self.g_name = state.get("g_name", "")
            self.clothe_use = state.get("clothe_use", "")
            self.code = state.get("code", "")
            self.if_logo_choice = state.get("if_logo_choice", 1)
            self.image_dict = state.get("image_dict", None)
            self.character_description_ = state.get("character_description_", "")
            self.language_description_ = state.get("language_description_", "spanish")
            self.select_ok = state.get("select_ok", True)
            self.num_chr = state.get(str(data_value["value_chr_select"]))
            self.num_pag = state.get(data_value["character_pag"])
            self.num_pag_max = state.get(data_value["max_chr_select"])

            # 🔄 Recargar JSON dinámicos
            self.refresh_json()



        def Pack_character_right(self):
            if self.num_pag >= self.num_pag_max:
                renpy.music.play("audio/sfx/user_ui_negative.ogg", channel="sound")
                self.num_pag = self.num_pag_max
                self.num_chr = self.num_pag_max
                self.Pack_reset()
            else:
                renpy.music.play("audio/sfx/effect_button_right.ogg", channel="sound")
                self.num_pag += 1
                self.num_chr += 1
                self.if_logo_choice = 1       
                self.Pack_reset()

        def Pack_character_left(self):
            if self.num_pag <= 1:
                renpy.music.play("audio/sfx/user_ui_negative.ogg", channel="sound")
                self.Pack_reset(c_all=True)
            else:
                renpy.music.play("audio/sfx/effect_button_left.ogg", channel="sound")
                self.num_pag -= 1
                self.num_chr -= 1
                self.if_logo_choice = 2
                self.Pack_reset()


        def Pack_reset(self, c_all=False):
            if c_all:
                self.num_chr = 1
                self.num_pag = 1

            chrs = str(self.num_chr)
            chrs_pag = str(self.num_pag)

            data_info = self.character_dict.get(chrs, {"name": "???", "culture": "???", "clothe": "???", "code": "???"})

            self.s_chr = data_info.get("name", "???")
            self.culture_chr = data_info.get("culture", "???")
            self.clothe_use = data_info.get("clothe", "???")
            self.code = data_info.get("code", "???")

            self.g_name = self.character_name_pack.get(chrs_pag, "???")

            chara_data = self.VAR_CHARA.get(chrs, {"spanish": "???", "english": "???"})

            # aseguramos que language_box tenga valor válido
            lang = getattr(persistent, "language_box", "spanish")

            # aquí sí pedimos la descripción en ese idioma
            self.character_description_ = chara_data.get(lang, "???")

            self.image_dict = self.NUMER.get(chrs, None)

        
            # if voice is True:
            #     renpy.music.play(f"audio/narrator/{self.s_chr}narrator_english.ogg", channel="voice_sfx")

        def __str__(self):
            return f"{self.s_chr}/{self.g_name}"


    def Sound_screen_once(neg: bool = True) -> bool:
        if neg:
            return renpy.music.play("audio/sfx_min/effect_notify1.ogg", channel='sound')
        else:
            return renpy.music.play("audio/sfx_min/effect_notify2.ogg", channel='sound')





#######################################################################

