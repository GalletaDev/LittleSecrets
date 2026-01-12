







init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("audio/bg_end_love.ogg", always_unlocked=True)
    #mr.add("audio/bg_life_happy_remix.ogg", always_unlocked=True)
    mr.add("audio/bg_menu_life_happy.ogg")
    mr.add("audio/bg_one_day_more.ogg")
    mr.add("audio/bg_tension.ogg", always_unlocked=True)
    mr.add("audio/bg_working_fast.ogg", always_unlocked=True)
    mr.add("audio/bg_world_paraise.ogg")
    mr.add("audio/bg_burguer.ogg", always_unlocked=True)
    mr.add("audio/bg_burguer_hard.ogg", always_unlocked=True)
    mr.add("audio/bg_disk.ogg", always_unlocked=True)
    #mr.add("audio/bg_terror_credist.ogg", always_unlocked=True)
    # mr.add("audio/bg_lup.ogg", always_unlocked=True)

# Step 3. Create the music room screen.
screen music_room():

    tag menu

    add black_d
    add "bg/bg_game_just.png" at Transform(alpha=0.5)

    frame:
        style "frame_2"
        align(0.5, 0.5)
        xysize(800, 600)
        
        text _(">Music Little Secrets<"):
            style "text_color_2"
            xalign 0.45
            yalign 0.1


        viewport:
                align (0.5, 0.5)  # Cambia la posición de la barra de desplazamiento        
                xysize(450, 300)  # Ajusta el ancho del viewport
                draggable True
                scrollbars "vertical"
                mousewheel True
                has vbox
                spacing 10

        # The buttons that play each track.
                #textbutton "End Love" action mr.Play("audio/bg_end_love.ogg") style "button_cookie_1"
                #textbutton "Life happy Remix" action mr.Play("audio/bg_life_happy_remix.ogg") style "button_cookie_1"
                textbutton "Life happy" action mr.Play("audio/bg_menu_life_happy.ogg") style "button_cookie_1"
                textbutton "One day more" action mr.Play("audio/bg_one_day_more.ogg") style "button_cookie_1"
                textbutton "Tension" action mr.Play("audio/bg_tension.ogg") style "button_cookie_1"
                textbutton "Working Fast" action mr.Play("audio/bg_working_fast.ogg") style "button_cookie_1"
                textbutton "World Paraise" action mr.Play("audio/bg_world_paraise.ogg") style "button_cookie_1"

                textbutton "Burguer Maniac" action mr.Play("audio/bg_burguer.ogg") style "button_cookie_1"
                textbutton "Burguer Gold" action mr.Play("audio/bg_burguer_hard.ogg") style "button_cookie_1"
                # textbutton "Loser well" action mr.Play("audio/bg_lup.ogg") style "button_cookie_1"
                textbutton "Disk" action mr.Play("audio/bg_disk.ogg") style "button_cookie_1"
                #textbutton "Terror Credist" action mr.Play("audio/bg_terror_credist.ogg") style "button_cookie_1"

                #null height 20
                
        
    frame:
        align(0.1, 0.5)
        padding(25, 25)
        vbox:    # Buttons that let us advance tracks.
            textbutton _(">") action mr.Next()
            textbutton _("<") action mr.Previous()

            null height 10
        # The button that lets the user exit the music room.
            textbutton _("Menu principal") action ShowMenu("main_menu")

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    #on "replaced" action Play("music", "audio/bg_one_day_more.ogg")