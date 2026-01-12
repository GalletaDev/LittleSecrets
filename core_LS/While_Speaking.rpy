init python:

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
    speaking_ctc = False

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking, love_, warning_love, chr2_game, speaking_ctc

        # voice_girl_available = ["azuli_", "milia_", "cristal_", "blody_"]
        voice_ect_available = ["al", "npc", "mi", "w"]
        voice_file = "audio/sfx_v/v_d_.ogg"  # sonido por defecto

        if love_.quantity <= warning_love:
            voice_file = "audio/sfx_min/pop_2.ogg"
        else:
            if name == "mc":
                voice_file = "audio/sfx_v/v_mc_.ogg"
            elif name in voice_ect_available:
                voice_file = "audio/sfx_v/v_d_.ogg"
            elif chr2_game and hasattr(chr2_game, "s_chr"):
                char = str(chr2_game.s_chr)
                voice_file = f"audio/sfx_v/v_{char}.ogg"


        if not renpy.music.is_playing(channel="voice_sfx"):
            renpy.music.play(voice_file, channel="voice_sfx", loop=True)


        if event == "show":
            speaking = name
            speaking_ctc = True
        elif event in ["slow_done", "end"]:
            speaking = None
            speaking_ctc = False
            renpy.music.stop(channel="voice_sfx")

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

