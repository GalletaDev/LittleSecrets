



init python:
    # Tu lista base de funciones
    base_test_functions = [
        warn_joker_w, 
        warn_cute_w, 
        warn_normal_w,
        warn_lust_w,
        warn_charismatic_n,
        warn_foolish_n,
        warn_study_n,
        warn_hate_n,
        warn_otaku_n,
        warn_angry_n,
        warn_celos_n,
        warn_distrust_n,
        warn_brave_n,
        warn_loving_r,
        warn_cook_r,
        warn_happy_r,
        warn_disgust_r,
        warn_ambitious_r,
        warn_confidence_r,
        warn_tsundere_z,
        warn_good_z,
        warn_child_z,
        warn_secret_z
    ]

    # Convertimos cada función en un diccionario con nombre, referencia y estado
    test_functions = [
        {"name": func.__name__, "func": func, "done": False, "result": None}
        for func in base_test_functions
    ]

    current_test_index = 0

    def run_next_test():
        global current_test_index, test_functions
        if current_test_index < len(test_functions):
            entry = test_functions[current_test_index]
            result = entry["func"]()
            entry["done"] = True
            entry["result"] = result
            current_test_index += 1
            # renpy.restart_interaction()  # 🔥 refresca la screen
            return f"{entry['name']} → {result}"
        else:
            # renpy.restart_interaction()  # 🔥 refresca la screen
            return "✅ Todas las funciones ya fueron probadas."



screen log_test_func():
    
    modal True

    timer 1.5 action Function(afecto.add_affection, 1) repeat True

    $ run_next_test()

    frame:
        align (0.5, 0.5)
        padding(40, 20)
        vbox:
            text "Tester de funciones"

            # Muestra todos los resultados en una caja con scroll
            viewport:
                draggable True
                mousewheel True
                ysize 200
                vbox:
                    for entry in test_functions:
                        $ status = "✔️" if entry["done"] else "⏳"
                        $ result = entry["result"] if entry["result"] else ""
                        text f"{status} {entry['name']} {result}"

            # textbutton "Ejecutar siguiente función" action Function(run_next_test)
            textbutton "Cerrar" action Return(True)








label test_menu:

    "prueba"

    scene black
    $ love_.add_love(9999, notify=False)
    $ afecto.add_affection(9_9999, notify=False)

    # call screen log_test_func()
    # si quieres dar tiempo
    # menu(timer=5.0, label_timer="temporal_s"):
    #     "perro":
    #         pass

    #     "Gato":
    #         pass

    #     "Gato":
    #         pass

    #     "Gato":
    #         pass

    #     "Gato":
    #         pass

    #     "Gato":
    #         pass

    

label temporal_s:

    # show azuli_ death_gl1 at mov_glitch

    # call screen glitch_blocks()

    pause 2.5
    # hide screen glitch_blocks

    "prueba 2"

    return    