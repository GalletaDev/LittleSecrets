



#### AL empaquetar el juego esto debe estar en True

# define mod_assets = True

default persistent.languaje_narrator = "english"

default persistent.choice_game = True
default persistent.Demo_game = False
#####################################
default persistent.skip_splascreen_game = False
init python:
    # _dismiss_pause = config.developer
    config.keymap["game_menu"].remove("mouseup_3")
    config.keymap["hide_windows"].remove("mouseup_2")

    config.has_autosave = False
    config.has_quicksave = False


default dificulty_mode_game = "" # la dificultad del juego

default mode_history_game = False
default mode_infinity_game = False
default mode_extreme_game = False

define player_dialog_available = ["azuli_", "milia_", "cristal_", "blody_"]

# Interruptores

default day_already_configured = False # verificador de dia para no repetir ciclos
default broken_object_player = False # verificador de no romper parametros

############################################################
################################################################

default time_global_ = "normal" # tiempo del mapa si llueve o no

####################################################

# VARIABLES DEL SISTEMA personaje y barras
default afecto = Affection(_("Afecto"), 0, 10_000_00) # Barra de afecto
default money_player = Money(_("Dinero"), 0, 10_000_00) #  Barra de dinero
default lust_ = Lust(_("Lujuria"), 0, 100)
default love_ = Love(_("Girl"), 0, 3000)#  Barra de amor

###################################################################
# Ejemplo :
#
#$ love_.add_love(100) para usar
#$ love_.remove_love(100) para usar
#
#$ afecto.add_affection(100) para usar
#$ afecto.remove_affection(100) para usar
#
#$ money_player.add_money(100) para usar
#$ money_player.remove_money(100) para usar
#
# la lujuria son muy pequeñas cantidades
#$ lust_.add_lust(5) para usar
#$ lust_.remove_lust(5) para usar
#
###################################################################

default expression_face_ = True

default warning_love = 50 # inicial
default warning_love_max = 2000 # maximo
default warning_affection_max = 3000 # maximo

default tmx = NANOSECONDPY

default talk_times = 0
default b_choice_times = 0
default rps_times = 0

####################################################
# VARIABLES DE ARCHIVOS CARGADOS

define inv_image_object = JSON_("data_library_json/OBJ_IMAGE_BUTTON.json")

####################################################
# VARIABLES DEL SISTEMA Little Secrets
default character_gift = CharacterPreferences() # los gustos del personaje
default inv_object = InvObjectGift() # Comprador de objetos y regalos
default bag_inv = Bag() # Mochila de objetos e inventario de regalos
default combiner_inv = GiftCombiner(bag_inv) # conbinador de objectos en Bag
default category_girl = Category_g()
default health_character = Health(name=_("Estado"), scale="1", status="good", image_p="icon_list_category/status_life/no_7.png") # estado del personaje
default time_p = Time() # Tiempo del juego

default chr3_game = ActionCounter()

# init python:

#     def force_save():
#         global character_gift, inv_object, bag_inv, combiner_inv, category_girl, health_character, time_p
        
#         # Reasignar cada objeto al store para que Ren'Py lo detecte como modificado
#         character_gift = character_gift
#         inv_object = inv_object
#         bag_inv = bag_inv
#         combiner_inv = combiner_inv
#         category_girl = category_girl
#         health_character = health_character
#         time_p = time_p

#         # Opcional: reinicia la UI si quieres que la pantalla se actualice inmediatamente
#         print("Force save executed.")
#         renpy.restart_interaction()
####################################################

default chair_npc_is = ""
default select_npc_shop = ""

####################################################

####################################################


default persistent.chapter_int1 = True
default persistent.chapter_int2 = True
default persistent.chapter_int3 = True


####################################################
# Personaje del sistema
define narrator = Character("", 
    what_color="#66C3FE", 
    what_prefix="'", 
    what_suffix="'")


define ssi = Character("", 
    screen="say_system", 
    what_size=32, 
    what_font="font/lick_big.ttf")


define my_centered = Character("", 
    what_color="#fff", 
    screen="say_centered", 
    what_size=36)

############################################################
# Protagonist jugador
define mc = Character("{font=font/folder_regular.ttf}{color=#EE0D0D}[mc_name!t]{/color}{/font}",
    what_prefix="「", 
    what_suffix="」", 
    callback=speaker("mc"))

# El personaje elegido
define g = Character("{font=font/folder_regular.ttf}[chr2_game.g_name]{/font}", 
    image="[chr2_game.s_chr]", 
    what_color="#ffffff", 
    what_prefix="「", 
    what_suffix="」", 
    callback=speaker("g"))

# NPC UNIVERSAL
define npc = Character("[npc_name!t]", 
    image="[npc_chr]", 
    what_prefix="'", 
    what_suffix="'", 
    callback=speaker("npc"))


##############################################################################
# Npc que solo aparece en Azuli
define mi = Character("[mi_name!t]", image="[npc_chr]", callback=speaker("mi")) # miko
define al = Character("[al_name!t]", image="altair_", callback=speaker("al")) # altair
define w = Character("[w_name!t]", callback=speaker("w"))

####################################################

define mc_name = "Kris" #prota
define npc_name = "" # nombres aleatorios

#############################
define w_name = "???" # Pink
##########################
define al_name = "Altair" # altair
define mi_name = "???" # miko

# default persistent.house_name_player = _("Mi Casa [mc_name!t]") # nombre de la casa del jugador

###################################################
define NANOSECONDPY = 1e-9
define SECONDPY = 0.00_0001

###################################################
default day = 1 # dias del juego
default week = 0 # semanas del juego / no hay meses

define name_day = [
    _("Lunes"), 
    _("Martes"), 
    _("Miércoles"), 
    _("Jueves"), 
    _("Viernes"), 
    _("Sábado"), 
    _("Domingo")
    ]




###################################################
# VARIABLES QUE CAMBIAN CONSTANTEMENTE
default current_day_name = ""
default activate_night_red = False # modo de noche roja
default night_red = False # noche roja activador
default day_beach_activate = False # modo de dia de playa

default persistent.girl_death = 0 # cantidad de veces que murio el personaje
###################################################



default love_add_tutorial = False # un tutorial pequeño de como jugar

default current_category_w = 0 # cantidad inicial de categorias

default max_category_w = 5 # cantidad maxima de categorias

default name_max_category = "max_category_"

###################################################

default menu_name = "_map_screen"

default location_choice_map = "house"

default moving_to_player = False
default again_animation = 1

default bot_is_exiting = False
default again_animation_exit = 1

default location_transform = "static"

default screen_name_map = "menu_"

default name_exit_character = "finish_exit_"

default select_ok_appointent = False
default outside_home = True # lo mismo pero con el jugador
default outside_girl = True # Es cuando esta adentro. (True) adentro, (False) afuera

default outside_exit_house_ = False # por si acaso da error de sintaxis al salir

####################################################

default pos_chr = "mid" # pos_chr
default last_chr = None

default character_bg = "character_"
#default clothe_character = "clothe1"
default ex_chr = "normal"
default activate_effect_bg = False

####################################################

default npc_appar = False

default npc_chr = ""

default ex_npc = "normal"

default pos_npc = "mid"

########################################
##### Funcion Music channel #######################


###################################
default character_select = ""
default image_base_character = "character_"
default history_label = "history_"
default status_label = "status_"
default category_label = "category_"

#################################################

default fuction_name_eat = "function_fail_eat_"
default fuction_name_bath = "function_fail_bath_"
default fuction_name_tele = "function_fail_tele_"

###################################################

default chat_label = "chat_"

default select_chat_random = "1"
########################################################

default player_rps = ""
default enemy_rps = ""


######################################

default gift_select = ""
default gift_true_confirm = False

##########################################


default eat_character = False
default tele_character = False
default bath_character = False
default sleep_character = False


############################################
#### LISTA DE CATEGORIAS DE CADA PERSONAJE #######
#########################################################
# Categorías para cada personaje
#   Azuli = [Buena ,Desconfianza]
#   Folahm = [Normal, Confianza]
#   Cristal = [Tsundere, Enojada, Cocinera, Valiente] Solo uno puede tener
#   Inosuki = []
#
#
###########################################################

#label start:
    #"El personaje tiene las siguientes categorías: [category_cristal]"
    #$ dialog_text = get_character_dialog(category_cristal)
    #"[dialog_text]"

###############################
#### Fuction current cookie


define current_number = 0
default work_yeah = False


##############################################
#
#
#########################################


# default touch_vacio_ = 0
# default touch_cristal_ = 0
# default touch_blody_ = 0

######################## SPECIAL

default tsundere_c = NameCategory(_("Arbitrary"), "special" , "icon_list_category/tsundere_p.png", "#1") #1
default good_c = NameCategory(_("Good"), "special" , "icon_list_category/buena_p.png", "#2") #2
default child_c = NameCategory(_("Childish"), "special", "icon_list_category/infantil_p.png", "#18") #18
default requirement_c = NameCategory(_("Demanding"), "special", "icon_list_category/requisito_p.png", "#21") #21
default yandere_c = NameCategory(_("Yandere"), "special", "icon_list_category/yandere_p.png", "#22") #22
default intelligent_c = NameCategory(_("Intelligent"), "special", "icon_list_category/inteligente_p.png", "#24") #24
default resent_c = NameCategory(_("Tolerant"), "special", "icon_list_category/tolerancia_p.png", "#26") #26

default secret_c = NameCategory(_("Secret"), "special" , "icon_list_category/secret_p.png", "#99") #1

######################## GOLD

default loving_c = NameCategory(_("Loving"), "gold" , "icon_list_category/amorosa_p.png", "#3") #3
default happy_c = NameCategory(_("Happy"), "gold" , "icon_list_category/feliz_p.png", "#7") #7
default disgust_c = NameCategory(_("Disgusting"), "gold", "icon_list_category/asquerosa_p.png", "#12") #12
default cook_c = NameCategory(_("Cook"), "gold", "icon_list_category/cocinera_p.png", "#17") #17
default ambitious_c = NameCategory(_("Ambitious"), "gold" , "icon_list_category/ambicioso_p.png", "#10") #10
default confidence_c = NameCategory(_("Confidence"), "gold", "icon_list_category/confianza_p.png", "#16") #16

######################## RARE

# default lust_c = NameCategory(_("Lust"), "rare" , "icon_list_category/lujuria_p.png", "#8") #8
default normal_c = NameCategory(_("Normal"), "rare", "icon_list_category/normal_p.png", "#15") #15
default cute_c = NameCategory(_("Beautiful"), "rare", "icon_list_category/hermosa_p.png", "#19") #19
default joker_c = NameCategory(_("Crazy"), "rare", "icon_list_category/loca_p.png", "#23") #23

######################## NORMAL

default charismatic_c = NameCategory(_("Charismatic"), "normal" , "icon_list_category/carismatica_p.png", "#4") #4 
default angry_c = NameCategory(_("Angry"), "normal" , "icon_list_category/enojada_p.png", "#5") #5 
default distrust_c = NameCategory(_("Distrustful"), "normal" , "icon_list_category/desconfianza_p.png", "#6") #6 
default foolish_c = NameCategory(_("Foolish"), "normal" , "icon_list_category/tonta_p.png", "#9") #9
default study_c = NameCategory(_("Studious"), "normal", "icon_list_category/estudiosa_p.png", "#11") #11
default hate_c = NameCategory(_("Hate"), "normal", "icon_list_category/odio_p.png", "#13") #13
default celos_c = NameCategory(_("Jealous"), "normal", "icon_list_category/celos_p.png", "#14") #14 ok
default brave_c = NameCategory(_("Brave"), "normal", "icon_list_category/valiente_p.png", "#20") #20
default otaku_c = NameCategory(_("Otaku"), "normal", "icon_list_category/otaku_p.png", "#25") #25

################################################
#
##############################################
#
################################################
################################################################################

# Button diccionario de working_game.rpy

define diccionario_intensity_1 = {
    "easy": "icon_list_category/working/intencidad_flow_hover.png",
    "normal": "icon_list_category/working/intencidad_normal_hover.png",
    "hard": "icon_list_category/working/intencidad_hardcore_hover.png",
    "extreme": "icon_list_category/working/intencidad_extreme_hover.png",
    "demente": "icon_list_category/working/intencidad_god_hover.png",
    "god": "icon_list_category/working/intencidad_now1_hover.png",
    "negation": "icon_list_category/working/intencidad_nwg_hover.png"
}

# {
#     "image": "gui/button_config_screen/button_two_exit_%s.png",
#     "action": If(lambda: time_global_ == "normal", true=lambda: renpy.jump("choice_map_" + chr2_game.s_chr), false=lambda: Play(channel='sound', file='audio/sfx/alerta_cancel.ogg')), # Accion de mover personaje desde la variable dinamico
#     "tooltip": _("Saldrás junto con [chr2_game.g_name]"),
# },

# diccionario de button_select_exit() >>> screen_map.rpy
# puede que en un futuro cambien -> agregar mas acciones
define button_data_select_exit = [
    {
        "image": "gui/button_config_screen/button_exit_%s.png",
        "action": [With(wipeleft_scene), SetVariable("outside_home", False), SetVariable("outside_girl", True), Jump("config_map_exit")],
        "tooltip": _("Saldrás tú solo"),
    },
    {
        "image": "gui/button_config_screen/button_work_%s.png",
        "action": [SetVariable("outside_home", False), SetVariable("outside_girl", True), Jump("working_game")],
        "tooltip": _("Vas a trabajar"),
    },
    {
        "image": "gui/button_config_screen/button_cancel_%s.png",
        "action": [SetVariable("outside_home", True), Jump("house_night_detected")],
        "tooltip": _("Cancelarás la salida"),
    }
]


####################################################################
########################################################################

# diccionario de nombre de ubicacion en screen_config.rpy
# Puede que un futuro cambie -> agregar botones para moverse mas
# default buttons_location = [
#     {"image": "resource/button_living_room_%s.png", "location": "living_room", "name": _("Sala principal")},
#     {"image": "resource/button_kitchen_%s.png", "location": "kitchen", "name": _("Cocina")},
#     {"image": "resource/button_bath_%s.png", "location": "bath", "name": _("Baño")},
#     {"image": "resource/button_room_%s.png", "location": "room", "name": _("Cuarto")},
#     ] OLD

define buttons_location_screen = [
    {
        "image": "resource/button_living_room_%s.png", 
        "location": "living_room", 
        "name": _("Sala principal"),
        },
    {
        "image": "resource/button_kitchen_%s.png", 
        "location": "kitchen", 
        "name": _("Cocina"),
        },
    {
        "image": "resource/button_bath_%s.png", 
        "location": "bath", 
        "name": _("Baño"),
        },
    {
        "image": "resource/button_room_%s.png", 
        "location": "room", 
        "name": _("Cuarto"),
        }
    ]



# button de moverse en casa screen_config.rpy
# Puede que un futuro cambie -> agregar mas imagenes para los botones
define button_images = {
    "living_room": "gui/button_config_screen/button_tv_%s.png",
    "kitchen": "gui/button_config_screen/button_eat_%s.png",
    "bath": "gui/button_config_screen/button_fish_%s.png",
    "room": "gui/button_config_screen/button_sleep_%s.png"
}


# imagenes de bg_screen() ubicado en screen_config
# Puede que un futuro cambie -> mas imagenes de las ubicaciones

#"house": bg_select + location_house,
define backgrounds = {
    "pizza": "bg/bg_pizzeria.png",
    "park": "bg/bg_park.png",
    "restaurant": "bg/bg_restaurant.png",
    "movie": "bg/bg_cine_location.png",
    "museum": "bg/bg_ayuntamiento.png",
    "shop": "bg/bg_shop.png",
    "beach": "bg/bg_beach.png",
    "house": "bg/sala_screen.png",
}


###################################################################

# cosas que dice en el parque el jugador

define dialog_player_c = [
    _("Siempre es el momento adecuado para hacer lo correcto."),
    _("No se trata de tener tiempo, se trata de hacer tiempo."),
    _("La vida es demasiado corta para estar enojado por cosas pequeñas."),
    _("Las grandes cosas nunca vienen de la zona de confort."),
    _("La actitud es una pequeña cosa que hace una gran diferencia."),
    _("Cada día es una nueva oportunidad para aprender algo nuevo."),
    _("No esperes que las oportunidades lleguen a ti; ve y búscalas."),
    _("A veces, el mayor riesgo es no tomar ninguno."),
    _("La vida no siempre es justa, pero eso no significa que no valga la pena vivirla."),
    _("La paciencia no es la capacidad de esperar, sino cómo te comportas mientras esperas."),
    _("La felicidad no es un destino, es una forma de viajar."),
    _("No se trata de cuántas veces caes, sino de cuántas veces te levantas.")
]







##########################################################
# Lista de posiciones transform del personaje, ya que no funcionan los de renpy
# para agregar una animación aquí 

default position_animation = ""

define position_mapping = {
    "left": move_left,
    "left_animate": move_left_animate,
    "mid": move_mid,
    "right": move_right,  
    "destroy": shake_gl,
    "zoom_face": face_z,
    "lost": low_a,
    "dist_chr": move_inf,
    "slide_left": move_left_screen,
    "slide_right": move_right_screen,
    "move_exit_right": move_exit_right,
    "move_exit_left": move_exit_left,
    "slide_exit": move_exit_random
    }

##########################################################
# Lista de imagenes de uso de fondo color de ambiente
# por si acaso puede que cambie con el tiempo
define backgrounds_liner = {
        "day": day_bg,
        "day2": day_bg,
        "afternoom": afternoom_bg,
        "afternoom2": afternoom_bg,
        "night": night_bg,
        "night2": night_bg,
        "night3": night3_bg
    }


##############################################################
# verifica el menu_option si la cancion se a bugueado por block in sinc
define music_reload_bug = {
        "day": "one_day_more",
        "day2": "one_day_more",
        "afternoom": "one_afternoom_more",
        "afternoom2": "one_afternoom_more",
        "night": "one_night_more",
        "night2": "one_night_more",
        "night3": "one_night_more"
    }


##########################################################
# Lista de imagenes de vignette para estados de emocion
# Animacion de vignette no mas
define backgrounds_vignette_use = {
        "hot": "bg/alpha_hot.png",
        "happy": "bg/alpha_happy.png",
        "sad": "bg/alpha_sad.png",
        "drunk": "bg/alpha_drunk.png",
        "medium": "bg/alpha_medium.png",
        "angry": "bg/alpha_angry.png",
        "boring": "bg/alpha_boring.png"
    }



##########################################################

# cosas que pueden decir algunos personajes, aunque los deje alli por si acaso

define azuli_quotes = [
    "¿Por qué me miras así? Jeje… ¿acaso sospechas de mí?",
    "El amor es bonito… hasta que deja de serlo.",
    "No tienes que saberlo todo. Hay secretos que deben quedarse guardados.",
    "A veces sonrío… solo para que no preguntes.",
    "Yo no hice nada… ¿tú me crees, verdad?",
    "Prometiste no dejarme, ¿lo recuerdas?",
    "Todo lo que hago es por amor. Aunque duela.",
    "Si te contara mi secreto… ya no podrías escapar.",
    "Dicen que soy dulce… pero tú aún no me has visto en serio.",
    "Me gusta cómo me miras… como si no supieras nada.",
    "¿Qué harías si te mostrara mi verdadero yo?",
    "A veces me da miedo lo que siento… pero no puedo evitarlo.",
    "¿Tú también ocultas cosas, o solo yo?"
]




define milia_quotes = [
    "¿Qué pasa? Solo quiero estar contigo todo el tiempo, ¿es tan raro?",
    "Yo siempre consigo lo que quiero. Y ahora… te quiero a ti.",
    "No tienes que entenderlo, solo haz lo que te digo.",
    "¿Quién más te trataría tan bien como yo?",
    "¿Me estás evitando? Eso me pone triste… y ya sabes lo que pasa cuando me pongo triste.",
    "Las promesas rotas duelen… pero tú no romperías la tuya, ¿verdad?",
    "Tú y yo… para siempre. Eso fue lo que dijiste.",
    "No te preocupes por lo que hago cuando no estás. No te gustaría saberlo.",
    "A veces hay que hacer cosas feas por amor.",
    "¿Vas a dejarme? No creo que quieras hacer eso.",
    "Es tan fácil hacer que confíes en mí…"
]



define cristal_quotes = [
    "¿Quieres jugar conmigo? Prometo no lastimarte… esta vez.",
    "A veces oigo voces… pero no te preocupes, no hablan de ti… todavía.",
    "Me porto bien… cuando me conviene.",
    "¿Te gusta mi sonrisa? A muchos les gustó antes que a ti.",
    "Me dijeron que era especial… pero nadie me entiende como tú.",
    "Si desapareces, ¿me puedo quedar con tus cosas?"
]


define blody_quotes = [
    "¿Quién era ella? No me mientas.",
    "Tú me perteneces. No quiero tener que recordártelo.",
    "Te amo tanto que me duele… pero a ti te va a doler más si me mientes.",
    "Haré lo que sea para que no me dejes. Lo que sea.",
    "No me gusta cuando hablas con otras. Me hace querer hacer cosas malas.",
    "La sangre se limpia… los recuerdos, no.",
    "¿Sabes qué es lo peor? Que sigues pensando que esto es amor normal.",
    "No llores… aún no te he hecho nada.",
    "¿Te dolió eso? Imagina lo que viene si me traicionas.",
    "No importa cuántas veces te vayas… siempre sabré dónde encontrarte.",
    "No estoy loca. Estoy enamorada."
]



###############################################################


init python:

    select_line_index = 0

    def get_next_line(dialog_lines):
        global select_line_index
        line = dialog_lines[select_line_index]
        select_line_index = (select_line_index + 1) % len(dialog_lines)  # Reinicia al principio cuando llega al final
        return line