

# r >> oro
# z >> special
# n >> normal
# w >> raro

init python:
    def warn_tsundere_z():
        levels = {
            8999: (14, True, 66),
            6999: (9, True, 27),
            4999: (8, True, 19),
            2999: (5, True, 13),
            0:    (5, True, 13),
        }

        for threshold in sorted(levels.keys(), reverse=True):
            if afecto.quantity > threshold:
                afecto.add_affection(*levels[threshold])
                break

        return "warn tsundere_z ✅"

    def warn_good_z():
        levels = {
            1700: {"affection": (10, True, 45), "love": 6, "good": 2},
            1200: {"affection": (9, True, 39), "love": 6, "good": 2},
            900:  {"affection": (9, True, 36), "love": 3, "good": 1},
            500:  {"affection": (9, True, 32), "love": 1, "good": 1},
            250:  {"affection": (9, True, 27), "love": 0, "good": 1},
            0:    {"affection": (9, True, 18), "love": 0, "good": 0},
        }

        # Buscar el nivel más alto aplicable
        for threshold in sorted(levels.keys(), reverse=True):
            if love_.quantity > threshold:
                data = levels[threshold]
                afecto.add_affection(*data["affection"])
                if data["love"] > 0:
                    love_.add_love(data["love"])
                if data["good"] > 0:
                    point_good.add(data["good"])
                break

        return "warn good_z ✅"

    def warn_child_z():
        afecto.add_affection(5, True, 30)
        return "warn child_z ✅"

    def warn_requirement_z(): # Requisito
        pass

    def warn_yandere_z(): # Yandere
        pass

    def warn_intelligent_z(): # Inteligencia
        pass

    def warn_resent_z(): # Tolerancia
        point_good.remove(10)
        point_bad.remove(10)
        levels = {
            10_000: (15, True, 55),
            8000: (15, True, 35),
            6000: (12, True, 24),
            4500: (8, True, 15),
            3500: (4, True, 11),
            2000: (1, True, 8),
            1000: (1, True, 5),
            0:    (1, True, 4),
        }
        for threshold in sorted(levels.keys(), reverse=True):
            if afecto.quantity > threshold:
                afecto.add_affection(*levels[threshold])
                break        

    def warn_secret_z():
        afecto.add_affection(50, True, 100)
        return "warn secret_z ✅"






init python:
    def warn_loving_r(): # amorosa
        if category_girl.get_quantity(loving_c):
            love_.add_love(1, True, 2)
            afecto.add_affection(5, True, 25)
            point_good.add(1)
        return "warn loving_r ✅"

    def warn_cook_r(): # cocinera
        if category_girl.get_quantity(cook_c):
            afecto.add_affection(5, True, 35)
            love_.add_love(1, True, 3)
        return "warn cook_r ✅"

    def warn_happy_r(): # feliz
        if category_girl.get_quantity(happy_c):
            if health_character.scale in ("2", "7"):
                afecto.add_affection(15, True, 35)
            else:
                afecto.add_affection(5, True, 15)
        return "warn happy_r ✅"

    def warn_disgust_r(): # asquerosa
        if category_girl.get_quantity(distrust_c):
            if health_character.scale == "8":
                afecto.add_affection(5, True, 20)
            else:
                afecto.add_affection(5, True, 15)
        return "warn disgust_r ✅"

    def warn_ambitious_r(use=1): # ambicioso
        global money_player, work_yeah, category_girl
        if not category_girl.get_quantity(requirement_c):
            if category_girl.get_quantity(ambitious_c):
                if use == 1:
                    if work_yeah == True:
                        afecto.add_affection(4, True, 10)
                        money_player.add_money(renpy.random.randint(2,  12))
                elif use == 2:
                    if work_yeah == True:
                        money_player.add_money(renpy.random.randint(2,  32))
                else:
                    try:
                        afecto.add_affection(4, True, 10)
                        print(f"Is action not use variable 1 or 2, requeriment OK")
                    except ValueError:
                        ValueError ("Valor indefinido ¿use? no registrado")
        return "warn ambitious_r ✅"

    def warn_confidence_r(): # confianza
        if category_girl.get_quantity(confidence_c):
            afecto.add_affection(10, True, 25)
        return "warn confidence_r ✅"




init python:
    def warn_joker_w():
        if category_girl.get_quantity(joker_c): # joker (aleatorio)
            if renpy.random.random() <= 0.5: # 50% de probabilidad
                renpy.sound.play("audio/sfx_d/sound_dificult_5.ogg", channel="sound")
                point_bad.add(renpy.random.randint(0, 1))
                point_good.add(renpy.random.randint(0, 1))
            else:
                afecto.add_affection(0, True, 3)

        return "warn joker_w ✅"

    def warn_cute_w():
        if category_girl.get_quantity(cute_c):
            afecto.add_affection(5, True, 20)
        return "warn cute_w ✅"

    def warn_normal_w():
        if category_girl.get_quantity(normal_c):
            afecto.add_affection(1, True, 10)
            love_.add_love(1, True, 5)
        return "warn normal_w ✅"

    def warn_lust_w():
        afecto.remove_affection(1, True, 4)
        return "warn lust_w ⚠️, este no deberia usarse"



init python:
    def warn_charismatic_n(): # carisma
        if category_girl.get_quantity(charismatic_c):
            if category_girl.get_quantity(joker_c):
                afecto.remove_affection(5, True, 55)
            else:
                afecto.add_affection(5, True, 25)
        return "warn charismatic_n ✅"

    def warn_foolish_n(): # tonta
        if category_girl.get_quantity(foolish_c):
            if category_girl.get_quantity(intelligent_c):
                afecto.add_affection(10, True, 40)
                point_good.add(2)
            else:
                afecto.remove_affection(0, True, 25)
                point_bad.add(2)
        return "warn foolish_n ✅"

    def warn_study_n(): # estudiosa
        global tele_character
        if category_girl.get_quantity(study_c):
            tele_character = False
            afecto.add_affection(15, True, 30)
        return "warn study_n ✅"

    def warn_hate_n(): # odio
        if category_girl.get_quantity(hate_c):
            if renpy.random.random() <= 0.5: # 30% de probabilidad
                afecto.remove_affection(60, True, 80)
                love_.remove_love(1, True, 3)
                point_bad.add(2)
            else:
                afecto.remove_affection(5, True, 20)
        return "warn hate_n ✅"

    def warn_otaku_n(): # otaku
        if category_girl.get_quantity(otaku_c):
            if category_girl.get_quantity(study_c):
                point_bad.add(1)
            else:
                tele_character = renpy.random.choice([True, False])
                afecto.add_affection(1, True, 5)
        return "warn otaku_n ✅"

    def warn_angry_n(): # enojada
        if category_girl.get_quantity(angry_c):
            if category_girl.get_quantity(good_c):
                point_bad.add(1)
            else:
                if renpy.random.random() <= 0.2:
                    afecto.remove_affection(15, True, 40)
                    point_bad.add(1)
                else:
                    afecto.remove_affection(1, True, 15)
        return "warn angry_n ✅"

    def warn_celos_n(): # celos
        if category_girl.get_quantity(celos_c):
            if category_girl.get_quantity(good_c):
                point_bad.add(1)
            else:
                if outside_home:
                    afecto.remove_affection(15, True, 55)
                else:
                    afecto.remove_affection(1, True, 9)
        return "warn celos_n ✅"

    def warn_distrust_n():  # Desconfianza
        if category_girl.get_quantity(distrust_c):
            if not category_girl.get_quantity(confidence_c):
                levels = {
                    12000: (0, True, 80),
                    10000: (0, True, 75),
                    8000: (0, True, 60),
                    6500: (0, True, 40),
                    4500: (0, True, 35),
                    8000: (0, True, 60),
                    6500: (0, True, 40),
                    4500: (0, True, 35),
                    2500: (0, True, 30),
                    0:    (0, True, 25),
                }
                for threshold in sorted(levels.keys(), reverse=True):
                    if afecto.quantity > threshold:
                        afecto.remove_affection(*levels[threshold])
                        break

        return "warn distrust_n ✅"





# Tiradas para ver qué opciones estarán disponibles
default r1_brave = 0

init python:

    def warn_brave_n(): # valiente
        global chr2_game
        if renpy.random.random() <= 0.2: # 20% de probabilidad
            renpy.jump("brave_" + chr2_game.s_chr)
        else:
            if afecto.quantity >= 2500:
                afecto.add_affection(1, True, 20)
        return "warn hate_n ✅"









# SYSTEMA DE PERSONALIDAD
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
    
    def Action_verify_fail_bug(bath=False, eat=False):
        """
        Verifica si falla cuando el jugador esta afuera, normalmente se encuentra en las necesidades
        de los personajes
        """
        global bath_character, eat_character, outside_home, point_bad
        Action_remove_need_fail()
        renpy.notify("Jumper Home")
        if dificulty_mode_game == "hard":
            point_bad.add(1, True, 7)
        else:   
            point_bad.add(1, True, 5)
        # outside_home = True
        if bath:
            bath_character = False   
            if outside_home == False:
                outside_home = True # por si acaso sucede inconveniente de valor
        if eat:
            eat_character = False  
            if outside_home == False:
                outside_home = True # por si acaso sucede inconveniente de valor


    def Action_remove_need_fail(affection_amount=10, love_amount=3):
        """
        Necesidad acumulativa para los personajes cuando fallan
        normalmente entra en sincronía con Action_verify_fail_bug()
        """
        global afecto, love_
        afecto.remove_affection(affection_amount, True, affection_amount*4)
        love_.remove_love(love_amount, True, love_amount*2+1)


    def Action_effect_status():
        """
        Esta acción aplica efectos según el estado de health_character.
        Normalmente se usa en los chats automáticos del personaje.
        """
        global health_character, afecto, love_, point_good, point_bad, dificulty_mode_game

        scale = health_character.scale

        # Casos simples definidos en un diccionario
        base_effects = {
            "10": ("good", 1, 2),
            "5":  ("bad", 1, 2),
            "2":  ("good", 1, 2),
            "7":  ("good", 1, 2),
            "4":  ("bad", 1, 2),
            "3":  ("bad", 1, 2),
        }

        if scale == "9":
            # Caso especial con dificultad
            if dificulty_mode_game == "hard":
                point_bad.add(7, True, 9)
                afecto.remove_affection(15, True, 25)
            elif dificulty_mode_game in ["easy", "pacific"]:
                point_bad.add(1)
                afecto.remove_affection(2, True, 5)
            else:
                point_bad.add(3, True, 5)
                afecto.remove_affection(10, True, 15)

        elif scale in base_effects:
            type_, quantity, limit_ = base_effects[scale]
            if type_ == "good":
                point_good.add(quantity, True, limit_)
            else:
                point_bad.add(quantity, True, limit_)


init python:
    def verify_object_status():
        """
        Se encarga de colocar algún estado diferente dependiendo del objecto que se le regalo
        al personaje. Normalmente se usa en los chats de regalos del personaje.
        """
        if inv_object.get_quantity("beer") or inv_object.get_quantity("vino"):
            health_character.config(10)
        elif inv_object.get_quantity("vino_ice"):
            health_character.config(10)



    def Action_effect_category():
        """
        Esta acción realiza una verificación para quitar algún estado que no se permita a la categoría
        como (bueno) y se (enoja), normalmente (bueno) no debería enojarse, se reintegra con un estado normal
        $ Action_effect_category() se activa sin nada
        """
        global health_character
        if category_girl.get_quantity(good_c):
            if health_character.scale == "4":
                health_character.config(1)
        elif category_girl.get_quantity(tsundere_c):
            if health_character.scale == "5":
                health_character.config(renpy.random.choice([1, 4]))
        elif category_girl.get_quantity(yandere_c):
            if health_character.scale in ("7", "2"):
                health_character.config(1)



# Action_effect_need_chr terminar codigo por errores tecnicos
