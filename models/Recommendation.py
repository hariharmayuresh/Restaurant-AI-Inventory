import streamlit as st
from Recommendation import Ingredient, Dish, Inventory, Menu, Restaurant

def setup_inventory_and_menu():
    # Create inventory and add ingredients
    inventory = Inventory()
    inventory.add_ingredient(Ingredient("spaghetti", 5))
    inventory.add_ingredient(Ingredient("tomato sauce", 3))
    inventory.add_ingredient(Ingredient("ground beef", 2))
    inventory.add_ingredient(Ingredient("fettuccine", 4))
    inventory.add_ingredient(Ingredient("alfredo sauce", 3))
    inventory.add_ingredient(Ingredient("romaine lettuce", 2))
    inventory.add_ingredient(Ingredient("croutons", 5))
    inventory.add_ingredient(Ingredient("Caesar dressing", 2))

    # Create menu and add dishes
    menu = Menu()
    menu.add_dish(Dish("Spaghetti Bolognese", [Ingredient("spaghetti", 1), Ingredient("tomato sauce", 1), Ingredient("ground beef", 0.5)], 10))
    menu.add_dish(Dish("Chicken Alfredo", [Ingredient("fettuccine", 1), Ingredient("alfredo sauce", 0.75), Ingredient("chicken breast", 0.5)], 8))
    menu.add_dish(Dish("Caesar Salad", [Ingredient("romaine lettuce", 1), Ingredient("croutons", 0.5), Ingredient("Caesar dressing", 0.25)], 6))

    return menu, inventory

def main():
    st.title("Restaurant Inventory and Menu Recommendation System")

    # Setup inventory and menu
    menu, inventory = setup_inventory_and_menu()

    # Create a restaurant instance
    restaurant = Restaurant(menu, inventory)

    # User selects a dish to check availability and get recommendation
    dish_names = [dish.name for dish in menu.dishes]
    selected_dish_name = st.selectbox("Select a dish to check availability:", dish_names)
    selected_dish = next(dish for dish in menu.dishes if dish.name == selected_dish_name)

    if st.button("Check Availability and Get Recommendation"):
        # Check if the selected dish is available
        if inventory.check_availability(selected_dish):
            st.success(f"{selected_dish.name} is available.")
            # Recommend the best-selling dish that is available
            recommended_dish = restaurant.recommend_dish()
            if recommended_dish:
                st.info(f"We recommend making {recommended_dish.name}.")
            else:
                st.error("No available dishes can be recommended at the moment.")
        else:
            st.error(f"{selected_dish.name} is not available due to insufficient ingredients.")

if __name__ == "__main__":
    main()