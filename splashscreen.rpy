


image splash_image = "gui/mark_logo.png"
image error_image = "gui/error/main_image_error.png"

label splashscreen:
    #$ required_files = check_required_files()
    if persistent.choice_game == True:
        scene black
        show splash_image:
            zoom 1.1 align(.5, .5)
        with dissolve
        $ renpy.pause(1.5, hard=True)
        scene black
        show logo_base at Transform(xalign=0.5, yalign=0.5, alpha=0.3, zoom=1.2)
        call screen select_language_fixed()


        my_centered "{size=+10}{color=#FF5555}⚠ ADVERTENCIA DE CONTENIDO ⚠{/color}{/size}"
        my_centered "Este juego aborda temas sensibles como autoestima, trauma emocional, luces parpadeantes, sonidos fuertes, consumo de sustancias y terror psicológico."
        my_centered "Ha sido creado con respeto y una intención emocional constructiva."
        my_centered "Todo es ficción lo cual no es real."
        my_centered "Todos los personajes representados son mayores de edad. No hay contenido que implique a menores."
        my_centered "Se recomienda para mayores de 16 años."
        my_centered "Al continuar, aceptas jugar bajo tu propio criterio y responsabilidad."
        menu:
            "¿Deseas continuar?"

            "Sí, continuar":
                $ persistent.choice_game = False
                pass
            "No, salir":
                $ persistent.choice_game = True
                $ renpy.quit()

        scene black
        with logo_scene
        $ renpy.pause(predict=True)
        return
    else:
        if not persistent.skip_splascreen_game:
            scene black
            show logo_base at Transform(xalign=0.5, yalign=0.5, alpha=0.3, zoom=1.2)
            with dissolve
            my_centered "{size=+10}{color=#FF5555}⚠ ADVERTENCIA DE CONTENIDO ⚠{/color}{/size}{nw=2.0}"
            my_centered "Este juego aborda temas sensibles como autoestima, trauma emocional, luces parpadeantes, sonidos fuertes, consumo de sustancias y terror psicológico.{nw=2.0}"
            my_centered "Se recomienda para mayores de 16 años.{nw=2.0}"
            scene black
            with dissolve
            $ renpy.pause(predict=True)
        else:
            scene black
            $ renpy.pause(predict=True)
        return
        






