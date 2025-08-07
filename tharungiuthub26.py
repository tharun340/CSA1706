class FruitColorDB:
    def __init__(self):
        self.fruit_colors = {
            'apple': 'red',
            'banana': 'yellow',
            'grape': 'purple',
            'orange': 'orange',
            'lemon': 'yellow',
            'cherry': 'red',
            'blueberry': 'blue',
            'watermelon': 'green'
        }

    def color_of_fruit(self, fruit):
        return self.fruit_colors.get(fruit.lower())

    def fruits_of_color(self, color):
        color = color.lower()
        for fruit, fruit_color in self.fruit_colors.items():
            if fruit_color == color:
                yield fruit
db = FruitColorDB()

fruit = 'apple'
color = db.color_of_fruit(fruit)
print(f"The color of {fruit} is {color}.")

search_color = 'red'
print(f"Fruits with color {search_color}:")
for f in db.fruits_of_color(search_color):
    print(f"- {f}")
