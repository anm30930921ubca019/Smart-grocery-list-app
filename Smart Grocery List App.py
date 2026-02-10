import streamlit as st
import pandas as pd

st.title("🛒 Smart Grocery List App")

# Initialize session state
if "grocery_list" not in st.session_state:
    st.session_state.grocery_list = []

st.header("Add Grocery Item")

item = st.text_input("Item name")
quantity = st.number_input("Quantity", min_value=1, step=1)
price = st.number_input("Price per item", min_value=0.0, step=0.5)

if st.button("Add Item"):
    total = quantity * price
    st.session_state.grocery_list.append([item, quantity, price, total])
    st.success(f"{item} added successfully!")

# Display table
if st.session_state.grocery_list:
    df = pd.DataFrame(
        st.session_state.grocery_list,
        columns=["Item", "Quantity", "Price", "Total"]
    )

    st.header("Grocery List")
    st.dataframe(df)

    grand_total = df["Total"].sum()
    st.subheader(f"Total Cost: ₹ {grand_total:.2f}")

# Clear list
if st.button("Clear List"):
    st.session_state.grocery_list = []
    st.warning("List cleared!")
