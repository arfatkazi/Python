# concession stand program


menu = {
    
        "Cheeseburger": 120,
        "Veg Burger": 90,
        "Chicken Burger": 140,
        "Double Patty Burger": 180,
   
    
        "Margherita": 199,
        "Farmhouse": 249,
        "Pepperoni": 279,
        "BBQ Chicken": 299,
   
    
        "Regular Fries": 70,
        "Cheesy Fries": 90,
        "Onion Rings": 80,
        "Chicken Nuggets (6 pcs)": 120,
   
    
        "Veg Wrap": 100,
        "Chicken Wrap": 130,
        "Paneer Roll": 110,
        "Egg Roll": 90,
  
    
        "Coke (500ml)": 40,
        "Pepsi (500ml)": 40,
        "Iced Tea": 50,
        "Mineral Water": 20,
  
    
        "Chocolate Brownie": 80,
        "Vanilla Ice Cream": 60,
        "Sundae": 100,
        "Choco Lava Cake": 90
    
}


cart = []

total = 0






print("-----------------Menu---------------------")

for key,value in menu.items():
    print(f"{key:10}: {value:.2f}")

print("------------------------------------")

while True:
    food = input("Enter your favorite food (q to quit): ")
    if food.lower() == 'q':
        break

    elif menu.get(food) is not None:
        cart.append(food)
        total+=menu[food]
        print(f"Added '{food}' to cart. Subtotal: ₹{total}")
    else:
        print("❌ Item not found in the menu.")




print("-------------Final Bill----------------")
if cart:
    for item in cart:
         print(f"{item:25} ₹{menu[item]:.2f}")
    print(f"Total Amount:               ₹{total:.2f}")
else:
    print("No items ordered.")

print("------------------------------------")
