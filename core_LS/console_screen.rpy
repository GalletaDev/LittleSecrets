


screen console_log():


    zorder 999

    frame:
        style "frame_5"
        align(0.0, 0.0)
        padding(20, 20)
        #xysize(550, 300)
        vbox:
            text "{size=18}MusicSFX:[name_music_m]{/size}"


    frame:
        background Solid("#111111DD")  # Negro con opacidad
        xsize 550
        ysize 200
        align (0.98, 0.02)  # Esquina superior derecha
        padding(10, 10)

        viewport:
            mousewheel True
            scrollbars "vertical"
            draggable True
            vbox:
                for cache_data in activited_history:
                    text "activited_history:[cache_data]" size 12









init -99 python:
    activited_history = []# Lista de actividades
    activited_log_visible = False # Control de visibilidad

    def toggle_activited_log():
        global activited_log_visible
        activited_log_visible = not activited_log_visible
        if activited_log_visible:
            renpy.show_screen("console_log")
        else:
            renpy.hide_screen("console_log")

    def register_log(texto):
        activited_history.append(texto)
        if len(activited_history) > 100:
            activited_history.pop(0)



screen command_center_console():
    key "K_TAB" action ToggleScreen("console_log")














# efecto glitch




screen console_log_glitch():

    zorder 999

    timer renpy.random.random() action Function(start_glitch) repeat True

    frame:
        background Solid("#1111117e")  # Negro con opacidad
        xsize 550
        ysize 200
        align (1.0, 0.0)  # Esquina superior derecha
        padding(10, 10)

        viewport:
            yinitial 1.0
            # mousewheel True
            # scrollbars "vertical"
            # draggable True
            vbox:
                for cache_data in activited_glitch:
                    text "[cache_data]" size 16


init -99 python:
    activited_glitch = []# Lista de actividades
    activited_log_gl_visible = False # Control de visibilidad
    # math.pi = 3.14
    # math.e = 2.71

    def toggle_activited_log():
        global activited_log_gl_visible
        activited_log_gl_visible = not activited_log_gl_visible
        if activited_log_gl_visible:
            renpy.show_screen("console_log_glitch")
        else:
            renpy.hide_screen("console_log_glitch")

    def register_log(texto):
        activited_glitch.append(texto)
        if len(activited_glitch) > 15:
            activited_glitch.clear()

    def glitch_tick():

        random = str(renpy.random.random())

        activited_glitch.append(f"{{color=#ff0000}}Python{{/color}}:{random}")
        if len(activited_glitch) > 16:
            activited_glitch.pop(0)
            activited_glitch.clear()


        # vuelve a llamarse a sí mismo
        # renpy.timeout(0.05)  # cada 0.05s

    def start_glitch():
        glitch_tick()