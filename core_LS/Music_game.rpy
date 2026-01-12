


############################################################
init python:
    renpy.music.register_channel("music_sfx", "music_sfx", loop=True, stop_on_mute=False)
    renpy.music.register_channel("voice_sfx", "voice_sfx", loop=False, stop_on_mute=False)

    # renpy.music.set_volume(volume=0.6, delay=0, channel='music_sfx')
    # renpy.music.set_volume(volume=0.6, delay=0, channel='voice_sfx')

default music_files = JSON_("data_library_json/SELECT_MUSIC_LIST.json")
default last_music_played = None  # <- guarda la última canción
default name_music_m = "silent"


# CANALES DE MUSICA
init python:

    def flag_freeze_music(active=True):
        """
        Si es verdadero apagara bg_music por completo,
        si es Falso, encenderá bg_music.
        """
        global name_music_m, freeze_music_bg
        if active:
            name_music_m = "silent"
            select_audio_b("audio/silent.ogg")
            freeze_music_bg = True
        else:
            freeze_music_bg = False           



    def select_audio_b(music: str = "audio/silent.ogg") -> str:
        """
        Verificador de música con music_sfx separado de la función normal de Ren'Py.
        Funciona mediante un screen persistente, actualizando su valor cada vez.

        Args:
            music (str): Ruta del archivo de música. Por defecto "audio/silent.ogg".

        Returns:
            str: La música seleccionada.
        """
        global music_files, last_music_played, name_music_m

        music = name_music_m

        if music == last_music_played:
            return


        current_file = renpy.music.get_playing(channel="music_sfx")

        if current_file != music:
            try:
                next_file = music_files[music]
            except KeyError as e:
                next_file = music_files["silent"]
    
            if current_file != next_file:
                renpy.music.play(next_file, channel="music_sfx", loop=True, fadeout=0.2)
                if name_music_m == "silent":
                    pass
                else:
                    show_notification_music(music_name=music)

            last_music_played = music  # actualiza

    def show_notification_music(music_name):
        renpy.show_screen("music_notification")

    def play_music_sfx(filename="audio/silent.ogg"):
        renpy.music.play(filename, channel="music_sfx", loop=True, fadeout=1.0) #(name_music = "one_day_more" #name_music = "")

    def stop_music_sfx():
        renpy.music.stop(channel="music_sfx", fadeout=0.2)


image disk_compaq = Transform("gui/disk.png", size=(64, 64))

image disk_grade:
    "disk_compaq"
    block:
        subpixel True
        rotate 0
        linear 2 rotate 360
        repeat 6

style music_notify_style:
    color "#FFFFFF" 
    size 30 
    outlines [(2, "#000", 0, 0)] 

screen music_notification():

    zorder 1000

    hbox:
        align(.5, .0)
        at music_notify_anim
        spacing 4
        frame:
            xalign 0.5
            yalign 0.9
            xysize(350, 100)
            style "frame_8"
            add "#000000e6" at Transform(size=(350, 100))
            hbox:
                add "disk_grade"
                text "[name_music_m]" style "music_notify_style"
    
    timer 3.5 action Hide("music_notification", transition=Dissolve(.5))


transform music_notify_anim:
    alpha 0.0
    yoffset -40
    easein 0.3 alpha 1.0 yoffset 0
    pause 2.8
    easeout 0.3 alpha 0.0 yoffset -40




define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define music_sfx = True
define voice_sfx = True

default preferences.volume.music_sfx = 0.85
default preferences.volume.voice_sfx = 0.85

default preferences.volume.music = 0.7
default preferences.volume.sfx = 0.7
default preferences.volume.main  = 1.0


init python:

    def play_dual_channel(snd1, snd2, ch1="sound", ch2="voice_sfx"):
        renpy.music.play(snd1, channel=ch1, loop=False, if_changed=True)
        renpy.music.play(snd2, channel=ch2, loop=False, if_changed=True)        


    def stop_dual_channel():
        renpy.music.stop(channel="sound")
        renpy.music.stop(channel="voice_sfx")

    #last_vol = -1.0