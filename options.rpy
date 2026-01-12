## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

# define config.name = _("Little Secrets Alpha [config.version]")

define name_dev_game = _("GalletaDev: ")

define config.debug_prediction = True
## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

default preferences.gl_framerate = 60
default preferences.gl_powersave = False
define gui.show_name = True

define custom_framerate = 60
default persistent.optimization = "medium"




define config.window_auto_hide = ["scene", "call screen", "menu", "say-centered", "say-bubble", "menu_option"]

init python:

    def update_framerate():
        preferences.gl_framerate = custom_framerate
        renpy.save_persistent()  # Guarda preferencias para que persista entre sesiones

    def optimization_option(status):
        if status == "low":
            persistent.optimization = "low"
        elif status == "medium":
            persistent.optimization = "medium"
        elif status == "high":
            persistent.optimization = "high"
        renpy.save_persistent()


default _save_enable = True
default _load_enable = True
default _skip_enable = True

#define config.after_load_callbacks.append(lambda: rpc_discord.init_rpc())

default persistent.skip_option_off = False
default persistent.choice_option_off = False

define config.transparent_tile = False

define config.pause_with_transition = True

define config.screenshot_pattern = "screenshot%04d.jpg"
## The version of the game.

define config.version = "0.0.0"

init python:

    fix_version = ["1.3.0", "1.3.1", "1.3.2"]

    def version_game_LS():
        return fix_version[-1]

    # Aplicar la versión
    config.version = version_game_LS()

    def game_name():
        return "Little Secrets Alpha {}".format(config.version)

    config.name = game_name()




#define config.gl2 = False # Usa el renderizado basado en OpenGL 1
define config.gl2 = True  # Usa el renderizado basado en OpenGL 2

######################################################################
# Activar despues de distribuir
init python:
    config.keymap['rollback'] = []

    # def no_rollback_event(ev, handled):
    #     if ev.type == renpy.display.core.KEYDOWN:
    #         if ev.key in ['K_PAGEUP', 'K_AC_BACK', 'K_KP_4']:
    #             return True
    #     return False


    # config.overlay_functions.append(lambda: renpy.display.interface.register_event_filter(no_rollback_event))

# define config.mousewheel_rollback = False
define config.rollback_enabled = False

######################################################################
## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


define config.conditionswitch_predict_all = True

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "LittleSecrets"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = renpy.random.choice(["audio/ELECTION.ogg"])

#define config.predict_statements = True  # Activa la predicción de declaraciones
#define config.predict_screen = True      # Activa la predicción de pantallas
#define config.predict_images = True      # Activa la predicción de imágenes
#define config.predict_audio = False      # Activa la predicción de audio




#define config.mouse = { }
#define config.mouse['default'] = [ ( "gui/arrow.png", 0, 0) ]
#define config.mouse['pressed_default'] = [ ( "gui/arrow_pressed.png", 0, 0) ]
#define config.mouse['button'] = [ ( "gui/arrow_button.png", 0, 0) ]
#define config.mouse['pressed_button'] = [ ( "gui/arrow_button_pressed.png", 0, 0) ]
#define config.mouse['menu'] = [ ( "gui/arrow_menu.png", 0, 0) ]


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = None
define config.exit_transition = None

define build.change_icon_i686 = True
## Between screens of the game menu.

define config.intra_transition = Dissolve(.2)
default persistent.language_box = "spanish"

## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = None
define config.window_hide_transition = None


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 75


# Ejemplo de uso

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 30
#default preferences.gl_framerate = 120

## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "LittleSecrets-1.2.9-official"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.



# init -99 python:
#     import os

#     def move_character_archives():
#         base_path = config.gamedir
#         rpa_files = [f for f in os.listdir(base_path) if f.endswith("_chr.rpa")]

#         for rpa in rpa_files:
#             name = os.path.splitext(rpa)[0]
#             dest_folder = os.path.join(base_path, "chr", name)
#             os.makedirs(dest_folder, exist_ok=True)

#             old_path = os.path.join(base_path, rpa)
#             new_path = os.path.join(dest_folder, rpa)

#             os.replace(old_path, new_path)
#             config.archives.append(os.path.join("chr", name, name))

#     # Solo mover después del build, no en modo desarrollador
#     if not config.developer:
#         move_character_archives()








init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    # build.classify_renpy = False
    # build.include_old_themes = False
    build.archive("TRADUCTION", "all")

    build.archive("azuli_chr", "all")
    build.archive("milia_chr", "all")
    build.archive("cristal_chr", "all")
    build.archive("blody_chr", "all")

    build.archive("BASE_DATA_", "all")
    build.archive("SCRIPTS", "all")
    build.archive("RESOURCE", "all")
    build.archive("AUDIO_SFX", "all")
    build.archive("FONTS", "all")



    build.classify('logs/**.txt', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("**.psd", None)
    build.classify("**.kra", None)
    build.classify("**.rpy", None)
    build.classify("**/desktop.ini", None)
    build.classify("**.pdf", None)
    build.classify('**.md', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/audio/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('/game/.vscode/**', None)

    ## To archive files, classify them as 'archive'.
    build.classify('game/tl/**', 'TRADUCTION')

    build.classify('game/images/character/azuli/**.png', 'azuli_chr')
    build.classify('game/game_character/azuli_/**.rpyc', 'azuli_chr')

    build.classify('game/images/character/milia/**.png', 'milia_chr')
    build.classify('game/game_character/milia_/**.rpyc', 'milia_chr')

    build.classify('game/images/character/cristal/**.png', 'cristal_chr')
    build.classify('game/game_character/cristal_/**.rpyc', 'cristal_chr')

    build.classify('game/images/character/blody/**.png', 'blody_chr')
    build.classify('game/game_character/blody_/**.rpyc', 'blody_chr')


    build.classify('game/**.png', 'RESOURCE')
    build.classify('game/**.jpg', 'RESOURCE')
    build.classify('game/**.webp', 'RESOURCE')
    build.classify('game/**.jpeg', 'RESOURCE')


    build.classify('game/**.ogg', 'AUDIO_SFX')
    build.classify('game/**.mp3', 'AUDIO_SFX')
    build.classify('game/**.wav', 'AUDIO_SFX')


    build.classify('game/**.json', 'BASE_DATA_')

    build.classify('game/**.rpyc', 'SCRIPTS')
    build.classify('game/**.ls', 'SCRIPTS')
    build.classify('game/**.py', 'SCRIPTS')
    build.classify('game/**.txt', 'SCRIPTS')
    build.classify("README.txt", "all")
    build.classify("HELP_README.html", "all")

    build.classify('game/**.ttf', 'FONTS')
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')




    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"


#translate japanese python:
    #gui.system_font = "fonts/japanese.ttf"
    #gui.name_text_font = "fonts/japanese.ttf"
    #gui.text_font = "fonts/japanese.ttf"
    #gui.interface_text_font = "fonts/japanese.ttf"
    #gui.button_text_font = "fonts/japanese.ttf"
    #gui.choice_button_text_font = "fonts/japanese.ttf"