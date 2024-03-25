# OOP Family Ties: The Inheritance Insanity

# 1. Create a class Product with properties name, price, and quantity. 
# Create a child class Book that inherits from Product and adds a 
# property author and a method called read that prints information about the book.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author
    
    def read(self):
        book_information = super().print(f"{self.name}. book's author is {self.author}")
        print(book_information)

book1 = Book('Tini_zabutyh predkiv', 199.0, 5, 'M.Kotsiubynskyi')

book1.name



# 2. Create a class Restaurant with properties name, cuisine, and menu.
# The menu property should be a dictionary with keys being the dish name and
# values being the price.
# Create a child class FastFood that inherits from Restaurant and adds a
# property drive_thru (a boolean indicating whether the restaurant has
# a drive-thru or not) and a method called order, which takes in the dish name
# and quantity and returns the total cost of the order.
# The method should also update the menu dictionary to subtract the ordered
# quantity from the available quantity. If the dish is not available or
# if the requested quantity # is greater than the available quantity,
# the method should return a message indicating # that the order cannot be
# fulfilled.

menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}


class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish, quantity):
        if dish in self.menu:
            dish_details = self.menu[dish]
            if dish_details['quantity'] >= quantity:
                order_amount = quantity * dish_details['price']
                dish_details['quantity'] -= quantity
                return f'Total cost of your order: ${order_amount}'
            else:
                return 'The order cannot be fulfilled. No such q-ty'
        else:
            return 'There is no such dish in the menu'


# Example of usage:
fast_food_restaurant = FastFood("FastFood Restaurant", "Fast Food", menu, True)
print(fast_food_restaurant.drive_thru)

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available

#v1
    # @property
    # def drive_thru(self):
    #     order_list = input('Enter your order items (dish: quantity): ')
    #     order_dish, order_quantity = order_list.split(":")
    #     order_dish = order_dish.strip()
    #     order_quantity = int(order_quantity.strip())

    #     if order_dish in self.menu:
    #         details = self.menu[order_dish]
    #         if details['quantity'] >= order_quantity:
    #             order_amount = order_quantity * details['price']
    #             details['quantity'] -= order_quantity
    #             return f'Total cost of your order: ${order_amount}'
    #         else:
    #             return 'The order cannot be fulfilled'
    #     else:
    #         return 'There is no such dish in the menu'
#do not work for second question if it is out of menu
