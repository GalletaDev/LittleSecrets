
# CHAPTER SYSTEM
default chapter_extra = Chapter(1, special=True)

default chapter = Chapter(1)

default chapter_complete = False

init python:

    MAX_CHAPTER = 100 # Limite de cap

    class Chapter(object):
        def __init__(self, ch: int, loop: bool = False, special: bool = False):
            self.ch = ch
            self.loop = loop
            self.special = special
            self._temp_cache = 0

        def Next_ch(self, a: int = 1) -> int:
            """
            Cambiamos al siguiente capitulo del juego, normalmente no supera el limite de capitulo permitidos
            """
            if self.ch >= MAX_CHAPTER:
                self.ch = MAX_CHAPTER
            else:
                self.ch += a

        def Set_ch(self, a: int) -> int:
            """
            Especificamos que capitulo ir exactamente, pero debe estar disponible.
            Si le decimos un numero que no existe en los archivos, puede que se desvié
            """
            if self.ch > MAX_CHAPTER:
                self.ch = MAX_CHAPTER
            else:
                self.ch = a

        def Loop(self, loop_a: bool = False):
            """
            Loop de capitulo, normalmente es False
            """
            if loop_a:
                renpy.jump("loop_bucle_game")

        def __getstate__(self):
            return {
                "ch": self.ch,
                "loop": self.loop,
                "special": self.special
            }

        # Método para deserializar (cargar)
        def __setstate__(self, state):
            self.ch = state.get("ch", 1)
            self.loop = state.get("loop", False)
            self.special = state.get("special", False)
            self._temp_cache = 0  # se reconstruye con valor default

        def Jump_event(self, next_cap: bool = False) -> bool:
            """
            Aqui le decimos para enviar al jugador al capitulo especifico del evento
            normalmente ya esta con el parámetro listo, esto funciona solo cuando ya tienes Amor suficiente
            """
            global chr2_game
            if next_cap:
                self.Next_ch()
            else:
                renpy.jump("event_" + str(self.ch) + "_game_" + str(chr2_game.s_chr))   

        def Jump_chapter(self):
            """
            Aqui le decimos para enviar al jugador al capitulo especifico del personaje,
            normalmente ya esta con el parámetro listo, esto funciona solo cuando ya tienes Amor suficiente
            """            
            global chr2_game
            renpy.jump("mode_" + str(chr2_game.s_chr) + "chapter_" + str(self.ch))

        def reset_all(self):
            """
            Reinicia los valores en capítulos
            """
            self.ch = 1
            self.loop = False
            self.special = False

        def resource_(self):
            print(f"Chapter", self.ch, "//", "Loop", self.loop, "//", "special", self.special)

        def __str__(self):
            value_name = f"Chapter={self.ch} " + f"Loop={self.loop} " + f"Special={self.special}"
            return value_name

