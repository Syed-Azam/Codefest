# PIZZA POINTS
# Create a function that takes a dictionary of customers, a minimum number of orders
# and a minimum order price. Return a list of customers that are eligible for a free pizza.

def pizza_points(customers, min_orders, min_price):
    elig = []
    for c in customers:
        if sum(i >= min_price for i in customers[c]) >= min_orders:
            elig.append(c)
    return elig

customers = {"Batman": [22, 30, 11, 17, 15, 52, 27, 12],
             "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45] }

print(pizza_points(customers, 5, 20))
print(pizza_points(customers, 3, 10))
print(pizza_points(customers, 5, 100))