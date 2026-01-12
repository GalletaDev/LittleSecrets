






# $ day_already_configured = False
# TIME GAME LOGIC
init python:

    class Time(object):
        def __init__(self, hora=0):
            self.hora = hora
            self.hora_max = 48
            self.fase_dia = "day"
            self.time_sound = 0
            self.key_proscess_day = set()
            """
            (Time) La class que se puede crear una hora con tiempo de 1 a 24 horas
            aunque llega mas de 24 ya que existe la noche roja.
            default value = Time() No hay que colocar nada
            """

        def add_time(self, hora=1):
            """
            Hace la funcion de avanzar el tiempo como lo especifica desde (Time)
            Automaticamente es 1 pero se puede colocar mas de 2 o 3
            $ value.add_time(), es opcional el numero que coloques
            no pueden ser numeros negativos
            """
            self.hora += hora
            if self.hora >= self.hora_max:
                self.hora -= self.hora
            # condition_status_good_and_bad()
            self.update()
            # print(f"📅Time moves on-->", hora)



        def __getstate__(self):
            return {
                'hora': self.hora,
                'hora_max': self.hora_max,
                'fase_dia': self.fase_dia,
                'time_sound': self.time_sound,
                'key_proscess_day': list(self.key_proscess_day),
            }

        def __setstate__(self, state):
            self.hora = state.get('hora', 0)
            self.hora_max = state.get('hora_max', 48)
            self.fase_dia = state.get('fase_dia', 'day')
            self.time_sound = state.get('time_sound', 0)
            self.key_proscess_day = set(state.get('key_proscess_day', []))
            self.update()


        def reset_timer(self):
            #day_already_configured = False
            self.hora -= self.hora
            self.update()


        def reset_all(self):
            """
            Vuelve a la hora inicial del dia
            y devuelve desde cero el tiempo
            """
            #day_already_configured = False
            self.hora -= self.hora
            self.run_phase_logic("reset", value=12, reset=True)

            self.update()


        def set_fase_dia(self, fase_dia):

            self.fase_dia = fase_dia
            self.update()
            print(f"📃🔍Set time-->", fase_dia)
            """
            Hace la Funcion desde (Time), se encarga de colocar una fase del dia.
            Como (day, day2, afternoom, afternoom2, night, night2, night3).
            $ value.set_fase_dia("day"), solo aceptar STR lo cual los numeros no se aceptan
            """
        def set_hora(self, hora):
            if 0 <= hora < self.hora_max:
                self.hora = hora
                self.update()
            else:
                raise ValueError("Time must be between 0 and {}".format(self.hora_max - 1))
            # print(f"📃🔍Set time-->", hora, "/", self.hora_max)

        def update(self):
            global bath_character, eat_character, sleep_character, night_red, activate_night_red, outside_girl, love_

            if self.hora < 8:
                self.fase_dia = "day" # Dia
                self.play_time_sound(1)
                # print(f"☀️Day-->", self.hora)


            elif self.hora < 14: # Dia 2
                self.fase_dia = "day2"
                self.run_phase_logic("day2", 1)
                # print(f"🌤️Day-->", self.hora)


            elif self.hora < 17: # Mediodia
                self.fase_dia = "afternoom"
                self.run_phase_logic("afternoom", None)
                self.play_time_sound(2)
                if outside_girl:
                    if love_.quantity <= 50:
                        pass
                    else:
                        if bath_character == True:
                            renpy.jump(fuction_name_bath + chr2_game.s_chr)

                print(f"⛅Afternoom-->", self.hora)
            elif self.hora < 19: # Mediodia 2
                self.fase_dia = "afternoom2"
                self.run_phase_logic("afternoom2", 2)
                # print(f"☁️Afternoom-->", self.hora)


            elif self.hora < 21: # Noche
                self.fase_dia = "night"
                self.run_phase_logic("night", None)
                self.play_time_sound(3)
                if outside_girl:
                    if love_.quantity <= 50:
                        pass
                    else:
                        if eat_character == True:
                            renpy.jump(fuction_name_eat + chr2_game.s_chr)
                # print(f"🌑Night-->", self.hora)

            elif self.hora < 24: # Noche 2
                self.fase_dia = "night2"
                self.run_phase_logic("night2", 3)
                # print(f"🌓Night-->", self.hora)

            elif self.hora < 38: # Luna roja
                if activate_night_red == True:
                    self.fase_dia = "night3"
                    self.run_phase_logic("night3", 4)
                    self.play_time_sound(4)
                    print(f"🌹🌕🌹Night red-->", self.hora)
                else:
                    self.fase_dia = "not_more"
                    self.run_phase_logic("not_more", 5, reset=True)
                    # print(f"💤<---Reset Time--->💤", self.hora)
                    renpy.jump("day_config")

            else: #No mas noches
                self.fase_dia = "not_more"
                self.run_phase_logic("not_more", 12, reset=True)
                # print(f"💤<---Reset Time--->💤", self.hora)
                renpy.jump("day_config")
            """
            Actualizador de dias. ofrece logica para que cuando pase el tiempo dia, mediodia, noche y la luna roja.
            Por si solo ya es automatico, ya que lo demas lo hace la funcion (add_time) o otros
            """


        def run_phase_logic(self, phase_name, value=0, reset=False):
            """
            Ejecuta la lógica de la fase solo si no se ha ejecutado antes.
            Reinicia todo si reset=True.
            """
            global bath_character, eat_character, sleep_character, night_red, activate_night_red

            if reset:
                # Reiniciar el set de fases ejecutadas al final del ciclo
                if phase_name == "reset":
                    self.key_proscess_day.clear()
                    if value == 12: # reininiciador ! = codigo 12
                        bath_character = False  
                        eat_character = False  
                        sleep_character = False  
                        night_red = False
                    else:
                        raise ValueError(f"""Error: 12, time reset not complete. 
                            (Config in run_phase_logic value!={value}, reset!={reset}, phase_name!={phase_name}); 
                            archive: System_time_game.rpy""")
                else: # Comportamiento normal
                    self.key_proscess_day.clear()

            elif phase_name not in self.key_proscess_day:
                if value == 1:
                    bath_character = True
                elif value == 2:
                    eat_character = True
                elif value == 3:
                    sleep_character = True
                elif value == 4:
                    night_red = True


                self.key_proscess_day.add(phase_name)          


        def play_time_sound(self, max_sound):
            """ Reproduce un sonido solo si no se ha alcanzado el límite. """
            if self.time_sound < max_sound:
                renpy.music.play("audio/sfx_min/tick.mp3", channel="sound", loop=False)
                self.time_sound += 1

        def __str__(self):
            return f"{self.hora}"