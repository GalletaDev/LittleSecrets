# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# Al comienzo se crea una lista de amor y categorias
# las categoria afectan al personaje dependiendo las que tenga
# pueden ser varias dependiendo de lo que quiera el jugador


# The game starts here.


# netsuzō trap

label start:
    if persistent.language_box == "spanish":
        $ chr2_game.language_description_ = str("spanish")
    else:
        $ chr2_game.language_description_ = str("english")    

    $ _save_enable = False
    # $ _skip_enabled = False
    $ config.allow_skipping = True
    $ config.save = False

#########################################

#########################################
    #show screen LS_notify_screen()
    stop music fadeout 2.4
    with logo_scene
    $ renpy.pause(predict=True)
####### PARA DESARROLLADOR ######
    # show screen command_center_console()
    # show screen console_log()
    # show screen console_log_glitch()
#####################################
    $ name_music_m = renpy.random.choice(["selection_music"])
    label _return_menu_starts:

        $ chr2_game.Pack_reset(c_all=True)
        call screen selector_character()


# EL JUEGO NACIO EL 22/7/2024


label history_start_finish_azuli_:

    scene black
    with dissolve_scene_full

    $ renpy.free_memory() # obtiene casi 200MB de sobra... limpiamos para no usarlo
    # ya que al seleccionar estos recursos extras no se usaran mas, por eso no tiene sentido esa cantidad
    call screen loading_screen() 
    # pantalla de carga para esperar el predict de renpy. sin animaciones para que piense mejor
    ####################################
    # reiniciar dia
    $ current_day_name = name_day[(day - 1) % 7]
    $ azuli_clothe.load_pack()
    ####################################
    $ azuli_clothe.set("clothe1")
    $ mc_name = "Kris"
    ####################################
    python:
        #################################
        select_npc_shop = "miko_" # seleccionamos un npc para usarlo como otro personaje
        # aunque no sea jugable es para darle un poco de relleno el lugar
        npc_chr = "miko_"
        ##################################

        love_.name = "Azuli"
        #############################
        bot_character_key = chr2_game.s_chr #funciones del bot
        select_bot_character() # Selecciona el diccionario de las ubicaciones, 
        ##############################
        money_player.sims = "{image=money_euro}" # Símbolo de moneda

        #dependiendo de que personaje es. por eje "azuli_" usara los movimientos de azuli como base
        ###########################################################

        #  para dar las personalidades del personaje

        category_girl.add_category(good_c)
        category_girl.add_category(distrust_c)
        
        category_girl.add_action(good_c ,warn_good_z)
        category_girl.add_action(distrust_c ,warn_distrust_n)

        ###########################################################
        add_max_(2) # agregar limites

        #########################################################
        name_music_m = "one_day_more" # seleccionamos la musica

        ############################################################
        # agregar los recursos del jugador al empezar

        if dificulty_mode_game == "pacific":
            afecto.add_affection(200, notify=False)
            money_player.add_money(500, notify=False)
            money_player.add_up_money_day(100)
            point_random_try = 1.0
        elif dificulty_mode_game == "easy":
            afecto.add_affection(100, notify=False)
            money_player.add_money(350, notify=False)
            money_player.add_up_money_day(50)
            point_random_try = 1.0
        else:
            afecto.add_affection(25, notify=False)
            money_player.add_money(250, notify=False)
            point_random_try = 0.8


        if love_.quantity != 100:
            love_.add_love(100, notify=False)
            
        
        ##############################################################



    #call screen loading_screen()
    "complete...{nw}"
    $ _save_enable = True
    # $ _skip_enabled = True
    $ config.allow_skipping = True
    $ config.save = True
    $ active_console_default = True
    $ ACTIVE_BOT(active=True)

    if persistent.skip_tutorial_game:
        show screen help_tutorial()
    else:
        hide screen help_tutorial

    hide bg_game_just with dissolve
    # show screen console_view()

    call screen menu_option()










label history_start_finish_milia_:

    scene black
    with dissolve_scene_full

    $ renpy.free_memory() # obtiene casi 200MB de sobra... limpiamos para no usarlo
    # ya que al seleccionar estos recursos extras no se usaran mas, por eso no tiene sentido esa cantidad
    call screen loading_screen() 
    # pantalla de carga para esperar el predict de renpy. sin animaciones para que piense mejor
    ####################################
    # reiniciar dia
    $ current_day_name = name_day[(day - 1) % 7]
    ####################################
    $ milia_clothe.load_pack()


    $ milia_clothe.set("normal")
    $ mc_name = "Marco"
    ####################################
    python:
        #################################
        select_npc_shop = "miko_" # seleccionamos un npc para usarlo como otro personaje
        # aunque no sea jugable es para darle un poco de relleno el lugar
        npc_chr = "miko_"
        ##################################

        love_.name = "Milia"
        love_.quantity_max = 1500 # limite permitido
        #############################
        bot_character_key = "milia_" #funciones del bot
        select_bot_character() # Selecciona el diccionario de las ubicaciones, 
        ##############################

        money_player.sims = "{image=money_euro}" # Símbolo de moneda


        #dependiendo de que personaje es. por eje "azuli_" usara los movimientos de azuli como base
        ###########################################################

        #  para dar las personalidades del personaje

        category_girl.add_category(resent_c)
        category_girl.add_category(confidence_c)
        
        category_girl.add_action(resent_c ,warn_resent_z)
        category_girl.add_action(confidence_c ,warn_confidence_r)

        ###########################################################
        add_max_(2) # agregar limites

        #########################################################
        name_music_m = "one_day_more" # seleccionamos la musica

        ############################################################
        # agregar los recursos del jugador al empezar

        if dificulty_mode_game == "pacific":
            afecto.add_affection(200, notify=False)
            money_player.add_money(500, notify=False)
            money_player.add_up_money_day(100)
            point_random_try = 1.0
        elif dificulty_mode_game == "easy":
            afecto.add_affection(100, notify=False)
            money_player.add_money(350, notify=False)
            money_player.add_up_money_day(50)
            point_random_try = 1.0
        else:
            afecto.add_affection(25, notify=False)
            money_player.add_money(250, notify=False)
            point_random_try = 1.0


        if love_.quantity != 100:
            love_.add_love(100, notify=False)

    "complete...{nw}"
    $ _save_enable = True
    # $ _skip_enabled = True
    $ config.save = True
    hide bg_game_just with dissolve
    # show screen console_view()
    call screen menu_option()


label history_cristal_:

    call screen confirm(message=_("Este personaje esta en desarrollo.\n ¿quieres apoyar al creador para que tenga las fuerzas de terminarlo?"),
        yes_action=Return(True), no_action=Return())
    return



label history_blody_:

    call screen confirm(message=_("Este personaje esta en desarrollo.\n ¿quieres apoyar al creador para que tenga las fuerzas de terminarlo?"),
        yes_action=Return(True), no_action=Return())
    return






label history_pink_:
    # stop music fadeout 3.0
    # scene black
    # with dissolve_scene_full
    # #$ renpy.pause(1, hard=True)
    # #call screen loading_screen(led=8.0)
    # ####################################
    # # cargar imagenes de ropas
    # #$ azuli_clothe.load_pack()
    # #$ azuli_clothe2.load_pack()

    # $ renpy.free_memory()
    # call screen loading_screen()

    # #$ azuli_clothe.set("clothe1")
    # #$ azuli_clothe2.set("clothe1a")

    # ####################################
    # python:

    #     love_.name = "Pink"
    #     love_.quantity_max = 1000

    #     bot_character_key = "pink_"
    #     money_player.sims = "{image=money_dollar}"
    #     list_select_protagonist = 10
    #     point_random_try = 0.96
    #     select_bot_character()
    #     ###########################################################

    #     #  para dar las personalidades del personaje

    #     category_girl.add_category(secret_c)
    #     category_girl.add_action(secret_c ,warn_secret_z)

    #     ###########################################################
    #     add_max_(1) # agregar limites

    #     #########################################################
    #     name_music_m = "one_day_more"

    #     ############################################################
    #     # agregar los recursos del jugador al empezar
    #     love_.add_love(1000)
            
    #     money_player.add_money(1000)
    #     money_player.add_up_money_day(200)

    # hide bg_game_just with dissolve
    # show screen console_view()
    # call screen menu_option()

    return
















label history_:
    show screen notify_message_error(message=_("Debes seleccionar un personaje"))
    $ renpy.pause(.5, hard=True)
    call screen selector_character()