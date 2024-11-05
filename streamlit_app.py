import streamlit as st

# Sample menu data with prices
menu = {
    "Pizza": 10,
    "Burger": 8,
    "Pasta": 12,
    "Salad": 6,
    "Drinks": 3
}

# Sample inventory for menu items
inventory = {
    "Pizza": 50,
    "Burger": 40,
    "Pasta": 30,
    "Salad": 20,
    "Drinks": 100
}


# Function to handle food orders and calculate price
def place_order(order_item, quantity):
    if inventory[order_item] >= quantity:
        inventory[order_item] -= quantity
        total_price = menu[order_item] * quantity
        return f"Order placed: {quantity} {order_item}(s). Total Price: ${total_price}. Remaining: {inventory[order_item]}"
    else:
        return f"Insufficient stock for {order_item}. Only {inventory[order_item]} left."



# Streamlit app UI
st.title("F&B Manpower Assistance System")

# Section 1: Display menu and handle orders
st.header("Menu and Order Automation")
st.write("Available menu items and prices:")

# Display menu
for item, price in menu.items():
    st.write(f"{item}: ${price}")

# Order input
st.write("Place an order:")
order_item = st.selectbox("Select item", list(menu.keys()))
quantity = st.number_input("Quantity", min_value=1, max_value=10)

# Place order button
if st.button("Place Order"):
    result = place_order(order_item, quantity)
    st.write(result)




# Section 4: Customer Support Automation
st.header("Customer Support Automation")
user_query = st.text_input("Ask a question (e.g., What is on the menu?)")
if st.button("Get Response"):
    if "menu" in user_query.lower():
        st.write("Our menu includes Pizza, Burger, Pasta, Salad, and Drinks.")
    elif "hours" in user_query.lower():
        st.write("We are open from 10 AM to 10 PM daily.")
    elif "location" in user_query.lower():
        st.write("We are located at 123 Main Street, Downtown.")
    elif "delivery" in user_query.lower():
        st.write("Yes, we offer delivery services within a 5-mile radius. Delivery charges apply based on the distance.")
    elif "payment" in user_query.lower():
        st.write("We accept cash, credit/debit cards, and mobile payments such as Apple Pay and Google Pay.")
    elif "promotion" in user_query.lower():
        st.write("We currently have a 10% discount on all pasta dishes and a free drink with every pizza order!")
    elif "reservation" in user_query.lower():
        st.write("We accept reservations. You can reserve a table by calling us at (123) 456-7890.")
    elif "allergy" in user_query.lower():
        st.write("Please inform us of any allergies, and we will do our best to accommodate your needs. We offer gluten-free and vegan options.")
    elif "refund" in user_query.lower():
        st.write("For refunds, please contact our customer support team. We handle refunds on a case-by-case basis.")
    else:
        st.write("Sorry, I didn't understand that. Please try again or contact customer support for more help.")


