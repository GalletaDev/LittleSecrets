

init python:

    @renpy.pure
    class Love(object): # AMOR CANTIDADES
        def __init__(self, name: str, quantity: int, quantity_max: int, **kwarg):
            self.name = name
            self.quantity = quantity
            self.quantity_max = quantity_max
            self._temp_cache = 0

        def add_love(self, quantity, random=False, max_=20, notify=True):
            ####################
            # register_log(f"Add love character =+{quantity}")
            ######################
            if quantity < 0:
                quantity = 0
            if random == False:
                self.quantity += quantity
            else:
                quantity += renpy.random.randint(1, max_)
                self.quantity += quantity

            persistent.record_love_d += quantity
            renpy.save_persistent()

            if self.quantity > self.quantity_max:
                self.quantity = self.quantity_max

            if notify:
                show_notification_love(quantity)           


        def get_quantity(self):
            return self.quantity


        # Método para serializar (guardar)
        def __getstate__(self):
            return {
                "name": self.name,
                "quantity": self.quantity,
                "quantity_max": self.quantity_max
            }

        # Método para deserializar (cargar)
        def __setstate__(self, state):
            self.name = state.get("name", _("Girl"))
            self.quantity = state.get("quantity", 0)
            self.quantity_max = state.get("quantity_max", 3000)
            self._temp_cache = 0  # se reconstruye con valor default

        def remove_love(self, quantity, random=False, max_=5, notify=True):
            if self.quantity <= 0:
                self.quantity = 0
                return None

            if quantity < 0:
                quantity = 0
            if self.quantity >= quantity:
                if random == False:
                    self.quantity -= quantity
                else:
                    quantity += renpy.random.randint(1, max_)
                    self.quantity -= quantity # no es necesario ya que 
            else:
                self.quantity = 0
            ####################
            # register_log(f"Remove love character ={-quantity}")
            ####################
            if notify:
                show_notification_love(-quantity)

            if dificulty_mode_game == "hard":
                self.quantity -= 1


        def __str__(self):
            return f"{self.quantity}/{self.quantity_max}"








init python:
    @renpy.pure
    class Lust(object):
        def __init__(self, name: str, quantity: int, quantity_max: int, **kwarg):
            self.name = name
            self.quantity = quantity
            self.quantity_max = quantity_max
            self._temp_cache = 0
        
        def get_quantity(self):
            return self.quantity

        # Método para serializar (guardar)
        def __getstate__(self):
            return {
                "name": self.name,
                "quantity": self.quantity,
                "quantity_max": self.quantity_max
            }

        # Método para deserializar (cargar)
        def __setstate__(self, state):
            self.name = state.get("name", _("Lujuria"))
            self.quantity = state.get("quantity", 0)
            self.quantity_max = state.get("quantity_max", 100)
            self._temp_cache = 0  # se reconstruye con valor default

        def add_lust(self, quantity, notify=True):
            ####################
            if quantity < 0:
                raise ValueError("The amount must be positive.")

            # persistent.record_affection_d += quantity
            # renpy.save_persistent()
            if self.quantity > self.quantity_max:
                self.quantity = self.quantity_max
            else:
                self.quantity += quantity

            if notify:
                show_notification_lust(quantity)            

        def remove_lust(self, quantity=1, notify=True):
            if self.quantity <= 0:
                self.quantity = 0
                return None
            if quantity < 0:
                raise ValueError("The amount must be positive.")
            if self.quantity >= quantity:
                self.quantity -= quantity
            if dificulty_mode_game == "hard":
                self.quantity -= 5
            if notify:
                show_notification_lust(-quantity)

        def reset_lust(self):
            self.quantity = 0
            return True
        

        def __str__(self):
            return f"{self.quantity}"





init python:

    @renpy.pure
    class Affection(object): # AFECTO CANTIDADES
        def __init__(self, name: str, quantity: int, quantity_max: int, **kwarg):
            self.name = name
            self.quantity = quantity
            self.quantity_max = quantity_max
            self._temp_cache = 0

        def add_affection(self, quantity, random=False, max_=20, x2=False, notify=True):
            ####################
            # register_log(f"Add affection character =+{quantity}")
            
            ####################
            if quantity < 0:
                raise ValueError("The amount must be positive.")
            if random == False:
                if x2 or dificulty_mode_game in ["pacific", "easy"]:
                    quantity += 30
                self.quantity += quantity
            else:
                quantity += renpy.random.randint(1, max_)
                if x2 or dificulty_mode_game in ["pacific", "easy"]:
                    quantity += 30
                self.quantity += quantity


            persistent.record_affection_d += quantity
            renpy.save_persistent()
            if self.quantity > self.quantity_max:
                self.quantity = self.quantity_max

            if notify:
                show_notification_affection(quantity)


        def get_quantity(self):
            return self.quantity

        # Método para serializar (guardar)
        def __getstate__(self):
            return {
                "name": self.name,
                "quantity": self.quantity,
                "quantity_max": self.quantity_max
            }

        # Método para deserializar (cargar)
        def __setstate__(self, state):
            self.name = state.get("name", _("Afecto"))
            self.quantity = state.get("quantity", 0)
            self.quantity_max = state.get("quantity_max", 10_000_00)
            self._temp_cache = 0  # se reconstruye con valor default

    
        def remove_affection(self, quantity=1, random=False, max_=5, notify=True):
            if self.quantity <= 0:
                self.quantity = 0
                return None

            if quantity < 0:
                quantity = 0
            if self.quantity >= quantity:
                if random == False:
                    self.quantity -= quantity
                else:
                    quantity += renpy.random.randint(1, max_)
                    if self.quantity <= 0:
                        self.quantity = 0
                    else:
                        self.quantity -= quantity
            else:
                self.quantity = 0

            if dificulty_mode_game == "hard":
                self.quantity -= 5

            if notify:
                show_notification_affection(-quantity)


        def __str__(self):
            return f"{self.quantity}"























default point_good = GoodAndBad(_("Bueno"), "good", 0, 100, "#00C713")
default point_bad = GoodAndBad(_("Malo"), "bad", 0, 100, "#FF0000")

init python:

    @renpy.pure
    class GoodAndBad(object): # Paciencia CANTIDADES
        def __init__(self, name: str, type: str,  quantity: int, quantity_max: int, color: str, **kwarg):
            self.name = name
            self.type = type
            self.quantity = quantity
            self.quantity_max = quantity_max
            self.color = color
            self._temp_cache = 0


        def add(self, quantity, random=False, max_=5, x2=False):
            if random:
                quantity += renpy.random.randint(1, max_)

            if self.type == "good":
                if x2:
                    quantity *= 2

                self.quantity += quantity

                if x2 or dificulty_mode_game in ["pacific", "easy"]:
                    quantity += 2

                if self.quantity > self.quantity_max:
                    self.quantity = self.quantity_max
            else:
                if x2 or dificulty_mode_game == "hard":
                    quantity += 2

                self.quantity += quantity  # sigue sumando, pero interpretás visualmente como “mal”
                if self.quantity > self.quantity_max:
                    self.quantity = self.quantity_max
        
            print(f"[{self.name}] actual: {self.quantity} / {self.quantity_max}")

        def get_quantity(self):
            return self.quantity
    

        def __getstate__(self):
            return {
                "name": self.name,
                "type": self.type,
                "quantity": self.quantity,
                "quantity_max": self.quantity_max,
                "color": self.color
            }

        # Método para deserializar (cargar)
        def __setstate__(self, state):
            self.name = state.get("name", _("Neutral"))
            self.type = state.get("type", "???")
            self.quantity = state.get("quantity", 0)
            self.quantity_max = state.get("quantity_max", 100)
            self.color = state.get("color", "#ffffff")
            self._temp_cache = 0  # se reconstruye con valor default



        def remove(self, quantity, random=False, max_=5):
            if quantity < 0:
                quantity = 0
            if self.quantity >= quantity:
                if random == False:
                    self.quantity -= quantity
                else:
                    quantity += renpy.random.randint(1, max_)
                    if self.quantity <= 0:
                        self.quantity = 0
                    else:
                        self.quantity -= quantity
            else:
                self.quantity = 0






        def __str__(self):
            if self.type == "good":
                return f"{{color={self.color}}}{self.quantity}/{self.quantity_max}"
            else:
                return f"{{color={self.color}}}{self.quantity}/{self.quantity_max}"






init python:

    def condition_status_good_and_bad():
        global dificulty_mode_game, point_good, point_bad, love_

        if dificulty_mode_game == "hard":
            if point_bad.quantity >= 100:
                love_.remove_love(0, True, 3)
            elif point_bad.quantity >= 50:
                if point_good.quantity <= 50:
                    love_.remove_love(0, True, 3)
                else:
                    love_.add_love(0, True, 2)  # <- puedes ajustar este valor si quieres
                point_good.remove(renpy.random.randint(0, 2))

            if point_good.quantity >= 50:
                love_.add_love(0, True, 1)
                point_good.add(1)
                point_bad.remove(renpy.random.randint(0, 1))   

        else:
            if point_bad.quantity >= 50:
                love_.remove_love(0, True, 1)
                point_bad.add(1)
                if point_bad.quantity >= 100:
                    point_good.remove(renpy.random.randint(1, 5))
                else:
                    point_good.remove(renpy.random.randint(0, 2))
                    
            if point_good.quantity >= 50:
                love_.add_love(0, True, 1)
                point_good.add(1)
                if point_good.quantity >= 100:
                    point_bad.remove(renpy.random.randint(2, 5))
                else:
                    point_bad.remove(renpy.random.randint(0, 2))




























init python:

    @renpy.pure
    class Money(object):
        def __init__(self, name: str, quantity: int, quantity_max: int, sims: str = "$", **kwarg):
            self.name = name
            self.quantity = quantity
            self.quantity_max = quantity_max
            self.amount = 0
            self.total_quantity = 0
            self.sims = sims
            self._temp_cache = 0  # se reconstruye con valor default

        def add_money(self, quantity, notify=True):

            # renpy.notify("!Actualizado¡")

            if quantity < 0:
                quantity = 0
            self.quantity += quantity
            self.quantity += self.amount
            if self.quantity > self.quantity_max:
                self.quantity = self.quantity_max
                self.amount = self.amount

            persistent.record_money_d += self.quantity
            renpy.save_persistent()

            renpy.music.play('audio/sfx/money_win.ogg', channel='sound')
            if notify:
                show_notification_money(quantity)
            #print(f"💲Add>>>", quantity)

        def add_up_money_day(self, amount=1):
            if amount < 0:
                raise ValueError("The amount must be positive.")
            self.amount += amount
            renpy.music.play('audio/sfx/money_win2.ogg', channel='sound')

        def add_money_bonus(self, notify=True):
            self.quantity += self.amount
            if self.quantity > self.quantity_max:
                self.quantity = self.quantity_max
            show_notification_money(self.amount)

        def get_quantity(self):
            return self.quantity


        # Método para serializar (guardar)
        def __getstate__(self):
            return {
                "name": self.name,
                "quantity": self.quantity,
                "quantity_max": self.quantity_max,
                "amount": self.amount,
                "total_quantity": self.total_quantity,
                "sims": self.sims
            }

        # Método para deserializar (cargar)
        def __setstate__(self, state):
            self.name = state.get("name", _("Dinero"))
            self.quantity = state.get("quantity", 0)
            self.quantity_max = state.get("quantity_max", 10_000_00)
            self.amount = state.get("amount", 0)
            self.total_quantity = state.get("total_quantity", 0)
            self.sims = state.get("sims", "$")
            self._temp_cache = 0  # se reconstruye con valor default


        def remove_money(self, quantity, notify=True):

            if quantity < 0:
                raise ValueError("The amount must be positive.")
            if self.quantity >= quantity:
                self.quantity -= quantity
            else:
                self.quantity = 0

            ####################
            #register_log(f"Add lust character ={-quantity}")
            ####################
            renpy.music.play('audio/sfx/money_cash.ogg', channel='sound')
            if notify:
                show_notification_money(-quantity)
            #print("💸Remove>>>", -quantity)



        def __str__(self):
            return f"{{font=font/Lato-Black.ttf}}{{color=#F00000}}{self.sims}{{/color}}({self.quantity})+({{color=#02BDFA}}Bonf.({self.amount}){{/color}}{{/font}})"
