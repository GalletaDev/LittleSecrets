
###########################################################################

###########################################################################


# default action_counter = {}

init python:

    available_actions = ["cook", "rps", "talk", "sleep", "b_choice", "ignored"]

    class ActionCounter(object):
        def __init__(self, dictionary=available_actions):
            self.list_use_available = dictionary
            self.action_counter = {}
            self.ensure_keys()

        def __getstate__(self):
                return {
                    "list_use_available": self.list_use_available,
                    "action_counter": self.action_counter,
                }

        def __setstate__(self, state):
            self.list_use_available = state.get("list_use_available", available_actions)   # valor por defecto
            self.action_counter = state.get("action_counter", {})
            self.ensure_keys()


        def ensure_keys(self):
            for key in self.list_use_available:
                self.action_counter.setdefault(key, 0)

        def add(self, action_name, quantity=1):
            if action_name not in self.list_use_available:
                print(f"La acción '{action_name}' no está disponible.")
                return
            self.action_counter[action_name] = self.action_counter.get(action_name, 0) + quantity

        def get(self, action_name):
            return self.action_counter.get(action_name, 0)

        def get_str(self, action_name):
            return f"{action_name} ({self.get(action_name)})"

        def reset(self, action_name):
            if action_name in self.action_counter:
                self.action_counter[action_name] = 0
            else:
                renpy.notify(f"La acción '{action_name}' no existe.")

        def reset_all(self):
            for key in self.action_counter:
                self.action_counter[key] = 0

        def reset_some(self, actions):
            for a in actions:
                if a in self.action_counter:
                    self.action_counter[a] = 0
###########################################################################

###########################################################################

















###########################################################################
# Otros ejemplos de acciones:
###########################################################################
init python:
    def check_need_verify_tele(bot=False):
        """This is a function
        check_need_verify_tele(bot=False)
        Verifica si hay algun bonificador en valor tele_character
        Args:
            bot (bool): Indica si se está usando un bot. Por defecto False.
        Returns:
            bool: True si necesita verificación, False si no.
        """
        # Ajusta la cantidad de afecto y amor según el estado del personaje
        ACTIVE_BOT(active=bot)
        # Actualizar afecto y amor
        if tele_character:
            ###################################
        #### Bonificadores
            if health_character.scale == "9":
                renpy.music.play("audio/sfx/fail.ogg", channel='sound')
                afecto.remove_affection(25, True, 40)
                love_.remove_love(1, True, 3)
                point_bad.add(5)
            elif health_character.scale == "10":
                renpy.music.play("audio/sfx/affection_sound.ogg", channel='sound')
                afecto.add_affection(25, True, 30)
                point_good.add(25)

            if category_girl.get_quantity(requirement_c):
                renpy.music.play("audio/sfx/alerta.ogg", channel='sound')
                afecto.remove_affection(44, True, 90)
                love_.add_love(2, True, 5)
            elif category_girl.get_quantity(study_c):
                renpy.music.play("audio/sfx/alerta.ogg", channel='sound')
                afecto.remove_affection(12, True, 60)
                love_.remove_love(1, True, 4)
            elif category_girl.get_quantity(otaku_c) and not category_girl.get_quantity(study_c):
                renpy.music.play("audio/sfx/alerta.ogg", channel='sound')
                afecto.add_affection(12, True, 32)
                love_.add_love(2, True, 4)
            ####
                ##############################
            afecto.add_affection(15, True, 30)
            love_.add_love(1, True, 6)

            # Determinar etiqueta de salto
        label_prefix = "yes_character_tele_" if tele_character else "not_character_tele_"
        renpy.jump(label_prefix + chr2_game.s_chr)


    def check_need_verify_bath(bot=False):
        """This is a function
        check_need_verify_bath(bot=False)
        Verifica si hay algun bonificador en valor bath_character
        Args:
            bot (bool): Indica si se está usando un bot. Por defecto False.
        Returns:
            bool: True si necesita verificación, False si no.
        """
        # Obtener valores según el estado o usar el valor por defecto
        ACTIVE_BOT(active=bot)
        if bath_character:
            ###################################
        #### Bonificadores 
            #if category_girl.get_quantity(requirement_c): EJEMPLO
                #return None
            if category_girl.get_quantity(disgust_c) and not category_girl.get_quantity(good_c):
                renpy.music.play("audio/sfx/alerta.ogg", channel='sound')
                afecto.remove_affection(55, True, 85)
                love_.add_love(7, True, 12)
                point_bad.add(10)
            elif category_girl.get_quantity(angry_c) and not category_girl.get_quantity(good_c):
                tele_character = False
                renpy.music.play("audio/sfx/alerta.ogg", channel='sound')
                afecto.remove_affection(65, True, 90)
                love_.add_love(8, True, 14)
        ####
            ##############################
        # Actualizar afecto y amor
            afecto.add_affection(22, True, 30)
            love_.add_love(1, True, 7)
        else:
            pass

        label_prefix = "yes_character_bath_" if bath_character else "not_character_bath_"
        renpy.jump(label_prefix + chr2_game.s_chr)



    def check_need_verify_eat(bot=False):
        """This is a function
        Args:
            bot (bool): Indica si se está usando un bot. Por defecto False.
        Returns:
            check_need_verify_eat: evaluar bonificadores en valor eat_character
        """
        # global BOT_CHR
        ACTIVE_BOT(active=bot)
        if eat_character:
            ###################################
        #### Bonificadores 
            #if category_girl.get_quantity(requirement_c): EJEMPLO
                #return None
            if category_girl.get_quantity(angry_c) > 0:
                renpy.music.play("audio/sfx/alerta.ogg", channel='sound')
                afecto.remove_affection(65, True, 90)
                love_.add_love(8, True, 14)
        ####
            ##############################
        # Actualizar afecto y amor
            afecto.add_affection(8, True, 30)
            love_.add_love(1, True, 4)
        else:
            pass


init python:

    def Action_effect_need_chr():
        global category_girl, health_character, afecto, lujuria
        if health_character.scale == "2":
            afecto.add_affection(5, 10)
        elif health_character.scale == "7":
            afecto.add_affection(15, 25)
        elif health_character.scale in ("5", "4"):
            afecto.remove_affection(12, 25)
        elif health_character.scale == "9":
            afecto.remove_affection(1, 5)    
        else:
            pass
###########################################################################

###########################################################################