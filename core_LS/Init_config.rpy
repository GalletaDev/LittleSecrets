
init offset = -1

init python:
    import random, math, json, os, re, store
    import time as tp
    import pygame
    import csv


init python:
    # Glitch text generator
    nonunicode = "¡!¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
    binario = "01"
    python_codec = [
        "self", "if", "else", "elif", "True", "False", "class", "def", "global", "eval", "range",
        "for", "in", "is", "self.action", "*=2", "+=2", "-=2", "return?", "eval+", "value=D + r",
        "while True", "while False", "if not value:", "if value != 2:", "math", "1e-9", "math.pi",
        "Numpy", "list", "keys", "random.randint", "random.random", "random.choice", "Renpy", "Python",
        "Pygame", "JSON"
    ]

    # Glitch text generator
    def glitchtext(length: str, in_binario: bool = False, in_codec: bool = False):
        output = ""
        if in_binario:
            for x in range(length):
                output += renpy.random.choice(binario) 
                return output  
        if in_codec:
            output = " ".join(renpy.random.sample(python_codec, 4))
            return output  

        for x in range(length):
            output += renpy.random.choice(nonunicode)
        return output


########################################################

init python:

    # CONFIG SYSTEM
    def go_to(label_name="nothing"): 
        """
        Se encarga de volver predeterminado las acciones o desactivar el bot
        cuando no tiene a ningun label en su diccionario puede que solo desactive valores de BOT-CHR
        label start:
            $ go_to("label_name")
        """
        if label_name == "nothing":
            ACTIVE_BOT(active=False)
        else:
            char_name = chr2_game.s_chr  # por ejemplo "azuli_"
            if char_name in scene_labels_all and label_name in scene_labels_all[char_name]:
                info = scene_labels_all[char_name][label_name]
                for var, val in info.items():
                    setattr(renpy.store, var, val)
            renpy.jump(label_name)

    # MENU DYNAMIC
    def menu_dynamic_menu(choices):
        menu_items = []

        for cid, ctext in choices:
            menu_items.append((ctext, cid))

        result = renpy.display_menu(
            menu_items,
            interact=True,
            screen="choice",
            type="menu",
            _kwargs={
                "timer": 12.0,
                "label_timer": "fail_choice_" + chr2_game.s_chr
            }
        )
        return result

    def randomize_types_choice(data, book=None):
        for key in data:
            t, impact = random.choice(book)
            data[key]["type"] = t
            data[key]["impact"] = impact


    def available_choice_text(key):
        texts = {
            "pos": [
                _("Me gusta pasar tiempo contigo."),
                _("Contigo me siento tranquilo."),
                _("Eres importante para mí."),
                _("Te brillan los ojos, bonito la verdad."),
                _("Creo que eres perfecta."),
                _("¿Que te digo? eres hermosa igual como eres"),
                _("¿No te dijeron una vez que eres guapa?"),
                _("Si miras al espejo, veo tu reflejo, lo cual me pone loco de lindura.")
            ],
            "neg": [
                _("A veces eres muy rara."),
                _("No me siento cómodo contigo."),
                _("Me incomodas un poco."),
                _("¿Que te digo?"),
                _("Pecho pequeño..."),
                _("Creo que estas incomodando mucho"),
                _("Oh no, eres tu..."),
                _("Camina, camina, que aun ni corres.")
            ],
            "neu": [
                _("No sé qué decir."),
                _("Carpintero."),
                _("Que chulada de buey."),
                _("Ta feo la latina"),
                _("¿Que pasa, se te cayo una moneda de oro?"),
                _("Lol"),
                _("Harre, harre mi caballito"),
                _("Oyes eso, !presiento tu alma malvada¡"),
                _("Odio el agua, por que no sabe nada."),
                _("La cucaracha bailo como si no fuera otro día"),
                _("Presiento cosas, y es mi estomago...")
            ]
        }
        return renpy.random.choice(texts[key])

    def select_menu_collection(data):
        result = []
        for key, info in data.items():
            text = available_choice_text(info["type"])
            result.append((key, text))
        return result





init python:
    def btn(name, action, alt=None, activate=None):
        return {
            "name": name,
            "auto": "gui/button_config_screen/button_%s_%%s.png" % name,
            "action": action,
            "alt": alt,
            "activate": activate,
        }




init python:
    scene_labels_all = {
        "azuli_": {
            "location_azuli_living_room": {"BOT_CHR": False},
            "location_azuli_kitchen": {"BOT_CHR": False},
            "location_azuli_bath": {"BOT_CHR": False},
            "location_azuli_room": {"BOT_CHR": False},
            "function_fail_bath_azuli_": {"BOT_CHR": False},
            "function_fail_eat_azuli_": {"BOT_CHR": False},
            "select_dialog_azuli_pet": {"BOT_CHR": False},
            "call_screen_center_menu_option": {"BOT_CHR": True},
        }
    }





init python:
    # CONFIG SYSTEM
    def Action_CONFIG():
        """
        Verifica y refresca varias funciones a la vez como expresiones
        estado, bot, str_verify_name ect...
        Se usa mas para refrescar los valores que muestran en pantalla
        """
        global name_music_m, ex_chr, health_character, BOT_CHR, outside_girl, pos_chr, warning_love, day_already_configured, expression_face_

        # outside_home = True

        if time_p.hora > 10:
            day_already_configured = False

        if love_.quantity <= warning_love:
            name_music_m = "tension"
            ex_chr = "death"
            BOT_CHR = outside_girl
            health_character.config(3)
            str_verify_name()
        else:
            
            # if not BOT_CHR:
            #     expression_face_ = True

            if expression_face_:
                BOT_CHR = outside_girl
                expresion_refresh()
                

            str_verify_name()

            fase = time_p.fase_dia
            if fase in ("day", "day2"):
                name_music_m = "one_day_more"
            elif fase in ("afternoom", "afternoom2"):
                name_music_m = "one_afternoom_more"
            elif fase in ("night", "night2", "night3"):
                name_music_m = "one_night_more"






init python:

    # LOW AFFECTION SYSTEM
    def Action_low_affection_verify():
        """
        Verifica si el afecto supera los limites permitidos.
        dependiendo de la dificultad puede quitar mas
        también puede que vuelva integrar algunas variables como:
        - sleep_character
        - night_red
        - tele_character 
        - gift_true_confirm
        """
        global afecto, love_, sleep_character, night_red, tele_character, gift_true_confirm, warning_affection_max, outside_girl
        if afecto.quantity <= 2500:
            if category_girl.get_quantity(resent_c):
                pass
            else:
                if afecto.quantity >= warning_affection_max:
                    if dificulty_mode_game == "hard":
                        renpy.music.play("audio/sfx/warning.ogg", channel="sound")
                        love_.remove_love(50, True, 50)
                    else:
                        love_.remove_love(5, True, 15)
                else:
                    if dificulty_mode_game == "pacific":
                        love_.remove_love(2, True, 2)
                    elif dificulty_mode_game == "easy":
                        love_.remove_love(2, True, 4)
                    else:
                        love_.remove_love(2, True, 5)


        sleep_character = False
        night_red = False
        tele_character = random.choice([True, False])
        gift_true_confirm = False


# DEATH SYSTEM
init python:

    def check_love_status():
        global category_girl

        if love_.quantity <= 0:
            if category_girl.get_quantity(yandere_c):
                renpy.jump("mode_death_yandere")
            else:
                renpy.jump("mode_death_" + chr2_game.s_chr)



init python:
    def bonus_active_general():
        global select_ok_appointent, npc_gift_ok, var_name, expression_face_, point_bad, point_good
        """
        Aquí se pueden agregar bonificaciones y reinicio de valores para el juego
        point_good.remove(renpy.random.randint(20, 50))
        point_bad.remove(renpy.random.randint(20, 50))
        """
        point_good.quantity = 0
        point_bad.quantity = 0
        warn_ambitious_r(int(renpy.random.randint(2, 8)))

        var_name = "memory_gift_" + chr2_game.s_chr
        expression_face_ = True
        var_name = 0 # cada personaje puede tener variables únicos

        Action_CONFIG()
        verify_chair_npc()
        select_ok_appointent = False
        npc_gift_ok = False        





# DAY AND WEEK SYSTEM
init python:

    def Action_Verify_day():
        """
        verifica en que dia esta el juego y refresca los valores que se muestran en pantalla
        también al acabar la semana aumenta la cantidades maxima de amor y afecto
        también cambia la variable de tiempo en el mapa variables que usa:
        - day = 1
        - week = 1
        - time_global_ = renpy.random.choice(["normal", "rain", "rain_force"])
        - una que otra function en python
        """
        global day, week, day_beach_activate, activate_night_red, time_global_, current_day_name

        time_global_ = renpy.random.choice(["normal", "rain", "rain_force"])

        if day in (1, 2, 3):
            day +=1
        elif day == 4:
            #day_beach_activate = True
            day +=1
        elif day == 5:
            #day_beach_activate = False
            day +=1
        elif day == 6:
            #activate_night_red = True
            day +=1
        elif day >= 7:
            #activate_night_red = False
            week +=1
            day = 1
            if dificulty_mode_game == "pacific":
                update_max_affection()
            elif dificulty_mode_game == "easy":
                update_max_affection()
                update_max_love()                
            elif dificulty_mode_game == "normal":
                update_max_affection()
                update_max_love()
            else:
                update_max_love(75)
                update_max_affection(250)
                
        current_day_name = name_day[(day - 1) % 7]
        renpy.jump("week_config")



###########################################################################

###########################################################################

define HEALTH_S_1 = {
    "5": "dissa",
    "7": "happy",
    "2": "happy",
    "9": "loss",
    "8": "hot",
    "10": "ah"
    }


# HEALTH SYSTEM
init python:
    
    def expresion_refresh(update=True):
        """
        expresion_refresh funciona para refrescar las expresiones de los personajes.
        se usa mas para funciones en sincronía con otro
        label start:
            $ expresion_refresh()
        """
        global ex_chr, health_character, HEALTH_S_1

        if health_character.get_scale() == "3":
            health_character.config(1)

        ex_chr = HEALTH_S_1.get(health_character.get_scale(), "normal")
        return None

###########################################################################

###########################################################################

init python:

    def location_move_animation():
        """
        Actualiza la animación del bot según el estado de movimiento y la variable again_animation.

        Variables globales utilizadas:
        - pos_chr: Define la posición/animación actual del bot.
        - again_animation: Controla si la animación de entrada 'slide_left' debe ejecutarse.
            1 → ejecutar slide_left una vez, luego poner a 0
            0 → posición normal 'left'
        - moving_to_player: Flag que indica si el bot está realizando un movimiento hacia el jugador.
            True → ejecutar animación
            False → no hacer nada
        """
        global pos_chr, again_animation, again_animation_exit
        global moving_to_player, bot_is_exiting
        global location_house, location_character

        # Si la animación ya se ha gastado, aseguramos que quede en posición 'left'
        if again_animation == 0:
            pos_chr = "left"

        # 1️⃣ ——— SI NO ESTÁ HACIENDO NADA → LEFT
        if not moving_to_player:
            pos_chr = "left"
            return None

        # Aplicar animación de entrada si corresponde
        if love_.quantity >= 50:
            if again_animation == 1:
                if location_house == "living_room" and location_character in ["living_room", "kitchen", "bath", "room"]:
                    pos_chr = "slide_left"
                elif location_house == "room" and location_character in ["bath", "living_room", "kitchen", "room"]:
                    pos_chr = "slide_right"
                else:
                    pos_chr = renpy.random.choice(["slide_right", "slide_left"])
                    
                again_animation = 0
                # again_animation_exit = 0

            else:
                pos_chr = "left"

        # Resetear flag de movimiento
        moving_to_player = False

###########################################################################

###########################################################################


init python:
    def get_position_character():
        """
        Condición que se usa para animaciones en screen
        """
        position_animation = position_mapping.get(pos_chr, None)
        return position_animation


###########################################################################

###########################################################################


init python:
    def get_bot_active_timer():
        """
        activator y detector de comandos de bot, activa y desactiva automáticamente.
        """
        global last_player_location, bot_timer_ready, location_house
        last_player_location = location_house
        bot_timer_ready = True
        return bot_timer_ready



###########################################################################

###########################################################################

init python:
    def update_max_love(add=50):
        """
        Aumenta la cantidad máxima de amor alcanzable.
        Esto se puede pasar un número adicional para aumentar la cantidad máxima de peligro de amor.
        label start:
            $ update_max_love(77)
            return
        """
        global warning_love, warning_love_max
        if warning_love >= warning_love_max:
            warning_love = warning_love_max
        else:
            warning_love += add


###########################################################################

###########################################################################


init python:

    def update_max_affection(add=1000):
        """
        Aumenta la cantidad máxima de amor alcanzable.
        Lo mismo sucede con amor aquí, pero con afecto aumenta las cantidades maxima de peligro con afecto
        label start:
            $ update_max_affection(2000)
            return
        """
        global afecto, warning_affection_max
        if warning_affection_max >= afecto.quantity_max:
            warning_affection_max = afecto.quantity_max
        else:
            warning_affection_max += add



init python:
    def choose_dialog_label(chr_id, health_scale, outside_girl):
        """
        Devuelve el label adecuado basado en el estado actual.
        """
        # 10% de probabilidad de diálogo vacío
        if renpy.random.randint(1, 10) == 1:
            return f"dialog_none_{chr_id}"

        # Determinar rango de número aleatorio base
        random_min = renpy.random.randint(1, 8)

        # Decidir tipo de diálogo según situación
        if health_scale == "8":
            return f"dialog_hot_{chr_id}{renpy.random.randint(1, 5)}"
        elif health_scale == "5":
            return f"dialog_sad_{chr_id}{renpy.random.randint(1, 3)}"
        elif health_scale == "10":
            return f"dialog_drunk_{chr_id}{renpy.random.randint(1, 10)}"

        # Si no aplica condición de salud
        # if not outside_girl and location == "park":
        #     return f"dialog_ext_{chr_id}{renpy.random.randint(random_min, 16)}"

        return f"dialog_ext_{chr_id}{renpy.random.randint(random_min, 16)}"


    def ACTIVE_BOT(active=True, verify_day=False):
        """
        Funciona para activar algunas variables o desactivar con ACTIVE_BOT(active=False)
        y si es de verify_day=True para asi desactivar la consola_view temporalmente
        label start:
            $ ACTIVE_BOT() 
            return
        """
        global BOT_CHR, expression_face_, again_animation, again_animation_exit

        if active:
            BOT_CHR = True
            expression_face_ = True
            again_animation = 1
            again_animation_exit = 1
        else:
            BOT_CHR = False
            expression_face_ = False

    def chr_pos_default(expression_character="chat", pos_character="mid", expression_choice=True):
        """
        esta función se encarga de show a bg_and_character y al mismo tiempo coloca al centro
        el personaje y pone una expression predeterminada que puede cambiar
        label start:
            $ chr_pos_default("happy", "mid")
            return
        """
        global pos_chr, ex_chr

        renpy.show_screen("bg_and_character")
        pos_chr = pos_character
        if expression_choice:
            ex_chr = expression_character


    def bonification_win_character():
        global point_good, afecto, love_, eat_character, bath_character, name_music_m
        """
        al terminar la cita con el personaje, se da bonificaciones y desactiva algunas funciones
        como comer y bañar al personaje
        label start:
            $ bonification_win_character()
            return
        """
        afecto.add_affection(250)
        love_.add_love(20)
        point_good.add(25)
        name_music_m = "one_night_more"
        chr_pos_default(expression_character="happy", pos_character="mid")
        eat_character = False
        bath_character = False

    def Reset_end_appointment():
        global location_choice_map, outside_girl, outside_home, active_console_default
        """
        al terminar la cita con el personaje, se reinicia algunas variables
        como el uso de ACTIVE_BOT
        label start:
            $ Reset_end_appointment()
            return
        """
        location_choice_map = "house"
        ACTIVE_BOT(active=True)
        outside_girl = True
        outside_home = True
        active_console_default = True        


    def Exit_resets_value():
        global outside_home, pos_chr, outside_exit_house_, pass_bot_time, time_p
        """
        Normalmente se encarga de reiniciar o acoplar varios valores
        para asi integrarlos en ese momento en concreto. puede que aparezca en el boon de exit o salida
        label start:
            $ Exit_resets_value()
            return
        """
        outside_home = False
        pos_chr = None
        go_to()
        outside_exit_house_ = True
        pass_bot_time = 0
        time_p.add_time(1)
        

##############################################################################



default list_select_protagonist = 1

init python:
    def dialog_extra_mode_history_player():
        global list_select_protagonist
        if str(chr2_game.s_chr) in player_dialog_available:
            if list_select_protagonist < 7 and not mode_infinity_game:
                list_select_protagonist += 1
                return "protagonist_" + str(list_select_protagonist) + "_" + chr2_game.s_chr
            else:
                return "day_config_end"
        else:
            # personaje personalizado o no disponible
            return None






##############################################################################

default name_p = ""
default wiki_log_text = wiki_log_0

init python:

    def logic_id_wiki(tips):
        global name_p, wiki_log_text
        name_p = tips


    def select_dialog_(dialog_t):
        global wiki_log_text
        wiki_log_text = dialog_t





############################################################### 

# LOGIC LIMIT BAR AFFECTION AND LUST

# default lust_max = 250
default affection_max = 1250

init python:
    def affection_limit_add():
        global affection_max, afecto

        if afecto.quantity > affection_max:
            if afecto.quantity >= afecto.quantity_max:
                affection_max = afecto.quantity_max
            else:
                affection_max *= 2
                print(f"Limit up cant/x2 total")
        else:
            pass






###################################################################################################

# QUANTITY LOVE, AFFECTION AND LUST

default persistent.record_love_d = 0
default persistent.record_affection_d = 0
default persistent.record_lust_d = 0
default persistent.record_money_d = 0
default persistent.logro_player_game = []


############################################################################################################






####################################################################


# RANDOM DIALOG SYSTEM
default current_dialog = ""

init python:
    def update_cookie_random(dialog_list):
        global current_dialog
        current_dialog = renpy.random.choice(dialog_list)

    def select_dialog_by_index(dialog_list, index):
        global current_dialog
        current_dialog = dialog_list[index]

    def update_chocolate_random():
        global current_number
        current_number = renpy.random.randint(1, 5)


##############################################################


