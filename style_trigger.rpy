

#########################################################################
#########################################################################
############## ESTILOS DE Botones



style button_cookie_1 is default:
    hover_background Frame("gui/button/button_hover.png")
    idle_background Frame("gui/button/button_idle.png")
    #xsize 180
    padding button_cookie_1_s.padding


style button_cookie_2 is default:
    hover_background Frame("gui/button/button_hover.png")
    idle_background Frame("gui/button/button_idle.png")
    #xsize 180
    padding button_cookie_1_s.padding

style grid_inventory is default:
    background Frame("gui/frame5.png", 20, 20)  # imagen de fondo

define button_cookie_1_s = Borders(50, 5, 50, 5)


define b_main_menu_borders = Borders(135, 15, 135, 15)
define button_main_1 = Borders(50, 5, 50, 5)

style b_main_menu is default:
    hover_background Frame("gui/button/button_hover_menu.png")
    idle_background Frame("gui/button/button_idle_menu.png")
    xsize 450
    padding b_main_menu_borders.padding



#########################################################################
#########################################################################
############## ESTILOS DE TEXT





style text_color_1:
    font "font/Lato-BoldItalic.ttf"  # Reemplaza con la ruta de tu fuente
    size 20
    color "#ffffff"
    outlines [(2, "#030303a1", 0, 0)]  # Outline de 2px de color negro
    bold True

style text_color_2:
    font "font/Lato-BoldItalic.ttf"
    size 35
    color "#994393"
    outlines [(2, "#000000", 0, 0)]
    bold True


style text_color_3:
    font "font/Lato-BoldItalic.ttf"
    size 23
    color "#ffffff"
    outlines [(2, "#000", 0, 0)]
    bold True

style frame_color_3 is text_color_3:
    background Frame("gui/button/choice_idle_background.png", button_cookie_1_s, tile=False)



style text_Screen_time_hr_1:
    font "font/Lato-BoldItalic.ttf"
    size 28
    color "#ffffff"
    outlines [(2, "#000", 0, 0)]
    bold True


style text_color_4:
    font "font/Lato-BoldItalic.ttf"
    size 28
    color "#994393"
    outlines [(2, "#ffffff", 0, 0)]
    bold True


style text_color_5:
    font "font/Lato-BoldItalic.ttf"
    size 35
    color "#fff"
    outlines [(2, "#000000", 0, 0)]
    bold True

style text_color_6:
    font "font/Lato-BoldItalic.ttf" 
    size 20
    color "#F0F0F0"
    bold True


style text_color_7:
    font "font/Lato-BoldItalic.ttf" 
    size 24
    color "#ffffff"
    outlines [(2, "#201F1Fa1", 0, 0)] 
    bold True

style text_color_8:
    font "font/spyci-regular.ttf" 
    size 36
    color "#B3298A"
    outlines [(2, "#fff", 2, 0)] 
    #bold True

style text_color_wiki_1:
    font "font/Lato-Bold.ttf" 
    size 28
    color "#fff"
    outlines [(1, "#000", 0, 0)] 


style text_color_category_view:
    font "font/Lato-BoldItalic.ttf" 
    size 30
    color "#fff"
    outlines [(1, "#000", 0, 0)]
    xfill True
    bold True


style text_color_dade_game:
    font "font/Lato-Black.ttf" 
    size 32
    color "#fff"
    outlines [(4, "#000000", 1, 1)]

style title_color_dade_game:
    font "font/moongalat.ttf" 
    size 28
    color "#fff"
    outlines [(4, "#120010", 1, 1)]


#########################################################################
#########################################################################
############## ESTILOS DE BARRAS


style text_bar_screen_love:
    font "font/Lato-BlackItalic.ttf"
    color "#F54C4C"
    xalign 0.3
    size 25

style text_bar_screen_affection:
    font "font/Lato-BlackItalic.ttf"
    color "#09ECF8"
    xalign 0.3
    size 25

style text_bar_screen_lust:
    font "font/Lato-BlackItalic.ttf"
    color "#ECA2FC"
    xalign 0.3
    size 25





style bar_love_:
    size 15
    right_bar Frame("bar_base_empty")
    left_bar Frame("bar_love_color")

style bar_affection_:
    size 15
    right_bar Frame("bar_base_empty")
    left_bar Frame("bar_affection_color")


style bar_lust_:
    size 15
    right_bar Frame("bar_base_empty")
    left_bar Frame("bar_lust_color")


style bar_good_:
    size 15
    right_bar Frame("bar_base_empty")
    left_bar Frame("bar_good_color")

style bar_bad_:
    size 15
    right_bar Frame("bar_base_empty")
    left_bar Frame("bar_bad_color")



#########################################################################
#########################################################################

#    ESTILOS DE FONDO
#########################################################################

style background_style_not_logo:
    padding gui.frame_borders.padding
    background Frame("gui/background_menu/back_2_rose_not_logo.png", gui.frame_borders, tile=gui.frame_tile)







#########################################################################
#########################################################################

#    ESTILOS DE FRAMES
#########################################################################

image background_general = "gui/background_menu/back_2_rose_not_logo.png"
image background_black = "gui/background_menu/back_5_black_not_logo.png"
image background_none = "gui/background_menu/back_3_grey_not_logo.png"

style frame_2:
    padding gui.frame_borders.padding
    background Frame("background_general", gui.frame_borders, tile=gui.frame_tile)

style frame_3:
    padding gui.frame_borders.padding
    background Frame("background_general", gui.frame_borders, tile=gui.frame_tile)

style frame_3a:
    padding gui.frame_borders.padding
    background Frame("background_general", gui.frame_borders, tile=gui.frame_tile)

style frame_4:
    padding gui.frame_borders.padding
    background Frame("background_general", gui.frame_borders, tile=gui.frame_tile)

style frame_5:
    padding gui.frame_borders.padding
    background Frame("background_black", gui.frame_borders, tile=gui.frame_tile)

style frame_6:
    padding gui.frame_borders.padding
    background Frame("background_general", gui.frame_borders, tile=gui.frame_tile)

style frame_7:
    padding gui.frame_borders.padding
    background Frame("background_general", gui.frame_borders, tile=gui.frame_tile)

style frame_8:
    padding gui.frame_borders.padding
    background None


style frame_name_select:
    background Frame("background_general", frame_name_chr)
    xsize 350
    ysize 120

style frame_10:
    padding gui.frame_borders2.padding
    xsize 800
    background Frame("background_general", gui.frame_borders, tile=gui.frame_tile)


style frame_black_opacity:
    padding gui.frame_borders.padding
    background Frame("gui/background_menu/back_6_azuli.png", gui.frame_borders, tile=gui.frame_tile)


style frame_neutral:
    padding gui.frame_borders.padding
    background Frame("background_none", gui.frame_borders, tile=gui.frame_tile)


#########################################################################
#########################################################################
# Estilos mas detallados

# Viendo el ejemplo que hizo chatgpt me di cuenta que utiliza especificaciones
# 1- no usar {colo=#000}{/color} o otra etiqueta de texto nunca, (!por que esto rompe los style¡)
# funciona en raiz existe style(el padre) y style_prefix(el hijo)
# con ese orden y especificacion exacta logras tener styler bien hecho
# 2- dependiendo de las especificaciones colocales las correctas para no confundirte
# 3- existen, frame, text, label y ect...

# EJEMPLO:
    # frame:
    #     style "frame_gui_text_rose"
    #     style_prefix "frame_gui_text_rose"   # 👈 sin "_text"
    #     align (0.5, 0.5)

    #     vbox:
    #         align (0.5, 0.1)
    #         spacing 10


# Estilos (mejor si están definidos antes de la screen)
style frame_gui_text_rose is frame:
    xsize 1080
    ysize 760
    background Frame("gui/frame7.png")

style frame_gui_text_rose_text is text:
    font "font/lick_big.ttf"
    bold False
    size 29
    color "#fff"
    outlines [(2, "#64008D", 1, 0)]

# Para el label (título)
style frame_gui_text_rose_label is label
style frame_gui_text_rose_label_text is text:
    font "font/Lato-BoldItalic.ttf"
    bold True
    size 32
    color "#FFD700"
    outlines [(4, "#000", 0, 0)]  # opcional


#########################################################################
#########################################################################


#########################################################################
#########################################################################
# Estilos mas hambueguer minigame



style frame_11_burguer:
    padding gui.frame_borders.padding
    background Frame("resource/base_bg_burguer/note.png", gui.frame_borders_burguer, tile=gui.frame_tile)

style frame_12_burguer:
    padding gui.frame_borders.padding
    background Frame("resource/base_bg_burguer/time_style.png", gui.frame_borders, tile=gui.frame_tile)

style frame_13_burguer:
    padding gui.frame_borders.padding
    background Frame("resource/base_bg_burguer/mess_b.png", gui.frame_borders, tile=gui.frame_tile)


#########################################################################
#########################################################################


image logo_frame_animation:
    subpixel True
    "gui/window_icon.png"
    block:
        rotate 360
        linear 20 rotate 0
        repeat

style frame_9:
    padding gui.frame_borders.padding
    background Frame("logo_frame_animation", gui.frame_borders, tile=gui.frame_tile)


style padded_button is text_color_2:
    xpadding 40
    ypadding 10
style margin_button is padded_button:
    ymargin 10
style sized_button is margin_button:
    size_group "text_color"
style xfill_button is margin_button:
    xfill True
 
 

style custom_vertical_bar:
    top_bar "gui/bar/top.png"
    bottom_bar "gui/bar/bottom.png"
    ymaximum 300
    xmaximum 30





 
