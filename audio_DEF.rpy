






define bg_theme_we = "audio/bg_my_blue_slow.ogg"
define bg_shop_day = "audio/bg_shop_day.ogg"
define bg_my_blue_slow = "audio/bg_my_blue_slow.ogg"

define bg_day_more = "audio/ONE_DAY_MORE.ogg"
define bg_afternoom_more = "audio/ONE_AFTERNOOM_MORE.ogg"
define bg_night_more = "audio/ONE_NIGHT_MORE.ogg"

define money_sound = "audio/sfx/money_sound.ogg"
define s_warning = "audio/sfx/alerta.ogg"
define fail_sfx = "audio/sfx/fail.ogg"
define win_sfx = "audio/sfx/affection_sound.ogg"

define kick_sound = "audio/sfx/kick.ogg"


define radio_sound = "audio/sfx/radio.ogg"

define user_ui_negative = "audio/sfx/user_ui_negative.ogg"
define user_ui_activate = "audio/sfx/user_ui_effect.ogg"
define ui_mouse_click = "audio/sfx/ui_click.ogg"

define drop_coin = "game_dade_bros/sound/drop_coin.mp3"
define sfx_pop = "audio/sfx/pop.ogg"
define glitch_voz = "audio/sfx/glitch_voice.ogg"
define sound_walk = renpy.random.choice(["audio/sfx/walk.ogg", "audio/sfx/walk2.ogg"])

define alert_tension = "audio/sfx_d/sound_dificult_5.ogg"

init python:
    
    #sound_ge = None

    def audio_full_kiss():
        global chr2_game
        try:
            sound_ge = renpy.random.choice(["audio/sfx_sx/"+ str(chr2_game.s_chr) + "/kiss" + str(renpy.random.randint(1, 5)) + ".ogg"])
        except ValueError:
            raise ValueError("!Music list not exist or more of 6, -1¡")
        renpy.music.play(sound_ge, channel="voice_sfx", loop=False, synchro_start=True)


init python:
    def sound_glitch(trans, st, at):
        if renpy.random.random() < 0.2:  # 40% chance to play a sound
            sound_random = renpy.random.choice([
                "audio/sfx/glitch.ogg",
                "audio/sfx/glitch2.ogg"
            ])
            renpy.music.play(sound_random, channel="sound")
        return None

    def sound_kick(trans, st, at):
        renpy.music.play("audio/sfx/kick.ogg", channel="sound")        
        return None