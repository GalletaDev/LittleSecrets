



init python:
    class Cube3Dfake(renpy.Displayable):
        def __init__(self, list_image, size=128, **kwargs):
            super(Cube3Dfake, self).__init__(**kwargs)
            self.images = [renpy.display.im.Image(img) for img in list_image]
            self.size = size
            self.count = len(self.images)
            self.dark_matrix = IdentityMatrix() * BrightnessMatrix(-0.15)

        def ease_in_out(self, t):
            # easing suave (acelera → frena)
            return t * t * (3 - 2 * t)

        def render(self, width, height, st, at):
            renpy.redraw(self, 0.01)

            r = renpy.Render(self.size * 3, self.size * 3)

            # tiempo normalizado en loop
            base = (math.sin(st * 2) + 1) / 2
            eased = self.ease_in_out(base)

            value = eased * (self.count - 1)
            idx = int(value)
            next_idx = min(idx + 1, self.count - 1)
            t = value - idx

            img_a = self.images[idx]
            img_b = self.images[next_idx]

            # oscurecer mediante efecto
            dark_strength = abs(t - 0.5) * 2  # 0 frontal, 1 lateral
            self.dark_matrix = IdentityMatrix() * BrightnessMatrix(-0.15 * dark_strength)
            # escalas fake 3D
            scale_a = 1.0 - t * 0.2
            scale_b = 0.9 + t * 0.2

            # renders con escala
            ra = renpy.render(img_a, int(self.size * scale_a), int(self.size * scale_a), st, at)
            rb = renpy.render(img_b, int(self.size * scale_b), int(self.size * scale_b), st, at)

            # aplicar oscuridad a la cara lateral
            img_a_dark = Transform(img_a, matrixcolor=self.dark_matrix)

            rb = renpy.render(
                img_a_dark,
                int(self.size * scale_a),
                int(self.size * scale_a),
                st,
                at
            )

            # alpha blending
            ra.alpha = int(t * 255)
            rb.alpha = int((1 - t) * 255)

            # offset lateral
            offset = int((t - 0.5) * 50)

            cx = self.size
            cy = self.size

            solid_shadow = Solid("#000")

            # ---- SOMBRA ----
            shadow = renpy.render(
                solid_shadow,
                int(self.size * 0.9),
                int(self.size * 0.25),
                st,
                at
            )
            shadow.alpha = 80  # ~0.3
            r.blit(shadow, (cx - 8, cy + self.size))

            # ---- CUBO ----
            r.blit(rb, (cx + offset, cy))
            r.blit(ra, (cx - offset, cy))

            return r








init python:
    class GlitchSlices(renpy.Displayable):
        def __init__(self, image="glitch_anchor.webp", max_offset=32, num_blocks=10, **kwargs):
            super(GlitchSlices, self).__init__(**kwargs)
            self.image = Image(image) # la imagen que usa
            self.max_offset = max_offset # maximo de movimiento de animacion izquierda y derecha
            self.num_blocks = num_blocks # numero de cuadros por segundo asi cambiara
            self.width = 1280
            self.height = 720

        def render(self, width, height, st, at):
            width = self.width
            height = self.height

            img_render = renpy.render(self.image, width, height, st, at)
            render = renpy.Render(img_render.width, img_render.height)

            block_height = img_render.height // self.num_blocks

            for i in range(self.num_blocks):
                y = i * block_height
                x_offset = random.randint(-self.max_offset, self.max_offset)
                clip_rect = (0, y, img_render.width, block_height)

                render.blit(img_render,
                            (x_offset, y),
                            clip_rect)

            renpy.redraw(self, 0.4)  # Redibuja cada 0.2s para animación fluida
            # puede saturar renpy si es menos
            return render




init python:

    class ParticuleGravity(renpy.Displayable):
        def __init__(self, image, count=12, max_radius=200, duration=1.0, max_size=64, gravity=300.0, **properties):
            super(ParticuleGravity, self).__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.duration = duration
            self.max_size = max_size
            self.gravity = gravity  # gravedad en pixeles por segundo^2
            self.start_time = None
            self.particles = []

            for i in range(count):
                angle = random.uniform(0, 2 * math.pi) # π
                speed = random.uniform(0.5, 1.0)
                scale = random.uniform(0.5, 1.0)
                initial_vy = random.uniform(-100, -300)  # velocidad vertical inicial (hacia arriba)

                self.particles.append({
                    "angle": angle,
                    "speed": speed,
                    "scale": scale,
                    "vy0": initial_vy,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            t = elapsed / self.duration

            if t >= 1.0:
                return renpy.Render(width, height)

            rv = renpy.Render(width, height)

            for p in self.particles:
                dist = self.max_radius * p["speed"] * t
                x = int(math.cos(p["angle"]) * dist)

                # Gravedad aplicada aquí
                vy = p["vy0"] + self.gravity * t  # velocidad final
                y = int(math.sin(p["angle"]) * dist + vy * t)

                size = int(self.max_size * p["scale"] * (1.0 - t))
                alpha = int(255 * (1.0 - t))

                particle_img = self.image
                cr = renpy.render(particle_img, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.02)
            return rv



init python:

    class AnimationCube(renpy.Displayable):
        def __init__(self, image, count=5, max_size=200, speed=1.0, frequency=1.0, amount=1.0, cycle_duration=2.0, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_size = max_size
            self.speed = speed
            self.amount = amount
            self.frequency = frequency
            self.cycle_duration = cycle_duration
            self.start_time = None

            # Fase temporal uniforme para cada copia
            self.offsets = [(i / count) * cycle_duration for i in range(count)]
            self.directions = [i * (2 * math.pi / count) for i in range(count)]  # distribución circular

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = (st - self.start_time) % self.cycle_duration
            base_size = 12
            rv = renpy.Render(self.max_size, self.max_size)

            for i in range(self.count):
                phase = (elapsed + self.offsets[i]) % self.cycle_duration

                # Normaliza a [0,1]
                norm_time = phase / self.cycle_duration

                # Cálculo del tamaño con expansión + temblor
                pulse = math.sin(norm_time * math.pi * 2 * self.frequency) * self.amount
                growth = norm_time  # ahora es de 0 a 1 uniforme
                size_factor = growth + pulse * (1 - growth)
                size = int(base_size + (self.max_size - base_size) * size_factor)

                cr = renpy.render(self.image, size, size, st, at)

                angle = self.directions[i]
                radius = 10 + 20 * growth
                dx = int(math.cos(angle) * radius)
                dy = int(math.sin(angle) * radius)

                x = self.max_size // 2 - size // 2 + dx
                y = self.max_size // 2 - size // 2 + dy

                rv.blit(cr, (x, y))

            renpy.redraw(self, 0.02)
            return rv




init python:

    class MultiPulseAnimation(renpy.Displayable):
        def __init__(self, image, count=6, max_size=150, cycle_duration=2.0, frequency=1.0, amount=0.2, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_size = max_size
            self.cycle_duration = cycle_duration
            self.frequency = frequency
            self.amount = amount
            self.start_time = None

            # Distribuir fases y direcciones uniformemente
            self.offsets = [(i / count) * cycle_duration for i in range(count)]
            self.directions = [i * (2 * math.pi / count) for i in range(count)]

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = (st - self.start_time) % self.cycle_duration
            base_size = 12
            render_surface = renpy.Render(self.max_size, self.max_size)

            for i in range(self.count):
                # Tiempo desplazado por copia
                phase = (elapsed + self.offsets[i]) % self.cycle_duration
                norm_time = phase / self.cycle_duration  # de 0 a 1

                # Expansión con pulso
                pulse = math.sin(norm_time * math.pi * 2 * self.frequency) * self.amount
                size_factor = norm_time + pulse * (1 - norm_time)
                size = int(base_size + (self.max_size - base_size) * size_factor)

                # Render individual
                cr = renpy.render(self.image, size, size, st, at)

                # Posición circular
                angle = self.directions[i]
                radius = 10 + 20 * norm_time
                dx = int(math.cos(angle) * radius)
                dy = int(math.sin(angle) * radius)

                x = self.max_size // 2 - size // 2 + dx
                y = self.max_size // 2 - size // 2 + dy

                render_surface.blit(cr, (x, y))

            renpy.redraw(self, 0.02)
            return render_surface




init python:
    class ExplosionParticles(renpy.Displayable):
        def __init__(self, image, count=12, max_radius=200, duration=1.0, max_size=64, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.duration = duration
            self.max_size = max_size
            self.start_time = None
            self.particles = []

            # Generar ángulos y velocidades aleatorios para cada partícula
            for i in range(count):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(0.5, 1.0)
                scale = random.uniform(0.5, 1.0)
                self.particles.append({
                    "angle": angle,
                    "speed": speed,
                    "scale": scale,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            t = elapsed / self.duration

            if t >= 1.0:
                return renpy.Render(width, height)  # Vacío después de explotar

            rv = renpy.Render(width, height)

            for p in self.particles:
                dist = self.max_radius * p["speed"] * t
                x = int(math.cos(p["angle"]) * dist)
                y = int(math.sin(p["angle"]) * dist)

                size = int(self.max_size * p["scale"] * (1.0 - t))  # Se hace más pequeña
                alpha = int(255 * (1.0 - t))  # Se desvanece

                particle_img = self.image
                cr = renpy.render(particle_img, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.02)
            return rv



init python:

    class AuraParticles(renpy.Displayable):
        def __init__(self, image, count=16, radius=40, speed=30, max_size=48, **props):
            super().__init__(**props)
            self.image = renpy.displayable(image)
            self.count = count
            self.radius = radius
            self.speed = speed
            self.max_size = max_size

            self.particles = [self.new_particle() for i in range(count)]

            # cache
            self.cached_images = {}
            for s in range(4, self.max_size + 1, 4):
                self.cached_images[s] = Transform(self.image, zoom=s/self.max_size)

        def new_particle(self):
            return {
                "angle": random.uniform(0, 2 * math.pi),
                "life": random.uniform(0.0, 1.0),
                "max_life": random.uniform(0.8, 1.4),
                "scale": random.uniform(0.4, 1.0),
            }

        def get_cached_image(self, size):
            s = min(self.cached_images.keys(), key=lambda k: abs(k - size))
            return self.cached_images[s]

        def render(self, width, height, st, at):
            renpy.redraw(self, 0.03)  # redraw

            rv = renpy.Render(width, height)
            cx = width // 2
            cy = height // 2

            for i, p in enumerate(self.particles):
                p["life"] += 0.016  # velocity life

                if p["life"] >= p["max_life"]:
                    self.particles[i] = self.new_particle()
                    p = self.particles[i]

                t = p["life"] / p["max_life"]

                dist = self.radius + t * self.speed
                x = int(math.cos(p["angle"]) * dist)
                y = int(math.sin(p["angle"]) * dist)

                size = int(self.max_size * p["scale"] * (1.0 - t))
                fade = 1.0 - t
                alpha = fade * fade  # 0.0 → 1.0
                alpha = max(0.0, min(alpha, 1.0))  # seguro

                img = self.get_cached_image(size)
                img_transform = Transform(img, alpha=alpha)

                rv.blit(renpy.render(img_transform, size, size, st, at),
                        (cx + x - size // 2, cy + y - size // 2))

            return rv








init python:

    class InfiniteSpiral(renpy.Displayable):
        def __init__(self, image, count=26, max_radius=250, max_size=128, spin_speed=6.0, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.max_size = max_size
            self.spin_speed = spin_speed
            self.start_time = None
            self.particles = []

            # Inicializar partículas distribuidas
            for i in range(count):
                angle = (i / count) * 2 * math.pi
                scale = random.uniform(0.5, 1.0)
                self.particles.append({
                    "angle": angle,
                    "scale": scale,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time

            rv = renpy.Render(width, height)

            for p in self.particles:
                # Movimiento circular + expansión/contracción cíclica
                # Usamos un seno para que se acerquen y se alejen constantemente
                phase = (elapsed * 0.5) % 1.0  # 0 → 1 en bucle
                radius = self.max_radius * abs(math.sin(phase * math.pi))

                # Ángulo base + giro infinito
                angle = p["angle"] + self.spin_speed * elapsed

                x = int(math.cos(angle) * radius)
                y = int(math.sin(angle) * radius)

                # Partículas con tamaño "palpitante"
                size_factor = 0.5 + 0.5 * math.sin(elapsed * 2 + p["angle"])
                size = int(self.max_size * p["scale"] * size_factor)
                cr = renpy.render(self.image, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.01)
            return rv



init python:

    class ChaoticSpiral(renpy.Displayable):
        def __init__(self, image, count=25, max_radius=300, max_size=64, spin_speed=4.0, **properties):
            super().__init__(**properties)
            self.image = renpy.displayable(image)
            self.count = count
            self.max_radius = max_radius
            self.max_size = max_size
            self.spin_speed = spin_speed
            self.start_time = None
            self.particles = []

            # Punto de fuga aleatorio (puede ser dentro o fuera del centro)
            self.focal_x = random.randint(-100, 100)
            self.focal_y = random.randint(-100, 100)

            # Configurar partículas con propiedades aleatorias
            for i in range(count):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(0.5, 1.5)     # cada una se expande a distinta velocidad
                spin_offset = random.uniform(-2, 2)  # diferencia en el giro
                scale = random.uniform(0.4, 1.2)
                self.particles.append({
                    "angle": angle,
                    "speed": speed,
                    "spin_offset": spin_offset,
                    "scale": scale,
                })

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            rv = renpy.Render(width, height)

            for p in self.particles:
                # Expansión radial caótica
                radius = self.max_radius * abs(math.sin(elapsed * p["speed"]))  # cada partícula late distinto

                # Ángulo base + giro infinito (desfasado por spin_offset)
                angle = p["angle"] + (self.spin_speed + p["spin_offset"]) * elapsed

                # Posición con punto de fuga (focal_x / focal_y)
                x = int(self.focal_x + math.cos(angle) * radius)
                y = int(self.focal_y + math.sin(angle) * radius)

                # Partículas con tamaño aleatorio + oscilación
                size_factor = 0.6 + 0.4 * math.sin(elapsed * 3 + p["angle"])
                size = int(self.max_size * p["scale"] * size_factor)

                cr = renpy.render(self.image, size, size, st, at)
                rv.blit(cr, (width // 2 + x - size // 2, height // 2 + y - size // 2))

            renpy.redraw(self, 0.02)
            return rv
















init python:

    class ScareText(renpy.Displayable):
        def __init__(self, child, square=2, **kwargs):
            super(ScareText, self).__init__(**kwargs)

            self.child = child

            self.square = square # The size of the square it will wobble within.
            # Include more variables if you'd like to have more control over the positioning.

        def render(self, width, height, st, at):
            # Randomly move the offset of the text's render.
            xoff = (random.random()-.8) * float(self.square)
            yoff = (random.random()-.8) * float(self.square)

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)

            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [ self.child ]

    def scare_tag(tag, argument, contents):
        new_list = [ ]
        if argument == "":
            argument = 5
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_text = Text(my_style.apply_style(char))
                    char_disp = ScareText(char_text, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if text.find("image") != -1:
                    tag, _, value = text.partition("=")
                    my_img = renpy.displayable(value)
                    img_disp = ScareText(my_img, argument)
                    new_list.append((renpy.TEXT_DISPLAYABLE, img_disp))
                elif not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))

        return new_list


    config.custom_text_tags["sc"] = scare_tag




init python:
    # import random
    # import math

    # This will maintain what styles we want to apply and help us apply them
    class DispTextStyle():
        # Notes:
        #   - "" denotes a style tag. Since it's usually {=user_style} and we partition
        #     it over the '=', it ends up being an empty string
        #   - If you want to add your own tags to the list, I recommend adding them
        #     before the ""
        #   - Self-closing tags should not be added here and should be handled
        #     in the text tag function.
        custom_tags = ["sc"]
        accepted_tags = ["", "b", "s", "u", "i", "color", "alpha", "font",  "size", "outlinecolor", "plain", 'cps']
        custom_cancel_tags = ["/" + tag for tag in custom_tags]
        cancel_tags = ["/" + tag for tag in accepted_tags]
        def __init__(self):
            self.tags = {}

        # For setting style properties. Returns false if it accepted none of the tags
        def add_tags(self, char):
            tag, _, value = char.partition("=") # Separate the tag and its info
            # Add tag to dictionary if we accept it
            if tag in self.accepted_tags or tag in self.custom_tags:
                if value == "":
                    self.tags[tag] = True
                else:
                    self.tags[tag] = value
                return True
            # Remove mark tag as cleared if should no longer apply it
            if tag in self.cancel_tags or tag in self.custom_cancel_tags:
                tag = tag.replace("/", "")
                self.tags.pop(tag)
                return True
            return False # If we got any other tag, tell the function to let it pass

        # Applies all style properties to the string
        def apply_style(self, char):
            new_string = ""
            # Go through and apply all the tags
            new_string += self.start_tags()
            # Add the character in the middle
            new_string += char
            # Now close all the tags we opened
            new_string += self.end_tags()
            return new_string

        # Spits out start tags. Primarily used for SwapText
        def start_tags(self):
            new_string = ""

            if "font" not in self.tags:
                new_string += "{font=font/lick_big.ttf}"
                new_string += "{color=#FF6E6E}"

            # Go through the custom tags
            for tag in self.custom_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            # Go through the standard tags
            for tag in self.accepted_tags:
                if tag in self.tags:
                    if self.tags[tag] == True:
                        new_string += "{" + tag + "}"
                    else:
                        new_string += "{" + tag + "=" +self.tags[tag] + "}"
            return new_string

        # Spits out ending tags. Primarily used for SwapText
        def end_tags(self):
            new_string = ""
            if "font" not in self.tags:
                new_string += "{/color}"
                new_string += "{/font}"

            # The only tags we are required to end are any custom text tags.
            # And should also end them in the reverse order they were applied.
            reversed_cancels = [tag for tag in self.custom_cancel_tags]
            reversed_cancels.reverse()
            for tag in reversed_cancels:
                temp = tag.replace("/", "")
                if temp in self.tags:
                    new_string += "{" + tag + "}"
            return new_string





# init python:
#     class TintMatrix(ColorMatrix):
#         def __init__(self, color):

#             # Store the color given as a parameter.
#             self.color = Color(color)

#         def __call__(self, other, done):

#             if type(other) is not type(self):

#                 # When not using an old color, we can take
#                 # r, g, b, and a from self.color.
#                 r, g, b = self.color.rgb
#                 a = self.color.alpha

#             else:

#                 # Otherwise, we have to extract from self.color
#                 # and other.color, and interpolate the results.
#                 oldr, oldg, oldb = other.color.rgb
#                 olda = other.color.alpha
#                 r, g, b = self.color.rgb
#                 a = self.color.alpha

#                 r = oldr + (r - oldr) * done
#                 g = oldg + (g - oldg) * done
#                 b = oldb + (b - oldb) * done
#                 a = olda + (a - olda) * done

#         # To properly handle premultiplied alpha, the color channels
#         # have to be multiplied by the alpha channel.
#             r *= a
#             g *= a
#             b *= a

#         # Return a Matrix.
#             return Matrix([ r, 0, 0, 0,
#                             0, g, 0, 0,
#                             0, 0, b, 0,
#                             0, 0, 0, a ])




# init python:

#     # Clase para las luces de fiesta
#     class PartyLight:
#         def __init__(self, width, height):
#             self.width = width
#             self.height = height
#             self.x = random.randint(0, width)
#             self.y = random.randint(0, height)
#             self.radius = random.randint(20, 50)
#             self.color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
#             self.speed_x = random.uniform(-2, 2)
#             self.speed_y = random.uniform(-2, 2)
#             self.angle = 0
#             self.angular_speed = random.uniform(-0.1, 0.1)

#         def update(self):
#             self.x += self.speed_x
#             self.y += self.speed_y
#             self.angle += self.angular_speed

#             # Rebotar en bordes
#             if self.x < 0 or self.x > self.width:
#                 self.speed_x *= -1
#             if self.y < 0 or self.y > self.height:
#                 self.speed_y *= -1

#         def draw(self, surface):
#             pulse = (math.sin(self.angle) + 1) / 2  # 0 a 1
#             color = tuple(min(255, int(c * pulse)) for c in self.color)
#             pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.radius)

#     # Displayable custom que usa pygame para dibujar las luces
#     class PartyLightDisplayable(renpy.Displayable):
#         def __init__(self, width=1280, height=720, num_lights=10, **kwargs):
#             super(PartyLightDisplayable, self).__init__(**kwargs)
#             self.width = width
#             self.height = height
#             self.lights = [PartyLight(width, height) for _ in range(num_lights)]
#             self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

#         def render(self, width, height, st, at):
#             # Actualizar posiciones y dibujar en surface pygame
#             self.surface.fill((0,0,0,0))  # Transparente

#             for light in self.lights:
#                 light.update()
#                 light.draw(self.surface)

#             # Convertir surface pygame a imagen Renpy
#             # img = Image(str(self.surface))
#             # return img.render(width, height, st, at)

#         def event(self, ev, x, y, st):
#             return None

#         def visit(self):
#             return [ ]

    # Registrar displayable para usar con show
    #renpy.exports.register_displayable("party_lights", PartyLightDisplayable)








#init 1 python:
    # import random

    # class NoiseBlock(renpy.Displayable):
    #     def __init__(self, width=24, height=24, **kwargs):
    #         super(NoiseBlock, self).__init__(**kwargs)
    #         self.width = width
    #         self.height = height

    #     def render(self, width, height, st, at):
    #         render = renpy.Render(self.width, self.height)

    #         # Dibuja píxeles en bloques con colores aleatorios en grises (efecto estática)
    #         for y in range(0, self.height, 4):
    #             for x in range(0, self.width, 4):
    #                 r = random.randint(0, 255)
    #                 g = random.randint(0, 255)
    #                 b = random.randint(0, 255)
    #                 color = (r, g, b, 255)

    #                 solid = Solid(color)
    #                 solid_render = renpy.render(solid, self.width, self.height, st, at)
    #                 render.blit(solid_render, (x, y))

    #         renpy.redraw(self, 0.1)  # Redibuja cada 0.05 seg para dar efecto de movimiento
    #         return render


    # screen_noise_block = Image("glitch_anchor.webp")






# init python:

#     class MeteorRain(renpy.Displayable):
#         def __init__(self, image, count=10, size=16, speed_range=(200, 400), duration=2.0, **kwargs):
#             super().__init__(**kwargs)
#             self.count = count
#             self.duration = duration
#             self.size = size
#             self.speed_range = speed_range
#             self.start_time = None
#             self.image = image

#             # Generar meteoritos con posiciones y velocidades
#             self.meteors = []
#             for _ in range(count):
#                 start_x = random.randint(0, 1920)  # asumiendo 1280x720
#                 start_y = random.randint(-322, -50)
#                 speed = random.uniform(*speed_range)
#                 angle = math.radians(random.randint(70, 110))  # inclinación hacia abajo

#                 self.meteors.append({
#                     "x": start_x,
#                     "y": start_y,
#                     "angle": angle,
#                     "speed": speed,
#                     "scale": random.uniform(0.5, 1.5),
#                 })

#         def render(self, width, height, st, at):
#             if self.start_time is None:
#                 self.start_time = st

#             elapsed = st - self.start_time
#             rv = renpy.Render(width, height)

#             for meteor in self.meteors:
#                 dx = math.cos(meteor["angle"]) * meteor["speed"] * elapsed
#                 dy = math.sin(meteor["angle"]) * meteor["speed"] * elapsed

#                 x = meteor["x"] + dx
#                 y = meteor["y"] + dy

#                 size_scaled = int(self.size * meteor["scale"])
#                 meteor_img = renpy.render(self.image, size_scaled, size_scaled, st, at)
#                 rv.blit(meteor_img, (x, y))

#             renpy.redraw(self, 0.02)
#             return rv



# image color_meteorit = Solid("#f00")

# image img_meteorit:
#     MeteorRain("color_meteorit", count=10, size=16, speed_range=(200, 400), duration=2.0)

# define meteorit_test = "img_meteorit"


# init python:
#     class TrackCursor(renpy.Displayable):

#         def __init__(self, child, paramod, **kwargs):

#             super(TrackCursor, self).__init__()

#             self.child = renpy.displayable(child)
#             self.x = 0
#             self.y = 0
#             self.actual_x = 0
#             self.actual_y = 0

#             self.paramod = paramod
#             self.last_st = 0



#         def render(self, width, height, st, at):

#             rv = renpy.Render(width, height)
#             minimum_speed = 0.5
#             maximum_speed = 3
#             speed = 1 + minimum_speed
#             mouse_distance_x = min(maximum_speed, max(minimum_speed, (self.x - self.actual_x)))
#             mouse_distance_y = (self.y - self.actual_y)
#             if self.x is not None:
#                 st_change = st - self.last_st

#                 self.last_st = st
#                 self.actual_x = math.floor(self.actual_x + ((self.x - self.actual_x) * speed * (st_change )) * self.paramod)
#                 self.actual_y = math.floor(self.actual_y + ((self.y - self.actual_y) * speed * (st_change)) * self.paramod)


#                 if mouse_distance_y <= minimum_speed:
#                     mouse_distance_y = minimum_speed
#                 elif mouse_distance_y >= maximum_speed:
#                     mouse_distance_y = maximum_speed

#                 cr = renpy.render(self.child, width, height, st, at)
#                 cw, ch = cr.get_size()
#                 rv.blit(cr, (self.actual_x, self.actual_y))



#             renpy.redraw(self, 0)
#             return rv

#         def event(self, ev, x, y, st):
#             hover = ev.type == pygame.MOUSEMOTION
#             click = ev.type == pygame.MOUSEBUTTONDOWN
#             mousefocus = pygame.mouse.get_focused()
#             if hover:

#                 if (x != self.x) or (y != self.y) or click:
#                     self.x = -x /self.paramod
#                     self.y = -y /self.paramod

