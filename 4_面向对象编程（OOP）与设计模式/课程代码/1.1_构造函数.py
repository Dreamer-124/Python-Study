class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def __str__(self):
        return f"Pizza(size={self.size}, toppings={self.toppings})"

# 直接调用构造函数创建不同类型的披萨
margherita_pizza = Pizza(size="Medium", toppings=["Tomato", "Mozzarella", "Basil"])
pepperoni_pizza = Pizza(size="Large", toppings=["Tomato", "Mozzarella", "Pepperoni"])
custom_pizza = Pizza(size="Small", toppings=["Tomato", "Mozzarella", "Mushrooms"])

print(margherita_pizza)  # 输出: Pizza(size=Medium, toppings=['Tomato', 'Mozzarella', 'Basil'])
print(pepperoni_pizza)   # 输出: Pizza(size=Large, toppings=['Tomato', 'Mozzarella', 'Pepperoni'])
print(custom_pizza)      # 输出: Pizza(size=Small, toppings=['Tomato', 'Mozzarella', 'Mushrooms'])