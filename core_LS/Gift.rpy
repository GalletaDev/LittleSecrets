



init python:

    _gift_csv_cache = {}

    def CSV_GIFT_(path):
        if path in _gift_csv_cache:
            return _gift_csv_cache[path]

        data = {}

        with renpy.file(path, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data[row["id"]] = {
                    "price": int(row["price"]),
                    "image": row["image"]
                }

        _gift_csv_cache[path] = data
        return data

    def reload_csv_gift():
        paths = list(_gift_csv_cache.keys())
        for path in paths:
            del _gift_csv_cache[path]
            CSV_GIFT_(path)        




# Clase para manejar el inventario de regalos
init python:

    @renpy.pure
    class InvObjectGift(object):
        def __init__(self, limit=1):
            self.gf = {}  # Diccionario para almacenar regalos comprados
            self.gf_details = CSV_GIFT_("LS_archive/OBJ_GIFT.csv")
            self.limit = limit
            
        def buy_gift(self, name, quantity=1, buy=True):
            global money_player, bag_inv
            """Intenta comprar un regalo y actualizar el inventario."""

            if bag_inv.storage.get(name, 0) + quantity > 99:
                renpy.music.play("audio/sfx/alerta.mp3", channel='sound')
                dynamic_notify_error(_("Max 99"))
                return

            if buy:
                if name not in self.gf_details:  # 1. Verificar si el regalo existe
                    return dynamic_notify_error(_("El regalo no existe."))
                # if len(self.gf) >= self.limit:  # 2. Límite de inventario
                #     return 

                price = self.gf_details[name]["price"]

                if money_player.quantity < price:  # 3. Verificar dinero
                    dynamic_notify_error(_("No tienes suficiente dinero para este regalo."))
                else:
                    money_player.remove_money(price)
                    self.gf[name] = self.gf.get(name, 0) + quantity
            else:
                self.gf[name] = self.gf.get(name, 0) + quantity

        def remove_buy(self, name, quantity=1):
            if name in self.gf:
                if self.gf[name] >= quantity:
                    self.gf[name] -= quantity
                    if self.gf[name] == 0:
                        del self.gf[name]
                else:
                    show_notification_error()
            else:
                show_notification_error()

        def return_all_purchases(self):
            global money_player
            # Reembolsar todo el inventario
            for name, quantity in list(self.gf.items()):
                if name in self.gf_details:
                    price = int(self.gf_details[name]["price"])
                    money_player.add_money(price * quantity)
                else:
                    dynamic_notify_error(_("Error al cargar datos del regalo."))

            self.clear_all()
            dynamic_notify_error(_("Se te ha reembolsado con éxito."))

        def return_buy(self, name, quantity=1):
            global money_player

            if name in self.gf:
                if self.gf[name] >= quantity:
                    price = int(self.gf_details[name]["price"])
                    self.gf[name] -= quantity

                    if self.gf[name] == 0:
                        del self.gf[name]

                    money_player.quantity += price * quantity
                    renpy.music.play("audio/sfx/money_win.ogg", channel='sound')
                else:
                    dynamic_notify_error(_("No tienes suficientes unidades de este regalo para devolver."))
            else:
                dynamic_notify_error(_("Este regalo no está en tu inventario."))

        def clear_all(self):
            self.gf.clear()

        def __getstate__(self):
            return {
                "limit": self.limit,
                "gf": self.gf,
            }

        def __setstate__(self, state):
            self.limit = state.get("limit", 1)   # valor por defecto
            self.gf = state.get("gf", {})
            # recargar siempre JSON actualizado
            self.gf_details = CSV_GIFT_("LS_archive/OBJ_GIFT.csv")

        def get_image(self, gift_name):
            """Obtiene la ruta de la imagen para un regalo dado."""
            if gift_name in self.gf_details:
                return self.gf_details[gift_name]["image"]
            return "gui/button_object_screen/button_obj_none_hover.png"

        def message_():
            print("Notificación de la clase InvObjectGift")

        def get_quantity(self, *gf_names):
            """Obtiene la cantidad total de los regalos especificados."""
            return sum(self.gf.get(name, 0) for name in gf_names)

        def get_price(self, gift_name):
            """Obtiene la ruta de precios para un regalo dado."""      
            if gift_name in self.gf_details:
                return self.gf_details[gift_name]["price"]  
            return print(f"A fallado la busqueda del precio")                

        def all_available(self, *gf_names):
            """Verifica si todos los regalos especificados están disponibles."""
            return all(self.gf.get(name, 0) > 0 for name in gf_names)

        def __str__(self):
            """Retorna una representación de los regalos en el inventario."""
            return "\n".join([f"{name}" for name in self.gf.keys()])



# Instancia global del inventario de regalos
init python:
    
    @renpy.pure
    class Bag(object):
        def __init__(self):
            self.storage = {}  # Mochila con regalos

        def store_gift(self, name, quantity=1):
            global inv_object
            #name = str(name)
            # Verifica que tenga suficientes del regalo para mover a la mochila
            if inv_object.gf.get(name, 0) >= quantity:
                if self.storage.get(name, 0) + quantity > 99:
                    dynamic_notify_error(_("Max 99"))
                    return


                inv_object.gf[name] -= quantity
                self.storage[name] = self.storage.get(name, 0) + quantity

                # Borra si queda 0 en el inventario principal
                if inv_object.gf[name] == 0:
                    del inv_object.gf[name]
            else:
                dynamic_notify_error(_("No tienes suficientes regalos para guardar."))

        def __getstate__(self):
            return {
                "storage": self.storage
            }

        def __setstate__(self, state):
            self.storage = state.get("storage", {})


        def get_quantity(self, name):
            self.storage.get(name, 0)


        def remove_from_bag(self, name, quantity=1):
            global inv_object

            if self.storage.get(name, 0) >= quantity:
                self.storage[name] -= quantity
                #inv_object.gf[name] = inv_object.gf.get(name, 0) + quantity

                if self.storage[name] == 0:
                    del self.storage[name]
            else:
                dynamic_notify_error(_("No tienes suficientes de ese regalo en la mochila."))
            
            renpy.jump("dequip_gift_check")

        def message_():
            print("Notificacion de la clase en funcion Bag")

        def equip_gift(self, name, quantity=1):
            global inv_object

            if inv_object.gf.keys():
                dynamic_notify_error(_("Primero quita el que tienes en manos."))
            else:
                if self.storage.get(name, 0) > 0:
                    self.storage[name] -= quantity
                    inv_object.buy_gift(name=name, quantity=1, buy=False)

                    if self.storage[name] == 0:
                        del self.storage[name]
    
                else:
                    dynamic_notify_error(_("No tienes ese regalo en la mochila."))
            
            renpy.jump("equip_gift_check")







# Clase para combinar regalos
init python:

    @renpy.pure
    class GiftCombiner(object):
        def __init__(self, bag):
            self.bag = bag  # Ahora usamos la mochila, no la mano
            self.combinations = JSON_("data_library_json/OBJ_COMBINE.json") # ubicar esta vez directo

        def can_combine(self, combo_key):
            """
            Verifica si se puede hacer la combinación con lo que hay en la mochila.
            """
            if combo_key not in self.combinations:
                return False

            required_items = self.combinations[combo_key]["ingredients"]
            return all(self.bag.storage.get(item, 0) >= qty for item, qty in required_items.items())

        def combine(self, combo_key):
            """
            Intenta hacer la combinación usando objetos de la mochila.
            """
            if combo_key not in self.combinations:
                dynamic_notify_error(_("Esa combinación no existe."))
                return

            combo_data = self.combinations[combo_key]
            required = combo_data["ingredients"]
            result = combo_data["result"]
            result_qty = combo_data.get("quantity", 1)

            if not self.can_combine(combo_key):
                dynamic_notify_error(_("No tienes los objetos necesarios para crear esto."))
                return

            # Quitar los ingredientes de la mochila
            for item, qty in required.items():
                self.bag.storage[item] -= qty
                if self.bag.storage[item] <= 0:
                    del self.bag.storage[item]

            # Agregar el resultado a la mochila
            self.bag.storage[result] = self.bag.storage.get(result, 0) + result_qty

            renpy.music.play("audio/sfx/affection_sound.ogg", channel='sound')
            renpy.jump("combine_gift_check")


            #dynamic_notify(_("¡Has creado un nuevo objeto: [result]!").replace("[result]", result))

        def get_all_combinable(self):
            """
            Devuelve una lista de todas las combinaciones que se pueden hacer ahora mismo.
            """
            return [key for key in self.combinations if self.can_combine(key)]


        def missing_items(self, combo_key):
            """
            Devuelve un diccionario con los objetos que faltan y la cantidad que hace falta para una combinación.
            Si ya tienes todos, devuelve un diccionario vacío.
            """
            for combo_key in self.combinations:
                if combo_key.startswith("_"):
                    continue

            required_items = self.combinations[combo_key]["ingredients"]
            missing = {}

            for item, qty in required_items.items():
                owned = self.bag.storage.get(item, 0)
                if owned < qty:
                    missing[item] = qty - owned

            return missing

        def __getstate__(self):
            return {
                "bag": self.bag,
                "combinations": self.combinations,
            }

        def __setstate__(self, state):
            self.bag = state.get("bag", {})
            self.combinations = JSON_("data_library_json/OBJ_COMBINE.json")

        def message_():
            return print("Notificacion de la clase en funcion GiftCombiner")


        def get_combinations_status(self):
            result = []
            for combo_key, combo_data in self.combinations.items():
                # Ignorar claves que no sean combinaciones válidas
                if not isinstance(combo_data, dict) or "ingredients" not in combo_data:
                    continue

                missing = self.missing_items(combo_key, combo_data)
                result.append({
                    "key": combo_key,
                    "can_combine": len(missing) == 0,
                    "missing": missing
                })
            return result







# default equip_gift_ok = False

label equip_gift_check:
    $ renpy.notify("Gift equipped")
    # $ renpy.pause(0.1, hard=True)
    show screen screen_bag()
    if outside_home:
        call screen menu_option()
    else:
        python:
            screens = {
                "pizza": "menu_pizza",
                "movie": "menu_movie",
                "restaurant": "menu_restaurant",
                "park": "menu_park",
                "beach": "menu_beach",
                "shop": "menu_gift_select",
                "work1": "working_play",
                "work2": "working_play2",
                "work3": "working_play3",
                "work4": "working_play4"
            }
            scr = screens.get(location_choice_map, "menu_option")
        call screen expression scr 


label dequip_gift_check:
    $ renpy.notify("Gift removed")
    # $ renpy.pause(0.1, hard=True)
    show screen screen_bag()
    if outside_home:
        call screen menu_option()
    else:
        python:
            screens = {
                "pizza": "menu_pizza",
                "movie": "menu_movie",
                "restaurant": "menu_restaurant",
                "park": "menu_park",
                "beach": "menu_beach",
                "shop": "menu_gift_select",
                "work1": "working_play",
                "work2": "working_play2",
                "work3": "working_play3",
                "work4": "working_play4"
            }
            scr = screens.get(location_choice_map, "menu_option")

        call screen expression scr 

label bag_inv_check:
    # _return bag menu
    if outside_home:
        call screen menu_option()
    else:
        python:
            screens = {
                "pizza": "menu_pizza",
                "movie": "menu_movie",
                "restaurant": "menu_restaurant",
                "park": "menu_park",
                "beach": "menu_beach",
                "shop": "menu_gift_select",
                "work1": "working_play",
                "work2": "working_play2",
                "work3": "working_play3",
                "work4": "working_play4"
            }
            scr = screens.get(location_choice_map, "menu_option")
            
        call screen expression scr 



label combine_gift_check:
    $ renpy.notify("Combine gifts")
    show screen menu_select_combine()
    call screen menu_option()




# Efectos de objetos en personajes


