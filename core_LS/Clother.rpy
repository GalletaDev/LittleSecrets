


init python:
    class SimpleClother(object):
        def __init__(self, character, clothe, default_c, poses=1, pose=1):
            self.character = character
            self.clothe = clothe
            self.default_c = default_c
            self.pack = None
            self.poses = poses
            self.pose = pose  
            self.current_arms_pose = "default"

        def __getstate__(self):
            return {
                "character": self.character,
                "clothe": self.clothe,
                "default_c": self.default_c,
                "poses": self.poses,
                "pose": self.pose,
                "current_arms_pose": self.current_arms_pose
            }

        def __setstate__(self, state):
            self.character = state.get("character", "")
            self.clothe = state.get("clothe", "")
            self.default_c = state.get("default_c", self.clothe)
            self.poses = state.get("poses", 1)
            self.pose = state.get("pose", 1)
            self.current_arms_pose = state.get("current_arms_pose", "default")
            
            self.load_pack()

        def load_pack(self):
            if not hasattr(self, "pack") or self.pack is None:
                json_path = f"data_clothe_json/chr_library_clother_{self.character}.json"
                self.pack = JSON_(json_path)
            return self.pack

        def set(self, new_clothe):
            self.clothe = new_clothe
            print(f"ahora {self.clothe} es {new_clothe}")
            renpy.restart_interaction() # forzamos a la pantalla a reiniciarse

        def get_clothe_data(self):
            return self.pack.get(self.clothe, {})   # ahora devuelve { "path": ..., "covers_arms": ... }

        def get_image_path(self):
            data = self.get_clothe_data()
            name = chr2_game.code
            return data.get("path", f"character/{name}/clouth/none_image.png")

        def covers_arms(self):
            """Devuelve cómo maneja los brazos esta prenda (False, True, o 'custom')."""
            data = self.get_clothe_data()
            return data.get("covers_arms", False)

        def set_arms_pose(self, pose_name):
            covers = self.covers_arms()

            if covers is True:
                # ropa que oculta brazos por completo
                print(f">> {self.clothe} cubre los brazos, no puedes cambiar pose, puede que ya tenga hechas ya")
                return True
            elif covers == "custom":
                # ropa que tiene brazos propios (ya se maneja en show_arms)
                print(f">> {self.clothe} usa brazos personalizados")
                self.current_arms_pose = "custom"
                return False
            elif covers is False:
                # ropa normal → sí puedes cambiar pose
                self.current_arms_pose = pose_name
                return True                
            else:
                print(f">> ❌ Error: estos brazos no existen")
                return False


        def get_custom_arms(self, pose_name=None):
            """Ruta de brazos alternativos si la ropa usa brazos propios."""
            name = chr2_game.code
            pose = pose_name or self.current_arms_pose
            return f"character/{name}/arm/{pose}_arms.png"

        def show_arms(self, st, at):
            covers = self.covers_arms()
        
            if covers is True:
                return Null(width=1490, height=1890), 0  # brazos ocultos
            elif covers == "custom":
                return Image(self.get_custom_arms()), 0 # recurso para usar manos personalizados
            elif covers is False:
                name = chr2_game.code
                return Image(f"character/{name}/arm/{self.current_arms_pose}_arm.png"), 0
            else:
                print(f">> ❌ Error: estos brazos no existen")
                return False

        def __str__(self):
            return self.get_image_path()


# wrapper que resuelve la ropa al mostrar (evita error si azuli_clothe no existe aún)
init python:

    def show_clothe_wrapper(character_name):
        def inner(st, at):
            instance = getattr(store, f"{character_name}_clothe", None)
            if instance is not None:
                try:
                    return Image(instance.get_image_path()), 0
                except Exception:
                    return Null(1490,1890), 0
            return Null(1490,1890), 0
        return inner

    def show_arms_wrapper(character_name):
        def inner(st, at):
            instance = getattr(store, f"{character_name}_clothe", None)
            if instance is not None:
                try:
                    return instance.show_arms(st, at)
                except Exception:
                    return Null(1490,1890), 0
            return Null(1490,1890), 0
        return inner



# covers_arms: false → se muestran los brazos normales dinámicos.

# covers_arms: true → los brazos quedan ocultos (ropa los tapa).

# covers_arms: "custom" → la ropa trae sus propios brazos dibujados, los cargamos























# init python:

#     class SimpleClother(object):
#         def __init__(self, character, clothe, default_c, poses=1, pose=1):
#             self.character = character
#             self.clothe = clothe
#             self.default_c = default_c
#             self.pack = None
#             self.poses = poses
#             self.pose = pose  # por defecto pose 1

#         def load_pack(self):
#             try:   
#                 if self.pack is None:
#                     json_path = f"data_clothe_json/chr_library_clother_{self.character}.json"
#                     self.pack = JSON_(json_path)
#                 return self.pack
#             except Exception as e:
#                 return None
#             return self.pack

#         def set(self, new_clothe):
#             self.clothe = new_clothe

#             print(f"ahora {self.clothe} es {new_clothe}")

#         def set_pose(self, new_pose):
#             if 1 <= new_pose <= self.poses:
#                 self.pose = new_pose

#             print(f"ahora {self.pose} es {new_pose}")

#         def get_clothe_id(self):
#             """Devuelve la ropa correspondiente a la pose actual."""
#             # Si pose > 1, asumimos que se agrega "a", "b", etc.
#             if self.pose == 1:
#                 return self.clothe
#             else:
#                 suffix = chr(ord('a') + self.pose - 2)  # pose=2 → 'a', pose=3 → 'b'
#                 return f"{self.clothe}{suffix}"

#         def get_image_path(self):
#             # pack = self.load_pack()
#             name = chr2_game.code
#             clothe_id = self.get_clothe_id()
#             return self.pack.get(clothe_id, f"character/{name}/clouth/none_image.png")

#         def get_base(self):
#             name = chr2_game.code
#             if self.pose == 1:
#                 result = f"character/{name}/base/base.png"
#             elif self.pose == 2:
#                 result = f"character/{name}/base/base1a.png"

#             return result

#         def default_(self):
#             self.clothe = self.default_c
#             print("volver a default")

#         def __str__(self):
#             return self.get_image_path()






# init python:

#     class ChangeClothe(Action):
#         def __init__(self, target, value):
#             self.target = target   # objeto o variable que vamos a modificar
#             self.value = value     # nuevo valor que queremos poner

#         def __call__(self):
#             # cuando se ejecuta la acción
#             self.target.set(self.value)

#         # def get_sensitive(self):
#         #     # opcional, si quieres que siempre esté activo
#         #     return False

#         # def get_selected(self):
#         #     # opcional, si quieres marcar si está seleccionado
#         #     return self.target.get() == self.value









# screen wardrobe():
#     # tag wardrobe  # evita duplicados de screen

#     modal True

#     add "black" at Transform(alpha=0.89)

#     zorder 80



#     frame:
#         style "frame_5"
#         xalign 0.1
#         yalign 1.0
#         padding(20, 20)

#         vbox:
#             add [chr2_game.s_chr + " " + "happy"] at move_left_history


#     frame:
#         style "frame_7"
#         xalign 0.82
#         yalign 0.5
#         padding(125, 50)

#         vbox:
#             spacing 12

#             # text "Vestidor de [character_clother.character]" size 30 color "#fff"

#             # --- Previsualización del personaje --



#             # --- Selección de ropa ---
#             text "Selecciona ropa:"
#             vbox:
#                 spacing 10
#                 if chr2_game.s_chr == "azuli_":
#                     textbutton _("Normal"):
#                         style "button_cookie_1"
#                         action Function(azuli_clothe.set, "clothe1")

#                     textbutton _("Conejo"):
#                         style "button_cookie_1"
#                         action Function(azuli_clothe.set, "bunny1")

#                     textbutton _("Casual"):
#                         style "button_cookie_1"
#                         action Function(azuli_clothe.set, "casual1")

#                     textbutton _("Mesera"):
#                         style "button_cookie_1"
#                         action Function(azuli_clothe.set, "mese1")

#                     textbutton _("Mesera con manta"):
#                         style "button_cookie_1"
#                         action Function(azuli_clothe.set, "mese2")

#                     textbutton _("Fiesta"):
#                         style "button_cookie_1"
#                         action Function(azuli_clothe.set, "clothe3")

#                     textbutton _("Family Real"):
#                         style "button_cookie_1"
#                         action Function(azuli_clothe.set, "family_blue")


#             # --- Selección de pose ---
#             # text "Selecciona pose:" size 25 color "#fff"
#             # hbox:
#             #     spacing 10
#             #     for i in range(1, character_clother.poses+1):
#             #         textbutton str(i):
#             #             action character_clother.set_pose(i)

#             # --- Botón de cerrar ---
#             textbutton "Cerrar":
#                 action Hide("wardrobe")
#                 xalign 0.5




# init python:
    
#     # clother: nombre predeterminado
#     # tag: numeral o codec
#     # only: si es que no se repite el nombre

#     # clother + tag = clothe1

#     # clother + only=true = casual

#     def clother_config_(clother, tag, only=False):
#         global chr2_game





