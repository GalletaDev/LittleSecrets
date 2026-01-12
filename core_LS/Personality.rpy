

init 55 python:
    class NameCategory(object):
        def __init__(self, name, category_type=None, image_path=None, num=None):
            self.name = name
            self.category_type = category_type
            self.image_path = image_path
            self.num = num

        def __getstate__(self):
            return {
                "name": self.name,
                "category_type": self.category_type,
                "image_path": self.image_path,
                "num": self.num
            }

        def __setstate__(self, state):
            self.name = state.get("name", "Unknown")
            self.category_type = state.get("category_type", None)
            self.image_path = state.get("image_path", None)
            self.num = state.get("num", None)



        def __str__(self):
            if self.category_type == "special":
                return f"{self.name} ({{color=#F713FF}}{self.category_type}{{/color}})"
            elif self.category_type == "gold":
                return f"{self.name} ({{color=#E0D300}}{self.category_type}{{/color}})"
            elif self.category_type == "rare":
                return f"{self.name} ({{color=#32D40D}}{self.category_type}{{/color}})"
            else:
                return f"{self.name} ({{color=#6490FF}}{self.category_type}{{/color}})"

    class Category_g(object):
        def __init__(self):
            self.category = {}  # Diccionario para almacenar cantidades
            self.category_details = {}  # Diccionario para almacenar instancias de NameCategory
            self.personality_actions = {}


        def __getstate__(self):
            return {
                "category": self.category,
                "category_details": self.category_details,
                "personality_actions": self.personality_actions
            }

        def __setstate__(self, state):
            self.category = state.get("category", {})
            self.category_details = state.get("category_details", {})
            self.personality_actions = state.get("personality_actions", {})

        def add_category(self, name_category, quantity=1):
            num = name_category.num
            if num in self.category:
                if quantity > 1:
                    self.category[num] += quantity
                else:
                    self.category[num] = quantity
            else:
                self.category[num] = quantity
                self.category_details[num] = name_category

        def add_action(self, name_category, action):
            num = name_category.num
            if num in self.personality_actions:
                show_notification_error()
            else:
                self.personality_actions[num] = action


        def clear_all(self):
            self.category.clear()
            self.category_details.clear()
            self.personality_actions.clear()


        def get_quantity(self, category_name):
            return self.category.get(category_name.num, 0)

        def get_image(self, num):
            category = self.category_details.get(num, None)
            return category.image_path if category else None

        def get_type(self, num):
            category = self.category_details.get(num, None)
            return category.category_type if category else None
    
        def get_list_categories(self):
            category = [key for key, value in self.category_details.items()]
            category_text = "\n".join([str(value) for value in category])
            return category_text

        def get_list_actions(self):
            category_action = "\n".join([str(self.personality_actions[key]) for key in self.personality_actions.keys()])
            return category_action

        def remove_category(self, category_name, quantity=1):
            if category_name.num in self.category:
                if self.category[category_name.num] >= quantity:
                    self.category[category_name.num] -= quantity
                    if self.category[category_name.num] == 0:
                        del self.category[category_name.num]
                        #del self.category_details[category_name]
                else:
                    show_notification_error()
            else:
                show_notification_error()


        def execute_personalities(self):
            for numpe, action in self.personality_actions.items():
                if numpe in self.category:
                    action()


        def __str__(self):
            category_x_str = "\n".join([str(self.category_details[num]) for num in self.category.keys()])
            return f"{category_x_str}"





# ADD MAX LIMIT OF CATEGORY
init python:
    def add_max_(amount: int) -> int:
        global current_category_w
        if amount < 0:
            raise ValueError("The amount must not be negative")
        if current_category_w + amount <= max_category_w:
            current_category_w += amount
        else:
            current_category_w = max_category_w
        print(f"🛠️Add limit category>>>", amount)

    def sell_max_(amount: int) -> int:
        global current_category_w
        if amount < 0:
            raise ValueError("The amount must not be negative")
        if current_category_w >= amount:
            current_category_w -= amount
        else:
            current_category_w = 0
        print(f"🛠️Remove limit category>>>", -amount)


    def add_more_max_(amount: int) -> int:
        global max_category_w
        if amount < 0:
            raise ValueError("The amount must not be negative")
        max_category_w += amount
        if max_category_w > 10:
            max_category_w = 10
        print(f"🛠️Add limit max category>>>", amount)


    def remove_more_max_(amount: int) -> int:
        global max_category_w
        if amount < 0:
            raise ValueError("The amount must not be negative")
        max_category_w -= amount
        if max_category_w < 0:
            max_category_w = 0
        print(f"🛠️Remove limit max category>>>", -amount)
