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

# Function to manage tasks for staff
def assign_task(task, staff):
    return f"Task '{task}' has been assigned to {staff}."

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

# Section 2: Display and manage inventory
st.header("Inventory Management")
if st.button("Check Inventory"):
    st.write("Current inventory levels:")
    for item, stock in inventory.items():
        st.write(f"{item}: {stock} remaining")

# Section 3: Assign tasks to staff
st.header("Staff Task Assignment")
tasks = ["Take orders", "Prepare food", "Deliver orders", "Clean tables", "Restock inventory"]
staff_list = ["Staff 1", "Staff 2", "Staff 3", "Staff 4"]

# Input for task assignment
task = st.selectbox("Select task", tasks)
staff = st.selectbox("Assign to", staff_list)

# Assign task button
if st.button("Assign Task"):
    task_result = assign_task(task, staff)
    st.write(task_result)

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

# Section 5: Generate simple sales report
st.header("Sales Report Generation")
sales_data = {
    "Pizza": 100,
    "Burger": 80,
    "Pasta": 60,
    "Salad": 40,
    "Drinks": 200
}

if st.button("Generate Sales Report"):
    st.write("Sales report:")
    for item, sales in sales_data.items():
        st.write(f"{item}: {sales} units sold")

