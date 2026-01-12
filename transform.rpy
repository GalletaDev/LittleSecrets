

init python:
    def reset_alpha(trans, st, at):
        trans.alpha = 1.0
        return None

    def reset_zoom(trans, st, at):
        trans.zoom = 0.64
        return None


# Function to play a glitch sound randomly (40% chance)



##############################################
########################################################
#### POSITION CHARACTER SHOW #####################

default f_s = False

screen gloud_sc():
    
    zorder 999

    on "show" action SetVariable("f_s", True)

    if f_s:
        add "white_exploder_burguer" at gloud_click
        timer 0.39 action [SetVariable("f_s", False), Hide("gloud_sc")]




transform gloud_click:
    subpixel True
    xalign 0.5 yalign 0.5
    easein 0.37 alpha 0.00



transform didatic_victory_game:
    subpixel True
    yalign -0.5 xalign 0.5
    on show:
        easeout_cubic .45 yalign 0.5
        .25
        block:
            pos (0.5, 0.5) 
            anchor (0.5, 0.5)
            linear .45 zoom 1.5
            .2
            linear .45 zoom 1.0

    on hide:
        easein .24 alpha 0.00

transform didatic_defeat_game:
    subpixel True
    yalign -0.5 xalign 0.5
    on show:
        easeout_cubic .45 yalign 0.5
        .25
        block:
            pos (0.5, 0.5) 
            anchor (0.5, 0.5)
            linear .45 zoom 1.5
            .2
            linear .45 zoom 1.0

    on hide:
        easein .24 alpha 0.00

init python:
    switch = True

    def right_or_left(d):
        if switch:
            return At(d, slide_right)
        else:
            return At(d, slide_left)


transform slide_left:
    subpixel True
    xpos 1350
    ypos -320
    zoom 0.6
    easein_elastic .25 xpos -150 ypos -70 # se mueve al lado izquierdo

transform slide_right: 
    subpixel True
    xpos -1350
    ypos 320
    zoom 0.6
    easein_elastic .25 xpos -150 ypos -70  # se mueve al lado izquierdo


transform character_a_z:
    subpixel True
    #alpha 0.00
    #yoffset 100
    zoom 0.6
    yalign 0.2
    xoffset -150
    yoffset -100
    alpha 0.00
    easein .75 alpha 1.00 xalign 0.2



transform character_a_z2:
    subpixel True
    #alpha 0.00
    yoffset 5
    on show:
        zoom 0.65
        alpha 0.00
        easein .2 alpha 1.00
    on replace:
        easein .2 alpha 0.00 

transform character_a_z3:
    subpixel True
    #alpha 0.00
    yoffset 40
    on show:
        zoom 0.65
        alpha 0.00
        easein .2 alpha 1.00
    on replace:
        easein .2 alpha 0.00

transform pos_character(x=550, z=0.64, xz=1.00):
    subpixel True
    yanchor 1.00
    xzoom xz
    zoom z
    ypos 1.00
    yoffset 40
    on show:
        easein .5 xcenter x #xoffset 0



#transform pos_character_burguer(z=0.8):
    

transform shake_slow_burguer(ts=1.0, z=0.8):
    subpixel True
    xalign 0.8 zoom z yoffset 0
    block:
        easein ts xoffset -4 yoffset 1
        easein ts xoffset 4 yoffset -1
        easein ts xoffset 2 yoffset -2
        easein ts xoffset -4 yoffset 1
        easein ts xoffset 0 yoffset 0
        easein ts xoffset -4 yoffset 1
        easein ts xoffset 4 yoffset -1
        easein ts xoffset 2 yoffset -2
        easein ts xoffset -3 yoffset 1
        easein ts xoffset 0 yoffset 0
        repeat



transform low_a(y=55):
    subpixel True
    easein 2.5 yoffset y






# Transform with glitch-like movement and optional sound on appearance
transform mov_glitch(x=950, z=0.62, yoff=40, y=1.00):
    subpixel True

    # Anchor and initial transform setup
    yanchor 1.00
    xzoom 1.00
    ypos y
    zoom z
    yoffset yoff

    # When this transform is first shown on screen
    on show:
        function reset_alpha       # Reset alpha to default (if needed)
        function reset_zoom        # Reset zoom to default (if needed)
        alpha 0.76                 # Start slightly transparent
        xcenter x                  # Position X (centered)
        linear 0.2 zoom 0.64 alpha 1.00  # Zoom in and fade in quickly

        block:
            function sound_glitch  # Play glitch sound once (with 40% chance)
            1.0
            repeat                 # Loop the pause, not the sound

    # When image is replaced by another with same tag
    on replace:
        function reset_alpha
        function reset_zoom
        easein .75 xcenter x zoom 0.64

    # When image is hidden
    on hide:
        alpha 0.0



# Transform normal of character
transform mov_t(x=950, z=0.62, yoff=40, y=1.00, xoff=0):
    subpixel True
    yanchor 1.00
    xzoom 1.00
    ypos y
    zoom z
    xoffset xoff
    yoffset yoff
    on show:
        function reset_alpha
        function reset_zoom
        alpha 0.85 xcenter x
        easein .2 zoom 0.64 alpha 1.00
    on replace:
        function reset_alpha
        function reset_zoom
        choice:
            easein .1 yzoom 0.99
            easein .1 yzoom 1.00
        choice:
            easein .1 yzoom 1.01
            easein .1 yzoom 1.00
        choice:
            pass
        easein .2 xcenter x zoom 0.64 xoffset 0
    on hide:
        alpha 0.0



transform move_mid_history:
    mov_t(x=950)

transform move_left_history:
    mov_t(x=550)

transform move_right_history:
    mov_t(x=1320)


transform move_left_screen(z=0.62, yoff=40, y=1.00, xoff=-90):
    subpixel True
    yanchor 1.00
    xzoom 1.00
    ypos y
    zoom z
    xoffset xoff
    yoffset yoff

    function reset_alpha
    function reset_zoom
    alpha 0.32 xcenter 550
    xoffset 1800
    pause .2
    ease .65 zoom 0.64 alpha 1.00 xoffset xoff

transform move_right_screen(z=0.62, yoff=40, y=1.00, xoff=-90):
    subpixel True
    yanchor 1.00
    xzoom 1.00
    ypos y
    zoom z
    xoffset xoff
    yoffset yoff

    function reset_alpha
    function reset_zoom
    alpha 0.32 xcenter 550
    xoffset -1500
    pause .2
    ease .65 zoom 0.64 alpha 1.00 xoffset xoff





# transform move_mid():
#     mov_t(x=950, z=0.64, yoff=40)
#     parallel:
#         pause .2
#         contains animation_jumping()

# transform move_right():
#     mov_t(x=1320, z=0.64, yoff=40)
#     parallel:
#         pause .2
#         contains animation_jumping()



init python:
    
    xpos_origin = 950

    def move_mid_(trans, st, at):
        xpos_origin = 950
        trans.xcenter = xpos_origin
        trans.alpha = 1.0
        return None


    def move_left_(trans, st, at):
        xpos_origin = 550
        trans.xcenter = xpos_origin
        trans.alpha = 1.0
        return None


    def move_right_(trans, st, at):
        xpos_origin = 1320
        trans.xcenter = xpos_origin
        trans.alpha = 1.0
        return None

    def move_t_screen_animation(trans, st, at):
        global move_animation_left_right
        if move_animation_left_right:
            if renpy.random.random() < 0.8:
                trans.xcenter = 2200
            else:
                trans.xcenter = -550

        return None


transform move_t_screen(x, z=0.64, zx=1.00, ats=.45):
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom z
    yoffset 40
    # function move_t_screen_animation
    on show:
        easein ats xcenter x


    # on replace:
    #     easein .75 xcenter x
transform move_t_screen_instant(x=950, z=0.64, zx=1.00, ats=.45):
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom z
    yoffset 40
    # function move_t_screen_animation
    ease .75 xcenter x





# transform move_exit_screen(z=0.64, yoff=40, y=1.00, xoff=-90):
#     subpixel True
#     yanchor 1.00
#     xzoom 1.00
#     ypos y
#     zoom z
#     xoffset xoff
#     yoffset yoff

#     # function reset_alpha
#     # function reset_zoom
#     xcenter 550
#     choice:
#         ease .75 xcenter -1350 alpha 0.00
#     choice:
#         ease .75 xcenter 1700 alpha 0.00

transform move_exit_random(): 
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom 0.64
    yoffset 40
    choice:
        ease .65 xcenter -1350 alpha 0.00
    choice:
        ease .65 xcenter 1700 alpha 0.00



transform move_exit_right(): 
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom 0.64
    yoffset 40
    ease .65 xcenter -1350 alpha 0.00

transform move_exit_left(): 
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom 0.64
    yoffset 40
    ease .65 xcenter 1700 alpha 0.00


transform move_left(): 
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom 0.64
    yoffset 40
    # function move_t_screen_animation
    xcenter 450


transform move_left_animate(): 
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom 0.64
    yoffset 40
    # function move_t_screen_animation
    ease .60 xcenter 470

transform move_mid():  
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom 0.64
    yoffset 40
    # function move_t_screen_animation
    ease .60 xcenter 950

transform move_right():
    subpixel True
    yanchor 1.00
    # xzoom zx
    ypos 1.00
    zoom 0.64
    yoffset 40
    # function move_t_screen_animation
    ease .60 xcenter 1320

transform move_inf():
    move_t_screen_instant(x=500)



transform animation_jumping():
    function reset_alpha
    function reset_zoom
    choice:
        easein .1 yzoom 0.99
        easein .1 yzoom 1.00
    choice:
        easein .1 yzoom 1.01
        easein .1 yzoom 1.00
    choice:
        pass


transform face_z(x=950, z=1.45, zx=1.00):
    subpixel True
    yanchor 1.00
    xzoom zx
    ypos 1.00
    parallel:
        linear 0.5 zoom z yoffset 1200 xcenter x 


transform face_z_left(x=950, z=0.64, zx=1.00):
    subpixel True
    yanchor 1.00
    xzoom zx
    ypos 1.00
    parallel:
        ease 0.3 zoom z yoffset 40 xcenter x 



#################################################################
###############################################################





transform animation_effect_bath(x=0.5, y=-0.05):
    subpixel True
    xalign x yalign y
    block:
        easein 15 yalign 0.9
        pause 1
        easein 15 yalign 0.05
        pause 1
        repeat


transform move_screen_alc:
    subpixel True
    zoom 1.1 align(0.5, 0.5)
    block:
        choice:
            easein 6 xzoom 1.1 xoffset 5 rotate 4
        choice:
            easein 6 xzoom 1.1 xoffset -5 rotate -4
        easein 3 xzoom 1.05 xoffset 0 rotate 0
        repeat


transform inf_image_move:
    subpixel True
    block:
        xpan 0
        linear 120 xpan 360
        repeat

#############################################################

# SHAKES

transform shake(ts=0.08):
    linear ts xoffset -2 yoffset 2
    linear ts xoffset 3 yoffset -3
    linear ts xoffset 2 yoffset -2
    linear ts xoffset -3 yoffset 3
    linear ts xoffset 0 yoffset 0
    linear ts xoffset -3 yoffset 1
    linear ts xoffset 3 yoffset -3
    linear ts xoffset 2 yoffset -2
    linear ts xoffset -2 yoffset 1
    linear ts xoffset 0 yoffset 0
    repeat


transform shake_gl(ts=0.01):
    linear ts xoffset -8 yoffset 2
    linear ts xoffset 7 yoffset -3
    linear ts xoffset 6 yoffset -4
    linear ts xoffset -4 yoffset 3
    linear ts xoffset 5 yoffset 2
    linear ts xoffset -5 yoffset 4
    linear ts xoffset 3 yoffset -6
    linear ts xoffset 4 yoffset -8
    linear ts xoffset -6 yoffset 1
    linear ts xoffset 4 yoffset 2
    linear ts xoffset 0 yoffset 0
    repeat

transform shake_gl_try(ts=0.01, r=9):
    linear ts xoffset -8 yoffset 2
    linear ts xoffset 7 yoffset -3
    linear ts xoffset 6 yoffset -4
    linear ts xoffset -4 yoffset 3
    linear ts xoffset 5 yoffset 2
    linear ts xoffset -5 yoffset 4
    linear ts xoffset 3 yoffset -6
    linear ts xoffset 4 yoffset -8
    linear ts xoffset -6 yoffset 1
    linear ts xoffset 4 yoffset 2
    linear ts xoffset 0 yoffset 0
    repeat r



transform shake_slow(ts=0.1):
    linear ts xoffset -2 yoffset 2
    linear ts xoffset 3 yoffset -3
    linear ts xoffset 2 yoffset -2
    linear ts xoffset -3 yoffset 3
    linear ts xoffset 0 yoffset 0
    linear ts xoffset -3 yoffset 1
    linear ts xoffset 3 yoffset -3
    linear ts xoffset 2 yoffset -2
    linear ts xoffset -2 yoffset 1
    linear ts xoffset 0 yoffset 0
    repeat




transform shake_slow_background(ts=0.1, xf=1, xf_n=-0.5, yf=0, yf_n=0.5, ps=2.0):
    subpixel True
    easein ts xoffset xf yoffset yf
    easein ts xoffset xf_n yoffset yf_n
    easein ts xoffset xf yoffset yf
    easein ts xoffset xf_n yoffset yf_n
    easein ts xoffset xf yoffset yf
    easein ts xoffset xf_n yoffset yf_n
    easein ts xoffset xf yoffset yf
    easein ts xoffset xf_n yoffset yf_n
    easein ts xoffset xf yoffset yf
    easein ts xoffset xf_n yoffset yf_n
    pause ps
    repeat






transform shake_more_slow:
    easein 1.0 xoffset -2 yoffset 2
    easein 1.0 xoffset 3 yoffset -3
    easein 1.0 xoffset 2 yoffset -2
    easein 1.0 xoffset -3 yoffset 3
    easein 1.0 xoffset 0 yoffset 0
    easein 1.0 xoffset -3 yoffset 1
    easein 1.0 xoffset 3 yoffset -3
    easein 1.0 xoffset 2 yoffset -2
    easein 1.0 xoffset -2 yoffset 1
    easein 1.0 xoffset 0 yoffset 0
    repeat


transform shake_one:
    linear 0.1 xoffset -2 yoffset 2
    linear 0.1 xoffset 3 yoffset -3
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0
    linear 0.1 xoffset -3 yoffset 1
    linear 0.1 xoffset 3 yoffset -3
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -2 yoffset 1
    linear 0.1 xoffset 0 yoffset 0
    repeat 8



transform shake_one_fast:
    linear 0.01 xoffset -3 yoffset 2
    linear 0.01 xoffset 3 yoffset -3
    linear 0.01 xoffset 1 yoffset -2
    linear 0.01 xoffset -4 yoffset 3
    linear 0.01 xoffset 0 yoffset 0
    linear 0.01 xoffset -3 yoffset 1
    linear 0.01 xoffset 4 yoffset -3
    linear 0.01 xoffset 5 yoffset -2
    linear 0.01 xoffset -3 yoffset 1
    linear 0.01 xoffset 0 yoffset 0
    repeat 12



transform shake_one_card:
    subpixel True
    zoom 0.5
    linear 0.1 xoffset 2
    linear 0.1 xoffset -2
    linear 0.1 xoffset 0


#############################################################



transform dissolve_screen_t(t=0.2):

    alpha 0.00 zoom 1.15 xalign 0.5
    block:
        linear t alpha 1.00 zoom 1.00 xalign 0.5
    
    on hover:
        function sound_kick



transform card_zoom:
    zoom 0.5



transform icon_transform_def:
    zoom 0.3
    xoffset 1

transform icon_transform_def2:
    zoom 0.5
    xoffset 1

transform icon_transform_def3:
    zoom 0.45
    xoffset 1


transform time_pos:
    xalign 0.70
    yalign 0.06

transform time_pos2:
    xalign 0.71
    yalign 0.06
    zoom 0.95



transform logo_rotate2(x=-0.75, y=0.5, t=8, z=1.6, ax=1.00):
    subpixel True
    zoom z
    xalign x
    yalign y
    alpha ax
    block:
        rotate 360
        linear t rotate 0
        repeat


transform up_word:
    easeout_cubic .4 yoffset 2
    easeout_cubic .4 yoffset -2
    easeout_cubic .4 yoffset 0
    repeat



transform icon_zoom(z=0.5):
    zoom z


















##############################################################

# ANIMATION BUTTON

###############################################################


transform zoom_timer:
    subpixel True
    linear .10 zoom 1.05
    linear .10 zoom 1.0
    repeat

transform zoom_timer2:
    subpixel True
    linear 1 zoom 1.05
    linear 1 zoom 1.0
    repeat



transform tack_button_right:
    subpixel True
    zoom 0.5 xoffset 330
    on hover:
        parallel:
            easein .25 xoffset 350
            easein .25 xoffset 330
        parallel:
            easein .10 zoom 0.45
            easein .10 zoom 0.5




transform tack_button_left:
    subpixel True
    xzoom -1 zoom 0.5 xoffset -450
    on hover:
        parallel:
            easein .25 xoffset -470
            easein .25 xoffset -450
        parallel:
            easein .10 zoom 0.45
            easein .10 zoom 0.5




transform tack_button_ok:
    subpixel True
    zoom 0.5 xalign 0.11 yalign 0.5
    on hover:
        easein .10 zoom 0.6 xalign 0.11
        easein .10 zoom 0.5 xalign 0.11


transform tack_button_work:
    subpixel True
    zoom 1.0
    on hover:
        easein .10 zoom 1.20
        easein .10 zoom 1.00


transform tack_button_sx:
    subpixel True
    zoom 1.0
    on hover:
        easein .10 zoom 1.04
        easein .10 zoom 1.00



transform tack_button_2:
    subpixel True
    zoom 0.5
    on hover:
        easein .10 zoom 0.55
        easein .10 zoom 0.5




transform position_button_exit:
    xalign 0.5
    yalign 0.5
    zoom 1.5


transform position_button_exit2:
    xalign 0.5
    yalign 1.0
    yoffset 100
    zoom 1.5


transform button_animation_exit:
    on hover:
        easein .25 zoom 1.1
        easein .25 zoom 1.0

transform button_animation_exit2:
    on hover:
        easein .25 zoom 1.05
        easein .25 zoom 1.0

###########################################################
############################################################



# init python:
#     class Screen_Move_Render(renpy.Displayable):
#         def __init__(self, **kwargs):
#             super(Screen_Move_Render, self).__init__(**kwargs)
#             self.x = 0
#             self.y = 0
#             self.shake_duration = 0
#             self.shake_force = 0

#             #self.child = renpy.display.layout.Fixed()

#             # Añadir screen renderizado como Displayable
#             #self.child.add(renpy.display.screen.ScreenDisplayable("screen_config", tag="screen_config", layer="master"))
#             #self.child.add(renpy.display.screen.ScreenDisplayable("bg_screen", tag="bg_screen", layer="master"))
#             #self.child.add(renpy.display.screen.ScreenDisplayable("character_show", tag="character_show", layer="master"))


#             #screen_disp = renpy.display.screen.ScreenDisplayable("screen_config", tag="screen_config", layer="master")
#             #self.child.add(screen_disp)

#         def render(self, width, height, st, at):
#             render = renpy.Render(width, height)

#             # Shake activo
#             if self.shake_duration > 0:
#                 dx = random.randint(-self.shake_force, self.shake_force)
#                 dy = random.randint(-self.shake_force, self.shake_force)
#                 self.shake_duration -= renpy.get_frame_time()
#             else:
#                 dx = dy = 0

#             child_render = renpy.render(self.child, width, height, st, at)
#             render.blit(child_render, (self.x + dx, self.y + dy))
#             return render

#         def visit(self):
#             return [self.child]

#         # Método para moverlo desde Python si deseas más control
#         def mover(self, x, y):
#             self.x = x
#             self.y = y

#label start:
    #show expression mother_screen_base as mother_screen_base onlayer master

    #"Aquí está todo normal."

    #"¡Ahora sacudo el universo!"
    #$ mother_screen_base.shake(duration=1.0, force=20)







########################################################################
########## TRANSFORM NOTIFY ####################################


transform notify_afecto:
    subpixel True
    alpha 1.00
    align(0.1, 0.5)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 3.2 yoffset -80 alpha 0.00
        
    #on replace:
        #easein .7 yoffset -80 alpha 1.00
        #pause .7
        #easein .7 yoffset -80 alpha 0.00


transform notify_afecto_b:
    subpixel True
    alpha 1.00
    align(0.2, 0.35)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 3.2 yoffset -80 alpha 0.00



transform notify_afecto2:
    subpixel True
    alpha 1.00
    align(0.2, 0.7)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 3.2 yoffset -80 alpha 0.00

transform notify_afecto2_b:
    subpixel True
    alpha 1.00
    align(0.3, 0.6)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 3.2 yoffset -80 alpha 0.00




transform notify_afecto3:
    subpixel True
    alpha 1.00
    align(0.05, 0.3)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 3.2 yoffset -80 alpha 0.00



transform notify_afecto3_b:
    subpixel True
    alpha 1.00
    align(0.05, 0.3)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 3.2 yoffset -80 alpha 0.00



transform notify_afecto4:
    subpixel True
    alpha 1.00
    align(0.34, 0.4)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 3.2 yoffset -100 alpha 0.00


transform notify_afecto4_b:
    subpixel True
    alpha 1.00
    align(0.25, 0.5)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 3.2 yoffset -100 alpha 0.00





transform notify_afecto_card:
    subpixel True
    alpha 1.00
    align(0.1, 0.2)
    zoom 1.6
    #on show:
        #easein .7 yoffset -80 alpha 0.00
    easein 1.0 yoffset -80 alpha 0.00

#########################################################################
#######################################################################














###################################################
# TRANSICIONES
define dissolve = Dissolve(.2)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(0.2),
    Solid("#000"), Pause(0.2),
    Solid("#000"), Dissolve(0.2),
    True])

define flash = Fade(0.1, 0.0, 0.3, color="#fff")

define wipeleft = ImageDissolve("wipeleft.png", 0.5, ramplen=64)

define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("wipeleft.png", 0.2, ramplen=64),
    Solid("#000"), Pause(0.20),
    Solid("#000"), ImageDissolve("wipeleft.png", 0.2, ramplen=64),
    True])


define dissolve_scene_exit = MultipleTransition([
    False, ImageDissolve("transparent_image2.png", 0.1, ramplen=64),
    Solid("#000"), Pause(.25),
    Solid("#000"), ImageDissolve("transparent_image2.png", 0.1, ramplen=64),
    True])

define dissolve_scene_full_slow = MultipleTransition([
    False, Dissolve(1.5),
    Solid("#000"), Pause(0.1),
    Solid("#000"), Dissolve(0.8),
    True])



define wipe_scene = MultipleTransition([
    False, ImageDissolve("wipe_papel.png", 0.9, ramplen=60),
    Solid("#000"), Pause(0.20),
    Solid("#000"), ImageDissolve("wipe_papel.png", 0.9, ramplen=60),
    True])


define clounds_scene = MultipleTransition([
    False, ImageDissolve("clounds.jpg", 0.4, ramplen=54),
    Solid("#000"), Pause(0.50),
    Solid("#000"), ImageDissolve("clounds.jpg", 0.4, ramplen=54),
    True])



define o_c_eyes_s = MultipleTransition([
    False, Dissolve(0.1),
    Solid("#000"), Pause(0.1),
    Solid("#000"), Dissolve(0.1),
    True])


define logo_scene = MultipleTransition([
    False, ImageDissolve("transition_logo.png", 1.4, ramplen=6),
    Solid("#000"), Pause(1.0),
    Solid("#000"), ImageDissolve("wipeleft.png", 1.4, ramplen=64),
    True])

define logo_scene_flash = MultipleTransition([
    False, ImageDissolve("transition_logo.png", 0.4, ramplen=54),
    Solid("#000"), Pause(0.20),
    Solid("#000"), ImageDissolve("transition_logo.png", 0.4, ramplen=54),
    True])

define multi_fort_scene = MultipleTransition([
    False, ImageDissolve("transition_dez.png", 0.3, ramplen=84),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("transition_dez.png", 0.3, ramplen=84),
    True])


define multi_scene = ImageDissolve("transition_multi.png", 1.0, 8)

define master_scene = ImageDissolve("transition_flash.png", 3.0, 64)

define left_transition = MoveTransition(delay=0.01, enter=wipeleft, leave=wipeleft, old=False, layers=['master'], time_warp=_warper.linear, enter_time_warp=_warper.linear, leave_time_warp=_warper.linear)

###################################################





####################################################################
########### ANIMACIONES DEL MAPA ###################################
# de todos modos luego se tendra que cambiar ya que se actualizara el mapa #~########

# transform olas_animation:
#     animation
#     subpixel True
#     xalign 0.0 xsize 360
#     block:
#         easein 3 xsize 400 xoffset -20
#         pause .25
#         easein 3 xsize 360 xoffset -40
#         pause .25
#         easein 3 xsize 400 xoffset -20
#         pause .25
#         repeat
            

# transform auto_red:
#     subpixel True
#     xpos 575 ypos -200
#     block:
#         linear 6 ypos 1200
#         pause 10
#         ypos -200
#         pause 2
#         repeat


# transform auto_blue:
#     subpixel True
#     xpos 1915 ypos 415 rotate 90
#     block:
#         linear 6 xpos 1150
#         linear .2 rotate 0 ypos 420
#         linear 2 xpos 1150 ypos 690 rotate 0
#         #pause 2
#         linear .2 rotate -90
#         linear 6 xpos 2000 ypos 690
#         pause .6
#         xpos 1915 ypos 415 rotate 90
#         repeat
        

transform fly_1_animation(z=1.5, alp=0.4):
    animation
    subpixel True
    alpha alp
    #xpos 2000 ypos 1200 rotate -90 #ypos 500
    zoom z
    choice:
        block:
            choice:
                ypos 700 xpos 1900 rotate 0
            choice:
                ypos 100 xpos 1900 rotate 0
            choice:
                ypos 800 xpos 1300 rotate 0
            parallel:
                choice:
                    linear 18 xpos -1200
                choice:
                    linear 26 xpos -1000
                choice:
                    linear 32 xpos -800
                choice:
                    xpos -3000
            pause 5
            repeat
    choice:
        block:
            choice:
                ypos 400 xpos 1800 rotate 0
            choice:
                ypos 800 xpos 1800 rotate 0
            choice:
                ypos 100 xpos 1800 rotate 0
            parallel:
                choice:
                    linear 33 xpos -1000
                choice:
                    linear 24 xpos -999
                choice:
                    linear 26 xpos -800
                choice:
                    xpos -3000
            pause 5
            repeat



transform move_card_right(xz=-1.0):
    subpixel True
    easein .7 xsize xz

transform move_card_left(xz=1.0):
    subpixel True
    easein .7 xsize xz

###############################################################################
##########################################################################
