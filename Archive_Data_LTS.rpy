

#"chr_azuli.chr",
#"chr_folahm.chr",
#"chr_cristal.chr",
#"chr_inosuki.chr"

# CODIGO DE SISTEMA #####################################


init -11 python:

    _txt_cache = {}

    def LS_data_txt(file_path):
        """
        Carga un archivo .txt o .ls con formato clave = valor.
        Devuelve un diccionario, usando caché si ya fue leído antes.
        Detecta automáticamente int, float y bool.
        """
        if file_path in _txt_cache:
            return _txt_cache[file_path]

        data_dict = {}
        try:
            with renpy.file(file_path, encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line and "=" in line:
                        key, value = line.split("=", 1)
                        key = key.strip()
                        value = value.strip()

                        # Detectar tipo
                        if value.lower() in ("true", "false"):
                            value = value.lower() == "true"
                        else:
                            try:
                                value = int(value)
                            except ValueError:
                                try:
                                    value = float(value)
                                except ValueError:
                                    pass  # deja como string

                        data_dict[key] = value

            # Guardar en caché
            _txt_cache[file_path] = data_dict
            return data_dict

        except Exception as e:
            renpy.notify(f"Error in reality action .ls {file_path}: {e}")
            return {}

    def reload_LS_txt_cache(file_path):
        if file_path in _txt_cache:
            del _txt_cache[file_path]


    def reload_all_LS_txt():
        paths = list(_txt_cache.keys())
        for path in paths:
            del _txt_cache[path]
            LS_data_txt(path)  # Vuelve a cargarlo al vuelo



init -11 python:

    _csv_cache = {}

    def LS_data_csv(file_path):
        """
        Carga un archivo .csv con columnas: key,value
        Devuelve un diccionario con caché.
        Detecta int, float y bool automáticamente.
        """
        if file_path in _csv_cache:
            return _csv_cache[file_path]

        data_dict = {}

        try:
            with renpy.file(file_path, encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    key = row.get("key")
                    value = row.get("value")

                    if key is None:
                        continue

                    value = value.strip()

                    # auto-type
                    if value.lower() in ("true", "false"):
                        value = value.lower() == "true"
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            try:
                                value = float(value)
                            except ValueError:
                                pass

                    data_dict[key] = value

            _csv_cache[file_path] = data_dict
            return data_dict

        except Exception as e:
            renpy.notify(f"CSV load error {file_path}: {e}")
            return {}

    def reload_LS_csv_cache(file_path):
        if file_path in _csv_cache:
            del _csv_cache[file_path]

    def reload_all_LS_csv():
        paths = list(_csv_cache.keys())
        for path in paths:
            del _csv_cache[path]
            LS_data_csv(path)





init -11 python:

    def LS_data(file_path):
        if file_path.endswith(".csv"):
            return LS_data_csv(file_path)
        else:
            return LS_data_txt(file_path)  # tu función antigua










init -11 python:

    _json_cache = {}

    def JSON_(file_path):
        """
        Carga un archivo .json con formato claves y valor.
        Devuelve un diccionario, usando caché si ya fue leído antes.
        """
        try:
            if file_path in _json_cache:
                return _json_cache[file_path]

            if not renpy.loadable(file_path):
                raise RuntimeError(f"{file_path} no se puede cargar todavía (modo de predicción).")

            if file_path.endswith(".json"):
                with renpy.file(file_path, encoding="utf-8") as f:
                    data = json.load(f)
                    _json_cache[file_path] = data  # Guardar en caché
                    return data

        except FileNotFoundError:
            renpy.notify(f"File {file_path} not found.")
            return {}
        except json.JSONDecodeError:
            renpy.notify(f"Error de formato en {file_path}.")
            return {}


    def reload_json_cache(file_path):
        if file_path in _json_cache:
            del _json_cache[file_path]


    def reload_all_json():
        paths = list(_json_cache.keys())
        for path in paths:
            del _json_cache[path]
            JSON_(path)  # Vuelve a cargarlo al vuelo
            print(f"Recargado JSON: {path}")





init python:
    def reload_multiple_objects(clear_memory=True):
        if clear_memory:
            renpy.free_memory()
        reload_all_json()
        reload_all_LS_txt()
        reload_all_LS_csv()
        reload_csv_gift()        
# init python:
#     def fix_data_after_load():
#         global love_, time_p, health_character, afecto, bag_inv

#         love_ = Love(love_.name, love_.quantity, love_.quantity_max)
        #time_p = Time(time_p.hora)
        #health_character = Health(health_character.name, health_character.scale)
        #afecto = Affection(afecto.name, afecto.quantity, afecto.quantity_max)
        #bag_inv = Bag()
        #inv_object = InvObjectGift()
        #combiner_inv = GiftCombiner(bag_inv)

        #money_player = Money(money_player.name, money_player.quantity, money_player.quantity_max)
    # Más ajustes...

    #config.after_load_callbacks.append(fix_data_after_load)
##############################################################

# control de versiones

# 1.3.0 -> 1.3.2

init python:
    # Si la variable no existe, créala sincronizada con el valor real
    if not hasattr(persistent, "choice_option_off"):
        # Leer el valor REAL del setting del motor
        current = renpy.game.preferences.get("after choices")
        persistent.choice_option_off = current
    
init python:
    if not hasattr(persistent, "skip_option_off"):
        current = renpy.game.preferences.get("skip")
        persistent.skip_option_off = current

#######################################################################
# define dlcs = { }

# init 1 python:  # The `1` here ensures this always runs *after* the `dlcs = { }` declaration above
#     dlcs['The Second Journey'] = 'secondjourney_start'


# screen dlc_menu():
#     vbox:
#         for title, start_label in dlcs.items():
#             textbutton (title) action Start(start_label)

#######################################################################


# screen exec_with_delay(delay, action_):
#     timer (delay) action [ action_, Hide('exec_with_delay') ]



# def kate_condition():
#     return (kate_tutor_events
#             and day_cycle.current_weekday in [1, 3]
#             and day_cycle.current_part == 1
#             and day_cycle.actions_remaining == 1)


# if all(
#     kate_tutor_events,
#     day_cycle.current_weekday in [1, 3],
#     day_cycle.current_part == 1,
#     day_cycle.actions_remaining == 1
#     ):



# config.mouse = {
#     "default": [ ("gui/cursor.webp", 1, 1) ],
#     "hover": [
#         ("gui/cursor_hover_01.webp", 18, 0),
#         ("gui/cursor_hover_02.webp", 18, 0),
#         ("gui/cursor_hover_03.webp", 18, 0),
#         ("gui/cursor_hover_03.webp", 18, 0),
#         ("gui/cursor_hover_02.webp", 18, 0),
#         ("gui/cursor_hover_01.webp", 18, 0),
#     ],
#     "right": [ ("gui/turn_right.webp", 1, 1) ],
#     "left":  [ ("gui/turn_left.webp",  1, 1) ],
#     "up":    [ ("gui/turn_up.webp"),   1, 1  ],
#     "down":  [ ("gui/turn_down.webp"), 1, 1  ]
# }

##############################################################

label after_load:
    $ reload_multiple_objects() # recarga multiples objectos
    $ renpy.pause(1.0, modal=True, hard=True)
    #####################################
    

    return


