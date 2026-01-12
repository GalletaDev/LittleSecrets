




######################################################

# default id_bot = 1

default point_random_try = 1.0 # movimiento al 100 por ciento de las veces cuanto mas bajo mas veces se movera aleatoriamente

default interaction_bot = True # por si interactua con el bot

default location_character = "living_room" # el personaje sabra donde esta el jugador
default location_house = "living_room"

default BOT_CHR = False # Variable general de Bot

default timer_mov_ = 1.5
default pass_bot_time = 0

default timer_character_temporizer = 5.0

default bot_character_key = ""

default bot_timer_ready = True
default last_player_location = ""

#default bot_possible_positions_azuli_ = ["living_room", "kitchen", "bath", "room"]
#default bot_possible_positions_milia_ = ["living_room", "kitchen", "bath", "room"]
#default bot_possible_positions_cristal_ = ["living_room", "kitchen", "bath", "room"]
#default bot_possible_positions_blody_ = ["living_room", "kitchen", "bath", "room"]


default location_move = "location_" # movimientos del jugador en ubicacion

default location_str = _("Sala")


define characters_data = {
    "azuli_": {
        "possible_positions": ["living_room", "kitchen", "bath", "room"]
    },
    "milia_": {
        "possible_positions": ["living_room", "kitchen", "bath", "room"]
    },
    "cristal_": {
        "possible_positions": ["living_room", "kitchen", "bath", "room", "school_base", "sch_s1", "sch_s2", "sch_s3", "sch_s4"]
    },
    "blody_": {
        "possible_positions": ["living_room", "kitchen", "bath", "room", "school_base", "sch_s1", "sch_s2", "sch_s3", "sch_s4"]
    }
}

# listas posibles de ubicaciones

define location_house_available = {
    "living_room",
    "kitchen",
    "bath",
    "room",
    "school_base",
    "sch_s1",
    "sch_s2",
    "sch_s3",
    "sch_s4"
}


init python:

    # Valor por defecto

    def select_bot_character():
        """
        Esta acción se encarga de seleccionar un personaje para mover al bot
        Al seleccionar personaje se guarda el dato del personaje y asi sabra donde moverse
        """
        global bot_character_key
        try:
            bot_character_key = renpy.random.choice(list(characters_data.keys()))
        except Exception as e:
            print(f"List of moving not detect {e}")


    def move_bot_to_player(condition_love=400):
        """
        Esta acción se encarga a mover al bot a la ubicación del jugador
        normalmente se usa en el screen de character_show para mostrar el personaje
        """
        global love_, warning_love, location_character, location_house, again_animation, moving_to_player

        same_location = (location_character == location_house)
        
        if love_.quantity <= warning_love:
            if same_location:
                pass
            else:
                renpy.music.play("audio/sfx/alerta_ok.mp3", channel='sound')

        else:
            if renpy.random.random() < point_random_try:  # % de las veces te sigue
                if same_location:
                    # register_log("not follow player 🤔")
                    location_move_animation()
                    renpy.music.play("audio/sfx/alerta_ok.mp3", channel='sound')
                else:
                    # register_log("follow player 😗")
                    renpy.music.play("audio/sfx/walk.ogg", channel='sound')
                
                # usar animacion de izq o der


                renpy.store.location_character = renpy.store.location_house
            else:
                # register_log("Move random 🤫")
                # Se queda en su sitio o va a otro aleatorio
                again_animation = 1
                moving_to_player = True

                if love_.quantity >= condition_love:
                    options = [loc for loc in get_bot_positions() if loc != location_house]
                else:
                    options = [loc for loc in ["living_room", "kitchen"] if loc != location_house]

                if options:
                    renpy.store.location_character = renpy.random.choice(options)

                location_move_animation()
                

                
    def move_bot_obligatory():
        """
        Mueve el bot inmediatamente a la ubicación del jugador
        y activa la animación correspondiente.
        """
        global moving_to_player, again_animation

        # register_log("My move obligatory 😡")

        # Indicar que el bot se está moviendo
        again_animation = 1
        moving_to_player = True

        # Actualizar ubicación del bot
        renpy.store.location_character = renpy.store.location_house

        # Ejecutar la animación según estado actual
        location_move_animation()


    def get_bot_positions():
        return characters_data[bot_character_key]["possible_positions"]



