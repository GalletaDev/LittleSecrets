

# init python:
#     def get_expressions(tag):
#         result = []

#         for name in renpy.display.image.images.keys():
#             if name and name[0] == tag:
#                 result.append(" ".join(name[1:]))

#         return result


screen expression_viewer():

    zorder 199

    $ CHARACTER_EXPRESSIONS = {
        "azuli_": [
            "normal",
            "happy",
            "sad",
            "angry",
            "perfect",
            "perfect2",
            "hot_1",
            "shape",
            "love",
            "hot",
            "chat",
            "loss",
            "chat2_not",
            "chat2",
            "more_sad1",
            "more_sad2",
            "more_sad3",
            "happy_sad",
            "sad_oh",
            "death",
            "death_not_sound",
            "rubor",
            "glitch_master",
            "death2",
            "ah",
            "dissa",
            "imp",
            "confusion",
            "confusion2",
            "lol",
            "lol2",
            "lol3",
            "lol4",
            "lol5",
            "lol6",
            "lol7",
            "lol8",   
            "tempori_dissa",
            "tempori_dissa2",
            "tempori_dissa3",
            "death_gl"
        ],
        "milia_":[
            "normal",
            "chat",
            "dissa",
            "happy",
            "sad",
            "loss",
            "death"
        ]
    }



    default char_tag = "azuli_"
    default selected_expr = "normal"

    $ expressions = CHARACTER_EXPRESSIONS.get(char_tag, [])

    add "#140f0f2a"
    modal True

    frame:
        align(.5, .5)
        padding(100, 80)

        viewport:
            ##############################################
            ##############################################
            align(0.9, 0.3)
            xysize(500, 720)
            draggable True
            scrollbars "vertical"
            mousewheel True

            vbox:
                spacing 10
                for expr in expressions:
                    textbutton expr:
                        action SetLocalVariable("selected_expr", expr)
                        

        add char_tag + " " + selected_expr at Transform(xalign=0.1, yalign=0.5, zoom=0.65, xysize=(1480, 1890))


    frame:
        xalign 0.1
        yalign 0.1
        padding(25, 25)
        hbox:
            spacing 5
            textbutton "Azuli":
                action [
                    SetLocalVariable("selected_expr", "normal"),
                    SetLocalVariable("char_tag", "azuli_"),
                    Function(renpy.restart_interaction)
                    ]

            textbutton "Milia":
                action [
                    SetLocalVariable("selected_expr", "happy"),
                    SetLocalVariable("char_tag", "milia_"),
                    Function(renpy.restart_interaction)
                    ]
            



    imagebutton:
        auto "gui/button_config_screen/button_cancel_%s.png"
        at Transform(xalign=0.9, yalign=0.1, zoom=0.7)
        activate_sound "audio/sfx/user_ui_effect.ogg"
        action Hide("expression_viewer")

