menu = [
    ["Margherita Pizza", "Pepperoni Pizza", "BBQ Chicken Pizza"],
    ["Caesar Salad", "Greek Salad", "Tuna Salad"],
    ["Cheeseburger", "Veggie Burger", "Chicken Burger"]
]

search_ingredient = input("Enter an ingredient to search for in the menu: ").lower()

matching_dishes = []

for category in menu:
    for dish in category:
        if search_ingredient in dish.lower():
            matching_dishes.append(dish)

if matching_dishes:  
    print(f"\nDishes containing '{search_ingredient}':")
    for i, dish in enumerate(matching_dishes, 1):
        print(f"{i}. {dish}")
else:
    print(f"\nSorry, no dishes found containing '{search_ingredient}'.")
