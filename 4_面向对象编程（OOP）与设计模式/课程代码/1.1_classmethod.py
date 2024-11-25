class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls(size="Medium", toppings=["Tomato", "Mozzarella", "Basil"])

    @classmethod
    def pepperoni(cls):
        return cls(size="Large", toppings=["Tomato", "Mozzarella", "Pepperoni"])

    @classmethod
    def custom(cls, size, toppings):
        return cls(size=size, toppings=toppings)

    def __str__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings})"

# 使用工厂方法创建不同类型的披萨
margherita_pizza = Pizza.margherita()
pepperoni_pizza = Pizza.pepperoni()
custom_pizza = Pizza.custom(size="Small", toppings=["Tomato", "Mozzarella", "Mushrooms"])

print(margherita_pizza)  # 输出: Pizza(size=Medium, toppings=['Tomato', 'Mozzarella', 'Basil'])
print(pepperoni_pizza)   # 输出: Pizza(size=Large, toppings=['Tomato', 'Mozzarella', 'Pepperoni'])
print(custom_pizza)      # 输出: Pizza(size=Small, toppings=['Tomato', 'Mozzarella', 'Mushrooms'])