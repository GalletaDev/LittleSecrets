
init python:
    def bug_option_reload():
        """
        Automatiza menu_option para que se encargue de algún bug suelto
        """
        global name_music_m, BOT_CHR
        if name_music_m == "silent":
            # bug reload ._.?
            name_music_m = music_reload_bug.get(time_p.fase_dia, "one_day_more")
        if BOT_CHR == False:
            # bug bot ._.?
            ACTIVE_BOT(active=True)
