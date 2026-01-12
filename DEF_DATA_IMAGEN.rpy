


########################################################
# BG
define ts_p_gl = 0.01



image bg_map_scene_show = Composite((1920, 1080), (0, 0), "map_resource/map_view_day.png")

image bg_living_room_gl:
    "bg_living_room"
    block:
        "bg_living_room"
        ts_p_gl
        "bg/sala_screen_gl.png"
        ts_p_gl
        "bg_living_room"
        ts_p_gl
        "bg/sala_screen_gl.png"
        ts_p_gl
        "bg_living_room"
        ts_p_gl
        "bg/sala_screen_gl.png"
        ts_p_gl
        "bg_living_room"
        ts_p_gl
        "bg/sala_screen_gl.png"
        ts_p_gl
        "bg_living_room"
        ts_p_gl
        "bg_living_room"
        ts_p_gl
        "bg/sala_screen_gl.png"
        ts_p_gl
        "bg_living_room"
        2.5
        repeat


image noise_a:
    "noise1.jpg"
    0.001
    "noise2.jpg"
    0.001   
    "noise3.jpg"
    0.001  
    "noise4.jpg"
    0.001
    "noise5.jpg"
    0.001
    "noise6.jpg"
    0.001
    repeat  

image noise = "noise_a"

image bg_kitchen_gl = "bg/cocina_screen.png"
image bg_bath_gl = "bg/bath_screen.png"
image bg_room_gl = "bg/cuarto_screen.png"

image street_bar = "bg/street_bar.png"

image bg_living_room:
    "bg/sala_screen.png"

image bg_kitchen = "bg/cocina_screen.png"
image bg_bath = "bg/bath_screen.png"
image bg_room = "bg/cuarto_screen.png"
image bg_beach = "bg/bg_beach.png"

image bg_beach_gray = Transform("bg/bg_beach.png", matrixcolor=SaturationMatrix(0))

image bg_park:
    "bg/bg_park.png"
    
image bg_restaurant = "bg/bg_restaurant.png"
image bg_shop = "bg/bg_shop.png"
image bg_bath2 = "bg/bg_bath.png"

define def_living_room = "bg_living_room"
define def_kitchen = "bg_kitchen"
define def_bath = "bg_bath"
define def_room = "bg_room"

#default bg_select_house = "def_"

image door_perilla = "use_door.png"

image white = Solid("#fff")
image black = Solid("#000")
image dark = Solid("#000000a4")
image blue = Solid("#0066FF")
image red = Solid("#FF0000")

image blue_alpha = Solid("#0066FFa4")
image red_alpha = Solid("#FF0000a4")

define dark_add = "dark"
define grey_add = "#ffffff77"
define black_d = "black"
define bg_map_view = "images/map_resource/map_view_new.png"

image glitch_bg = "resource/glitch_background.png"

init python:
    def random_color():
        colors = [
            "#FF0000", "#001EFF", "#33F000", "#EA00FF",
            "#00FFD2", "#5A00FF", "#FF9C00", "#FFEA00", "#FFFFFF"
        ]
        return renpy.random.choice(colors)

# transform para cambiar colores suavemente
transform color_wipe_anim:
    xalign 0.5 yalign 0.5
    block:
        ease 4.0 matrixcolor TintMatrix(random_color())
        easein 4.0 matrixcolor TintMatrix(random_color())
        ease 4.0 matrixcolor TintMatrix(random_color())
        easein 4.0 matrixcolor TintMatrix(random_color())
        ease 4.0 matrixcolor TintMatrix(random_color())
        easein 4.0 matrixcolor TintMatrix(random_color())
        ease 4.0 matrixcolor TintMatrix(random_color())
        easein 4.0 matrixcolor TintMatrix(random_color())
        ease 4.0 matrixcolor TintMatrix(random_color())
        repeat

image pass_bg_color = "infinity_pass.png"
# define background_color_select = "pass_bg_color"




###############################################################


define vignette_press_main = "vignette_press"

image vignette_press:
    xysize(1920, 1080)
    "vignette.png" 

transform lock_vignette(x=950):
    on show:
        alpha 0.0
        linear 2 alpha 1.0
    block:
        easein 3.5 xcenter x zoom 1.4
        easein 3.5 xcenter x zoom 1.0
        easein 3.5 xcenter x zoom 1.4
        easein 3.5 xcenter x zoom 1.0
        repeat


#image punto_negro_full = Composite((1280, 720), (0, 0), "punto_negro", (0, 0), "punto_negro2", (0, 0), "punto_negro3", (0, 0), "punto_negro4")

#WhileSpeaking("aug", "speaking_august", "august_mouth_closed")


#############################################################

image image_config_map:
    "map_resource/map_view_day_[chr2_game.culture_chr].png"


image water_ = Solid("#078FFF")
image water_pixel = Transform("water_", size=(20, 32))

image p_white = Solid("#fff")
image p_black = Solid("#000")
image p_red = Solid("#BD0101")
image p_red_dark = Solid("#5D0101")
image p_pink = Solid("#FF00EA")
image p_aqua_light = Solid("#A9F4FD")
image p_green = Solid("#0BEB00")
image p_blue = Solid("#3745ff")

image particules_white = Transform("p_white", size=(32, 32))
image particules_black = Transform("p_black", size=(64, 64))
image particules_pink = Transform("p_pink", size=(3, 3))
image particules_white2 = Transform("p_white", size=(3, 3))
image particules_aqua_light = Transform("p_aqua_light", size=(28, 28))

image particules_blue = Transform("p_blue", size=(7, 7))

image particules_green = Transform("p_green", size=(32, 32))
image particules_red = Transform("p_red", size=(32, 32))
image particules_red_dark = Transform("p_red_dark", size=(64, 64))


image ilumination_effect = Transform("gui/ilumination.png", size=(12, 12))
image ilumination_effect_pink = Transform("images/resource/dade/3d_fake/particule_rose.webp", size=(8, 8))

image ilumination_effect_pink_great = Transform("images/resource/dade/3d_fake/particule_rose.webp", size=(32, 32))

image victory_game_mini = "resource/victory_screen.png"
image defeat_game_mini = "resource/defeat_screen.png"


image water_gout:
    "water_pixel"
    zoom 0.90 rotate -20
    block:
        easein .75 alpha 0.00

image water_gout2:
    "water_pixel"
    zoom 0.75 rotate -30
    block:
        easein 1 alpha 0.00

image water_gout_rect:
    "water_pixel"
    zoom 0.90 rotate 0
    block:
        easein .75 alpha 0.00


image image_water = SnowBlossom(
    "water_gout", 
    count=69, 
    border=15, 
    xspeed=(22, 220), 
    yspeed=(100, 1300), 
    start=4, 
    fast=True, 
    horizontal=False)

define map_rain_water = SnowBlossom(
    "water_gout2", 
    count=110, 
    border=20, 
    xspeed=(22, 600), 
    yspeed=(100, 1700), 
    start=0, 
    fast=True, 
    horizontal=False)


define map_rain_water_improvised = SnowBlossom(
    "water_gout_rect", 
    count=110, 
    border=20, 
    xspeed=(22, 55), 
    yspeed=(100, 1700), 
    start=0, 
    fast=True, 
    horizontal=False)

define map_rain_water_force = SnowBlossom(
    "water_gout2", 
    count=271, 
    border=20, 
    xspeed=(22, 600), 
    yspeed=(100, 2000), 
    start=5, 
    fast=True, 
    horizontal=False)





define image_blossomkey = SnowBlossom(
    "ilumination_effect_pink_great", 
    count=10, 
    border=50, 
    xspeed=(5, 34), 
    yspeed=(100, 225), 
    start=5, 
    fast=True, 
    horizontal=False)


define particule_pink_main_menu = SnowBlossom(
    "ilumination_effect_pink", 
    count=10, 
    border=5, 
    xspeed=(20, 30), 
    yspeed=(55, 108), 
    start=10, 
    fast=True, 
    horizontal=False)

define particule_white_main_menu = SnowBlossom(
    "ilumination_effect", 
    count=20, 
    border=5, 
    xspeed=(20, 30), 
    yspeed=(55, 67), 
    start=20, 
    fast=False, 
    horizontal=False)


#####################################################################





image maniac_characters_img:
    choice:
        "character/sprite_icon/azuli_logo.png"
    choice:
        "character/sprite_icon/milia_logo.png"
    choice:
        "character/sprite_icon/cristal_logo.png"
    choice:
        "character/sprite_icon/blody_logo.png"


define maniac_characters_ = "maniac_characters_img"


image particele_edition:
    "resource/particule.png"
    zoom 0.2 alpha 1.00
    block:
        linear renpy.random.randint(1, 7) alpha 0.00


image ilumination_1 = "gui/ilumination.png"


define logo_model = "logo_base"
define logo_model2 = "logo_model_alphak"


image logo_base = "gui/icon_hd.png"

image logo_base_glitch:
    "logo_base"
    subpixel True
    xoffset 1000 zoom 1.4 yalign 0.4 rotate 90 alpha 0.5 
    ease_back 1.2 xoffset 322 rotate 0
    block:
        rotate 80
        linear 80 rotate 0
        repeat

image logo_base_verify_day:
    "logo_base"
    subpixel True
    xoffset 2500 zoom 1.4 yalign 0.4 rotate 360 alpha 0.5 
    ease_back 1.5 xoffset 450 rotate 0
    block:
        rotate 360
        linear 30 rotate 0
        repeat

image logo_model_alphak:
    "gui/icon_hd.png"
    block:
        linear 5 alpha 0.00
        linear 5 alpha 1.00
        repeat
        



image logo_onda_work:
    subpixel True
    "resource/base_frame_onda.png"
    #yoffset -140
    #xoffset -150
    xoffset -115
    yoffset -20
    #xalign 0.0
    #yalign 0.10
    block:
        rotate 360
        linear 10 rotate 0
        repeat



image logo_onda_work2:
    subpixel True
    "resource/base_frame_onda2.png"
    #yoffset -140
    #xoffset -150
    xoffset -115
    yoffset -20
    #xalign 0.0
    #yalign 0.10
    block:
        rotate 360
        linear 50 rotate 0
        repeat


image logo_onda_work3:
    subpixel True
    "resource/base_frame_onda3.png"
    #yoffset -140
    #xoffset -150
    xoffset -115
    yoffset -20
    #xalign 0.0
    #yalign 0.10
    block:
        rotate 360
        ease_back 20 rotate 0
        repeat





define add_animation_work = "logo_onda_work"
define add_animation_work2 = "logo_onda_work2"
define add_animation_work3 = "logo_onda_work3"

image alpha_day:
    subpixel True
    "bg/alpha_day.png"
    block:
        xpan 0
        linear 120 xpan 360
        repeat
    
image alpha_afternoom:
    subpixel True
    "bg/alpha_afternoom.png"
    block:
        xpan 0
        linear 120 xpan 360
        repeat

image alpha_night:
    subpixel True
    "bg/alpha_night.png"
    block:
        xpan 0
        linear 120 xpan 360
        repeat


image alpha_night_red = "bg/alpha_night_red.png"


image day_im_bg = "alpha_day"
image day2_im_bg = "alpha_day"
image afternoom_im_bg = "alpha_afternoom"
image afternoom2_im_bg = "alpha_afternoom"
image night_im_bg = "alpha_night"
image night2_im_bg = "alpha_night"
image night3_im_bg = "alpha_night_red"


define day_bg = "alpha_day"
define day2_bg = "alpha_day"
define afternoom_bg = "alpha_afternoom"
define afternoom2_bg = "alpha_afternoom"
define night_bg = "alpha_night"
define night2_bg = "alpha_night"
define night3_bg = "alpha_night_red"


image vacio_image_character = At("character/sprite_icon/screen_milia.png", character_a_z)
image cristal_image_character = At("character/sprite_icon/screen_cristal.png", character_a_z)
image azuli_image_character = At("character/sprite_icon/screen_azuli.png", character_a_z)
image blody_image_character = At("character/sprite_icon/screen_blody.png", character_a_z)

define vacio_pose_character = "vacio_image_character"
define cristal_pose_character = "cristal_image_character"
define azuli_pose_character = "azuli_image_character"
define blody_pose_character = "blody_image_character"




image demonic_emoji = Transform("icon_list_category/working/intencidad_now_hover.png", size=(64, 64))

image coins = Transform("gui/emoji/coin_money.png", size=(32, 32))

image money_euro = Transform("gui/emoji/euro_money.png", size=(32, 32))
image dollar_euro = Transform("gui/emoji/dollar_money.png", size=(32, 32))
image yen_euro = Transform("gui/emoji/yen_money.png", size=(32, 32))



transform ctc_animation:
    subpixel True
    xalign 0.18
    yalign 0.83
    size(48, 48)
    block:
        rotate 0
        linear 5 rotate -360
        repeat 



define ctc_img = At("ctc_", ctc_animation)
image ctc_ = "gui/icon_hd.png"



image flag_usa_ = Transform("gui/flags/usa_.png", size=(64, 42))
image flag_jp_ = Transform("gui/flags/jp_.png", size=(64, 42))
image flag_ru_ = Transform("gui/flags/ru_.png", size=(64, 42))
image flag_spain_ = Transform("gui/flags/spain_.png", size=(64, 42))
image flag_ucra_ = Transform("gui/flags/ucra_.png", size=(64, 42))
image flag_fr_ = Transform("gui/flags/fr_.png", size=(64, 42))

image afs = Transform("gui/affection.png", size=(32, 32))
image afs_b = Transform("gui/affection_bad.png", size=(32, 32))

image lx = Transform("gui/lust.png", size=(32, 32))
image lx_b = Transform("gui/lust_bad.png", size=(32, 32))

define coins_img = "coins"




image demon_animation:
    "icon_list_category/working/intencidad_now_hover.png" with Dissolve(.8)
    1.0
    "icon_list_category/working/intencidad_now1_hover.png" with Dissolve(.8)
    1.0
    "icon_list_category/working/intencidad_now2_hover.png" with Dissolve(.8)
    1.0
    repeat

define demon_icon_animation = "demon_animation"


transform logo_rotate_mini1:
    subpixel True
    xoffset -700
    yalign 0.5
    alpha 0.8
    zoom 1.8
    parallel:
        rotate 360
        ease_back 1 rotate 0


transform logo_rotate_mini2:
    subpixel True
    xoffset -700
    yalign 0.5
    alpha 0.8
    zoom 1.8
    parallel:
        rotate 0
        ease_back 1 rotate 360


image logo_mini1 = At("gui/icon_ultra.png", logo_rotate_mini1)
image logo_mini2 = At("gui/icon_ultra.png", logo_rotate_mini2)

define logo_im_selector = "logo_selector"

image window_icon_logo = "gui/logo_game.png"


layeredimage logo_selector:

    if chr2_game.if_logo_choice == 1:
        "logo_mini1"
    elif chr2_game.if_logo_choice == 2:
        "logo_mini2"

##########################################################################
##########################################################################


#define flash = Fade(0.1, 0.0, 0.5, color="#fff")

image flash_im:
    "#fff"
    alpha 0.5
    linear .7 alpha 0.0
    repeat 3

#c_1_pose1


image hand_1a = "character/azuli/pet_azuli/hand_1.png"




##########################################################################
##########################################################################


#image reloj_screen_1 = "resource/reloj_1.png"
#image reloj_screen_2 = "resource/reloj_2.png"
#image reloj_screen_3 = "resource/reloj_3.png"
#image reloj_screen_4 = "resource/reloj_4.png"
#image reloj_screen_5 = "resource/reloj_5.png"

image hd_reloj_bar:
    subpixel True
    "resource/circule_reloj_bar.png"
    block:
        rotate 360
        linear 30 rotate 0
        repeat

image hd_reloj_bar_hard:
    subpixel True
    xoffset -140
    yoffset -140
    "resource/circule_reloj_bar_hard.png"
    block:
        rotate 360
        linear 35 rotate 0
        repeat


image hd_base_1:
    "resource/circule_reloj_base.png"
    rotate 150

image hd_base_2:
    "resource/circule_reloj_base.png"
    rotate 110

image hd_base_3:
    "resource/circule_reloj_base.png"
    rotate 80

image hd_base_4:
    "resource/circule_reloj_base.png"
    rotate 50

image hd_base_5:
    "resource/circule_reloj_base.png"
    rotate 10

image hd_base_6:
    "resource/circule_reloj_base.png"
    rotate -25

image hd_base_7:
    "resource/circule_reloj_base.png"
    rotate -120


image hd_base_1_hard:
    "resource/circule_reloj_base_hard.png"
    rotate 150

image hd_base_2_hard:
    "resource/circule_reloj_base_hard.png"
    rotate 110

image hd_base_3_hard:
    "resource/circule_reloj_base_hard.png"
    rotate 80

image hd_base_4_hard:
    "resource/circule_reloj_base_hard.png"
    rotate 50

image hd_base_5_hard:
    "resource/circule_reloj_base_hard.png"
    rotate 10

image hd_base_6_hard:
    "resource/circule_reloj_base_hard.png"
    rotate -25

image hd_base_7_hard:
    "resource/circule_reloj_base_hard.png"
    rotate -120


image hd_base_8_hard:
    subpixel True
    "resource/circule_reloj_base_hard.png"
    block:
        rotate 0
        linear 38 rotate 360
        repeat



image hd_base_8:
    subpixel True
    "resource/circule_reloj_base.png"
    block:
        rotate 0
        linear 38 rotate 360
        repeat


image time_screen_point1:
    xoffset 115
    yoffset 110
    "resource/circule_reloj_point1.png"

image time_screen_point2:
    xoffset 115
    yoffset 110
    "resource/circule_reloj_point2.png"

image time_screen_point3:
    xoffset 115
    yoffset 110
    "resource/circule_reloj_point3.png"

image time_screen_point4:
    xoffset 115
    yoffset 110
    "resource/circule_reloj_point4.png"


layeredimage hd_reloj_base:
    if time_p.fase_dia == "day":
        "hd_base_1"
    elif time_p.fase_dia == "day2":
        "hd_base_2"
    elif time_p.fase_dia == "afternoom":
        "hd_base_3"
    elif time_p.fase_dia == "afternoom2":
        "hd_base_4"
    elif time_p.fase_dia == "night":
        "hd_base_5"
    elif time_p.fase_dia == "night2":
        "hd_base_6"
    else:
        "hd_base_7"
    

layeredimage hd_reloj_point_general:
    if time_p.fase_dia == "day":
        "time_screen_point1"
    elif time_p.fase_dia == "day2":
        "time_screen_point1"
    elif time_p.fase_dia == "afternoom":
        "time_screen_point2"
    elif time_p.fase_dia == "afternoom2":
        "time_screen_point2"
    elif time_p.fase_dia == "night":
        "time_screen_point3"
    elif time_p.fase_dia == "night2":
        "time_screen_point3"
    else:
        "time_screen_point4"



layeredimage hd_reloj_base_hard:
    if time_p.fase_dia == "day":
        "hd_base_1_hard"
    elif time_p.fase_dia == "day2":
        "hd_base_2_hard"
    elif time_p.fase_dia == "afternoom":
        "hd_base_3_hard"
    elif time_p.fase_dia == "afternoom2":
        "hd_base_4_hard"
    elif time_p.fase_dia == "night":
        "hd_base_5_hard"
    elif time_p.fase_dia == "night2":
        "hd_base_6_hard"
    else:
        "hd_base_7_hard"





define timer_base_screen_chr = "timer_screen_chr"
define timer_base_screen_chr2 = "timer_screen_chr2"

image timer_screen_chr = Composite((512, 512), (0, 0), "hd_reloj_base",
    (0, 0), "hd_reloj_point_general",
    (0, 0), "hd_reloj_bar")


image timer_screen_chr2 = Composite((512, 512), (0, 0), "hd_base_8",
    (0, 0), "hd_reloj_point_general",
    (0, 0), "hd_reloj_bar")


image timer_screen_chr_hard = Composite((512, 512), (0, 0), "hd_reloj_base_hard",
    (0, 0), "hd_reloj_point_general",
    (0, 0), "hd_reloj_bar_hard")


image timer_screen_chr2_hard = Composite((512, 512), (0, 0), "hd_base_8_hard",
    (0, 0), "hd_reloj_point_general",
    (0, 0), "hd_reloj_bar_hard")



image reloj_timer_dinamic = ConditionSwitch(
        "persistent.optimization in ['low', 'medium'] and dificulty_mode_game == 'hard'",
            "timer_screen_chr_hard",

        "persistent.optimization in ['low', 'medium']",
            timer_base_screen_chr,

        "love_.quantity <= warning_love and dificulty_mode_game == 'hard'",
            "timer_screen_chr2_hard",

        "love_.quantity <= warning_love",
            timer_base_screen_chr2,
            
        "dificulty_mode_game == 'hard'",
            "timer_screen_chr_hard",
        "True",
            timer_base_screen_chr
    )


####################################################################


transform icon_bar_color:
    xoffset -20 yoffset 35
    zoom 0.35 alpha 0.7


define emoji_love_ = "gui/bar/bar_love/hearth.png"
define emoji_star_ = "gui/bar/bar_love/star.png"
define emoji_lust_ = "gui/bar/bar_love/lust.png"


# TEXTURE BAR DEF



image bar_base_empty = Composite((1480, 312), (0, 0), "gui/bar/bar_love/bar_base_hover.png")

image bar_base_full = Composite((1480, 312), (0, 0), "gui/bar/bar_love/bar_base_idle.png")


image bar_love_color = At("bar_base_full", select_color_matrix(c="#F63838"))

image bar_lust_color = At("bar_base_full", select_color_matrix(c="#bd0de4"))

image bar_affection_color = At("bar_base_full", select_color_matrix(c="#01FEEF"))

image bar_good_color = At("bar_base_full", select_color_matrix(c="#00ff04"))

image bar_bad_color = At("bar_base_full", select_color_matrix(c="#c20000"))

transform select_color_matrix(c="#fff"):
    matrixcolor TintMatrix(c) * SaturationMatrix(0.5)



image icon_love_bar = "gui/bar/bar_love/borde_hearth.png"

image icon_affection_bar = "gui/bar/bar_love/borde_affection.png"

image icon_lust_bar = "gui/bar/bar_love/borde_lust.png"









define image_gui_character = "move_pose_character"

image move_pose_character:
    subpixel True
    choice:
        "character_gray_azuli"
        choice:
            xpos 2300
            linear 35 xpos -2300
        choice:
            xpos -2300
            linear 35 xpos 2300
    choice:
        "character_gray_vacio"
        choice:
            xpos 2300
            linear 35 xpos -2300
        choice:
            xpos -2300
            linear 35 xpos 2300
    choice:
        "character_gray_cristal"
        choice:
            xpos 2300
            linear 35 xpos -2300
        choice:
            xpos -2300
            linear 35 xpos 2300
    choice:
        "character_gray_blody"
        choice:
            xpos 2300
            linear 35 xpos -2300
        choice:
            xpos -2300
            linear 35 xpos 2300
    pause 3
    repeat






################################################################

# Funciones de screen working



image character_add_burguer2:
    choice:
        "resource/select_level_work2a.png"
    choice:
        "resource/select_level_work3a.png"
    choice:
        "resource/select_level_work1a.png"



image character_add_random:
    choice:
        "resource/select_level_work2.png"
    choice:
        "resource/select_level_work3.png"
    choice:
        "resource/select_level_work4.png"
    choice:
        "resource/select_level_work5.png"


define character_maniac_add_work = "character_add_random"
define character_maniac_add_burguer2 = "character_add_burguer2"



####################################################################



screen glitch_blocks():
    add "noise" at glitch_alpha_static
    if not persistent.optimization in ("low", "medium"):
        add GlitchSlices(max_offset=32, num_blocks=10) at glitch_estatic
        add GlitchSlices(max_offset=32, num_blocks=8) at glitch_estatic
        add GlitchSlices(max_offset=32, num_blocks=8) at glitch_estatic



transform glitch_estatic_yp:
    ypan 0 alpha 0.40
    block:
        linear 0.5 xpan 360 ypan 90 zoom 1.05 alpha 0.55
        xpan 0 ypan 0 zoom 1.00 alpha 0.2
        repeat



transform glitch_alpha_static(opacity=0.2):
    alpha opacity
    choice:
        linear .8 alpha 0.02*0.4
        linear .8 alpha 0.4
    choice:
        linear .8 alpha 0.02*0.2
        linear .8 alpha 0.4
    pause 3.5
    repeat



transform glitch_estatic(opacity=0.1):
    alpha opacity xalign 0.5
    choice:
        linear 2 yoffset -1150 alpha 0.02*0.4
    choice:
        linear 1.4 yoffset 1150 alpha 0.02*0.4
    choice:
        linear 1 yoffset -1150 alpha 0.02*0.2
    choice:
        linear 1.2 yoffset 1150 alpha 0.02*0.4
    repeat      
        


image light_red = "resource/led_red.png"
image light_green = "resource/led_green.png"
image light_blue = "resource/led_aqua.png"
image light_pink = "resource/led_pink.png"

image light_color:
    choice:
        "light_red" with Dissolve(.75)
    choice:
        "light_green" with Dissolve(.75)
    choice:
        "light_blue" with Dissolve(.75)
    choice:
        "light_pink" with Dissolve(.75)
    1.5    
    repeat

image light_matrix_1 = "light_color"
image light_matrix_2 = "light_color"
image light_matrix_3 = "light_color"
image light_matrix_4 = "light_color"

image particule_disk = SnowBlossom(
    "particules_pink", 
    count=100, 
    border=5, 
    xspeed=(20, 30), 
    yspeed=(55, 203), 
    start=100, 
    fast=True, 
    horizontal=False)

image particule_disk2 = SnowBlossom(
    "particules_white2", 
    count=100, 
    border=5, 
    xspeed=(20, 30), 
    yspeed=(55, 203), 
    start=100, 
    fast=True, 
    horizontal=False)

image bg_effect_light:
    alpha 0.2
    choice:
        "dark" with Dissolve(.75)
    choice:
        "white" with Dissolve(.75)
    0.8
    repeat



transform light_move_animation_left(xs=-1.0, al=1.00, v=2):
    xalign xs yoffset -150 alpha al
    block:
        parallel:
            ease v xoffset 650
            ease v xoffset 0
        parallel:
            ease v rotate -25
            ease v rotate 0
        repeat



transform light_move_animation_right(xs=2.0, al=1.00, v=2):
    xalign xs yoffset -150 alpha al
    block:
        parallel:
            ease v xoffset -650
            ease v xoffset 0
        parallel:
            ease v rotate 25
            ease v rotate 0
        repeat    
















###############################################################

image SpiralInfinity:
    ChaoticSpiral("particules_pink", count=38, max_radius=400, max_size=64, spin_speed=2.0)
    xalign 0.5
    yalign 0.5
    zoom 1.5

image SpiralInfinity2:
    ChaoticSpiral("particules_pink", count=22, max_radius=400, max_size=64, spin_speed=2.0)
    xalign 0.5
    yalign 0.5
    zoom 1.3


image SpiralInfinity3:
    ChaoticSpiral("particules_pink", count=19, max_radius=400, max_size=64, spin_speed=2.0)
    xalign 0.5
    yalign 0.5
    zoom 1.0

###################################################

image SpiralInfinity4:
    ChaoticSpiral("particules_white2", count=28, max_radius=550, max_size=64, spin_speed=0.02)
    xalign 0.5
    yalign 0.5
    zoom 1.8

image SpiralInfinity5:
    ChaoticSpiral("particules_blue", count=18, max_radius=350, max_size=84, spin_speed=0.02)
    xalign 0.5
    yalign 0.5
    zoom 1.4

define screen_SpiralInfinity = "SpiralInfinity4"
define screen_SpiralInfinity2 = "SpiralInfinity5"

############################################################

image animation_gravity_blood:
    ParticuleGravity("particules_red_dark", count=48, max_radius=440, duration=1.0, gravity=910.0, max_size=100)
    xalign 0.5
    yalign 0.5
    zoom 0.65


image animation_gravity_blood_hit:
    ParticuleGravity("particules_red_dark", count=21, max_radius=850, duration=1.0, gravity=910.0, max_size=300)
    xalign 0.5
    yalign 0.5
    zoom 1.35




image animation_cluster:
    AnimationCube("particules_black", count=15, max_size=75, speed=2.4, frequency=6.0, amount=0.4, cycle_duration=2.3)
    xalign 0.2
    yalign 0.5
    zoom 1.0

image animation_cluster2:
    MultiPulseAnimation("particules_black", count=10, max_size=180, cycle_duration=2.5, frequency=2.0, amount=0.2)
    xalign 0.7
    yalign 0.5
    zoom 1.0

image cube_explode_once:
    ExplosionParticles("particules_black", count=60, max_radius=1400, duration=1.5, max_size=80)
    xalign 0.5
    yalign 0.5
    zoom 1.4
    block:
        pause 0.5
        linear .7 alpha 0.00


image blood_explode:
    ParticuleGravity("particules_red", count=67, max_radius=800, duration=1.0, gravity=910.0, max_size=100)
    xalign 0.5
    yalign 0.5
    zoom 0.95
    block:
        pause 0.4
        linear .7 alpha 0.00

image animation_blood:
    ExplosionParticles("particules_red_dark", count=48, max_radius=300, duration=1.0, max_size=100)
    xalign 0.5
    yalign 0.5
    zoom 0.65

#define image_test = "animation_cluster"



define image_dade_list = [
    "images/resource/dade/3d_fake/dade1.png",
    "images/resource/dade/3d_fake/dade2.png",
    "images/resource/dade/3d_fake/dade3.png",
    "images/resource/dade/3d_fake/dade4.png",
    "images/resource/dade/3d_fake/dade5.png",
    "images/resource/dade/3d_fake/dade6.png"
    ]

image cube_fake = Cube3Dfake(image_dade_list)

image solid_pink_s:
    "images/resource/dade/3d_fake/particule_rose.webp"
    choice:
        zoom 0.8
    choice:
        zoom 1.0
    choice:
        zoom 0.9

        

image particules_aura_fake = AuraParticles("solid_pink_s", count=32, radius=200, speed=32, max_size=80)

image particules_aura_fake_gui = AuraParticles("solid_pink_s", count=40, radius=260, speed=55, max_size=120)


image dade_dinamic_effect = Composite(
    (256, 256), 
    (0, 0), "particules_aura_fake", 
    (0, 0), Transform("cube_fake", xoffset=-150, yoffset=-150)
    )


